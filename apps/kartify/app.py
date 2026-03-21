import streamlit as st
import sqlite3
import pandas as pd
import os
import json
from langchain.chat_models import ChatOpenAI
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain.schema import HumanMessage



# Load the JSON file and extract values
file_name = os.path.join(os.path.dirname(__file__), 'config.json')
with open(file_name, 'r') as file:
    config = json.load(file)
    API_KEY = config.get("API_KEY") # Loading the API Key
    OPENAI_API_BASE = config.get("OPENAI_API_BASE") # Loading the API Base Url

# Set API keys and base
os.environ['OPENAI_API_KEY'] = API_KEY
os.environ['OPENAI_BASE_URL'] = OPENAI_API_BASE

llm = ChatOpenAI(model_name="gpt-4")

connection = sqlite3.connect("kartify.db", check_same_thread=False)
kartify_db = SQLDatabase.from_uri("sqlite:///kartify.db")
sqlite_agent = create_sql_agent(llm, db=kartify_db, agent_type="openai-tools", verbose=False)

def policy_tool_func(input: str) -> str:
    prompt = f"""Only respond about return or replacement if the user has explicitly asked about it in their query.
Use the following context from order, shipment, and product policy data:
{input}
Your task (only if return or replacement is mentioned):
1. Check eligibility based on `actual_delivery` and product policy:
   - If `return_days_allowed` is 0, clearly state the product is not eligible for return.
   - If within window, mention last date allowed for return and replacement.
   - If the window has passed, say so.
2. Mention return conditions (e.g., “Sealed only”).
3. If `actual_delivery` is null, return/replacement is not yet applicable.
4. If any required info is missing, say so politely that i am connecting to human support.
If the query does **not** mention return or replacement, do **not** include any information about it in your response.
Respond clearly and briefly — no system or SQL steps."""
    return llm([HumanMessage(content=prompt)]).content.strip()

def answer_generation_tool(input: str) -> str:
    prompt = f"""You are a polite and formal customer assistant replying to a user query to customer about return, replacement, delivery, cancellation, or address change.
Use the context provided below:
{input}
Guidelines:
- Respond in a short, formal, and factual tone.
- Do **not** add extra details that were not asked in the user's query.
- Do **not** format like an email — avoid greetings, sign-offs, or explanations.
- Do not offer return/replacement windows unless directly asked.
- Do not mention cancellation or refund policies unless cancellation is requested.
- Do not mention address change policy until asked.
- If the product has **not been delivered**, mention that return/replacement cannot be processed yet.
- If the product **has been delivered**, calculate based on delivery date whether return or replacement is still allowed.
- If the order has already **shipped**, reply that address changes are not possible.
- If any required info is missing, say so politely that i am connecting to human support.
- If you do not what to answer now, say so politely that i am connecting to human support.
- Never ask for any bank details
Output:
- Return only a single, relevant customer-facing message — no system instructions, reasoning, or metadata.
"""
    return llm([HumanMessage(content=prompt)]).content.strip()

def output_guard_check(model_output: str) -> str:
    prompt = f"""
You are a content safety assistant. Your task is to classify if the assistant's response is appropriate.
If the message contains:
- Requests for bank details, OTPs, account numbers
- Harassment or offensive tone
- Privacy concerns or unsafe advice
- Misunderstanding and miscommunication word
- Phrases like "please contact customer service" or redirection to a human agent
- Escalated this to our support team
Return: BLOCK
Otherwise, return: SAFE
Response: {model_output}
Output:
"""
    return llm.predict(prompt).strip()

def evaluate_response_quality(context: str, query: str, response: str) -> dict:
    prompt = f"""Evaluate the assistant's response to a customer query using the provided order context.

    Context: {context}
    Customer Query: {query}
    Assistant's Response: {response}

     Instructions:
      1. **Groundedness (0.0 to 1.0)**: Score based on how well the response is factually supported by the context. 
                                      - Score closer to 1 if all facts are accurate and derived from the context.
                                      - Score closer to 0 if there is hallucination, guesswork, or any fabricated information.

      2. **Precision (0.0 to 1.0)**: Score based on how directly and accurately the assistant addresses the query.
                                      - Score closer to 1 if the response is concise, focused, and answers the exact user query.
                                      - Score closer to 0 if it includes irrelevant details or misses the main point.

        Output format (JSON only):    
        
           groundedness: float between 0 and 1 ,
             precision: float between 0 and 1
        
        Only return the JSON. No explanations.

"""
    score = llm.predict(prompt).strip()
    try:
        return eval(score)
    except:
        return {"groundedness": 0.0, "precision": 0.0}


def conversation_guard_check(history) -> str:
    chat_summary = "\n".join([f"Customer: {h['user']}\nAssistant: {h['assistant']}" for h in history])
    prompt = f"""
You are a conversation monitor AI. Review the entire conversation and classify if the assistant:
- Repeatedly offered unnecessary return or replacement steps
- Gave more than what the user asked
- Missed signs of customer distress
- Ignored user's refusal of an option
If any of the above are TRUE, return BLOCK
Else, return SAFE
Conversation:
{chat_summary}
Output:
"""
    return llm.predict(prompt).strip()

tools = [
    Tool(name="PolicyChecker", func=policy_tool_func, description="Check return and replacement eligibility."),
    Tool(name="AnswerGenerator", func=answer_generation_tool, description="Craft final response.")
]

order_agent = initialize_agent(tools, llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=False, handle_parsing_errors=True)

st.title("📦 Kartify Order Query Chatbot")

customer_id = st.text_input("Enter your Customer ID:")

if customer_id:
    query = """
        SELECT
            order_id,
            product_description
        FROM
            orders
        WHERE
            customer_id = ?
        ORDER BY order_date DESC
        """
    df = pd.read_sql_query(query, connection, params=(customer_id,))

    if not df.empty:
        selected_order = st.selectbox("Select your Order:", df["order_id"] + " - " + df["product_description"])
        start_chat = st.button("Start Chat")

        if start_chat:
            # Reset chat state except customer ID and order ID
            st.session_state.chat_history = []
            st.session_state.order_id = selected_order.split(" - ")[0]
            with st.spinner("Loading order details..."):
                order_context_raw = sqlite_agent.invoke(f"Fetch all columns for order ID {st.session_state.order_id}")
                st.session_state.order_context = f"Order ID: {st.session_state.order_id}\n{order_context_raw}\nToday's Date: 25 July"

    if "order_context" in st.session_state:
        st.markdown("### Chat with Assistant")

        for msg in st.session_state.chat_history:
            st.chat_message("user").write(msg["user"])
            st.chat_message("assistant").write(msg["assistant"])

        user_query = st.chat_input("How can I help you?")
        
        if user_query:
            intent_prompt = f"""You are an intent classifier for customer service queries. Your task is to classify the user's query into one of the following 3 categories based on tone, completeness, and content.
Return **only the numeric category ID (0, 1, 2 and 3)** as the output. Do not include any explanation or extra text.
### Categories:
0 — **Escalation**
- The user is very angry, frustrated, or upset.
- Uses strong emotional language (e.g., “This is unacceptable”, “Worst service ever”, “I’m tired of this”, “I want a human now”).
- Requires **immediate human handoff**.
- Escalation confidence must be very high (90% or more).
1 — **Exit**
- The user is ending the conversation or expressing satisfaction.
- Phrases like “Thanks”, “Got it”, “Okay”, “Resolved”, “Never mind”.
- No further action is required.
2 — **Process**
- The query is clear and well-formed.
- Contains enough detail to act on (e.g., mentions order ID, issue, date).
- Language is polite or neutral; the query is actionable.
- Proceed with normal handling.
3- **Random Question**
- If user asked something not related to order
example - What is NLP
---
Your job:  
Read the user query and return just the category number (0, 1, 2, or 3). Do not include explanations, formatting, or any text beyond the number.
User Query: {user_query}"""
            intent = llm.predict(intent_prompt).strip()

            if intent == "0":
                response = "Sorry for the inconvenience. A human agent will assist you shortly 1."
            elif intent == "1":
                response = "Thank you! I hope I was able to help."
            elif intent == "3":
                response = "Apologies, I’m currently only able to help with information about your placed orders. Please let me know how I can assist you with those!"
            else:
                full_prompt = f"""
                    Context:
                    {st.session_state.order_context}
                    Customer Query: {user_query}
                    Previous response: {st.session_state.chat_history}
                    Use tools to reply.
                    """
                with st.spinner("Generating response..."):
                    raw_response = order_agent.run(full_prompt)

                    # Step 1: Evaluate quality (Groundedness and Precision first)
                    scores = evaluate_response_quality(st.session_state.order_context, user_query, raw_response)
                    if scores["groundedness"] < 0.75 or scores["precision"] < 0.75:
                        regenerated_response = order_agent.run(full_prompt)
                        scores_retry = evaluate_response_quality(st.session_state.order_context, user_query, regenerated_response)
                        if scores_retry["groundedness"] >= 0.75 and scores_retry["precision"] >= 0.75:
                            response = regenerated_response
                        else:
                            response = "Your request is being forwarded to a customer support specialist. A human agent will assist you shortly."
                    else:
                        response = raw_response
                    
                    # Step 2: Guard check (after passing quality check)
                    if response not in [
                        "Your request is being forwarded to a customer support specialist. A human agent will assist you shortly."
                    ]:
                        guard = output_guard_check(response)
                        if guard == "BLOCK":
                            response = "Your request is being forwarded to a customer support specialist. A human agent will assist you shortly."
                    
                    # Save chat history
                    st.session_state.chat_history.append({"user": user_query, "assistant": response})
                    
                    # Step 3: Conversation-level safety
                    conv_check = conversation_guard_check(st.session_state.chat_history)
                    if conv_check == "BLOCK":
                        response = "Your request is being forwarded to a customer support specialist. A human agent will assist you shortly."


            st.chat_message("user").write(user_query)
            st.chat_message("assistant").write(response)
            

else:
    st.info("Please enter a Customer ID to begin.")