# Generative AI — Learning & Project Repository

A structured Python project containing notebooks, utilities, datasets, and applications covering Generative AI, Machine Learning, and NLP fundamentals.

---

## Project Structure

```
GenerativeAI/
├── config/                        # Runtime configuration
│   ├── config.yaml                # Project settings & paths
│   └── config.json                # Additional configuration
│
├── data/                          # Organized data pipeline
│   ├── raw/                       # Raw input datasets
│   │   ├── churn/                 # Customer churn data
│   │   ├── covid/                 # COVID-19 images & labels (.npy, .csv)
│   │   ├── insurance/             # Insurance premium data
│   │   ├── reviews/               # Movie reviews data
│   │   ├── sales/                 # Sales & advertising data
│   │   ├── stock/                 # Stock prices & news data
│   │   └── other/                 # Miscellaneous datasets
│   ├── processed/                 # Cleaned, preprocessed data
│   ├── interim/                   # Intermediate transformation outputs
│   └── outputs/                   # Final results & predictions
│
├── notebooks/                     # Jupyter notebooks organized by type
│   ├── python-fundamentals/       # (3 notebooks) Intro Python & Pandas basics
│   ├── machine-learning/          # (14 notebooks) Linear regression deep dives
│   └── case-studies/              # (9 notebooks) End-to-end ML/AI projects
│
├── utils/                         # Reusable Python utilities & helpers
│   ├── __init__.py
│   ├── config.py                  # Environment detection & path configuration
│   ├── helpers.py                 # Common helper functions
│   ├── paths.py                   # Project path utilities
│   └── __pycache__/               # Python compiled files
│
├── .venv/                         # Virtual environment (gitignored)
├── .gitignore                     # Git ignore rules
├── requirements.txt               # Python package dependencies
├── setup.py                       # Package setup configuration
└── README.md                      # This file
```

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourname/GenerativeAI.git
cd GenerativeAI
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch Jupyter
```bash
jupyter lab
```
Navigate to `notebooks/` and start with a case study that interests you.

---

## Running Notebooks

### Locally with Jupyter Lab
```bash
jupyter lab
# Open any notebook from notebooks/case-studies/ or notebooks/machine-learning/
```

---

## Notebook Catalogue

| Folder | Count | Topic | Best For |
|---|---|---|---|
| `notebooks/python-fundamentals/` | 3 | Python basics & Pandas | Beginners learning Python |
| `notebooks/machine-learning/` | 14 | Linear regression deep dives | Understanding ML fundamentals |
| `notebooks/case-studies/` | 9 | **End-to-end ML/AI projects** | **→ See detailed guide below** |

---

## Case Studies — Detailed Guide

Each case-study notebook is a **production-ready, end-to-end project** demonstrating real-world ML/AI applications.

### 1. **Customer Churn Prediction** 🏦
**Objective:** Predict customers at risk of churning and develop retention strategies.

**What You'll Learn:**
- Banking customer behavior analysis with 10,127+ records
- Data preprocessing and feature engineering for classification
- Compare Decision Tree, Random Forest, Gradient Boosting models
- Class imbalance handling and business-focused metrics

**Key Insights:** Identify high-risk customers early to enable proactive retention and loyalty programs.

---

### 2. **COVID-19 Image Classification** 🏥
**Objective:** Build a deep learning CNN to classify chest X-rays as COVID-19 positive or negative.

**What You'll Learn:**
- Medical image preprocessing and normalization
- Convolutional Neural Network (CNN) architecture design
- Transfer learning and regularization techniques
- Model comparison: 2-layer vs 3-layer CNN for medical diagnosis
- Evaluation metrics critical in healthcare: sensitivity & recall

**Key Insights:** Achieve 97.37% test accuracy to support rapid, accessible COVID-19 screening.

---

### 3. **Health Insurance Premium Prediction** 💰
**Objective:** Build a regression model to predict health insurance premiums based on individual factors.

**What You'll Learn:**
- Regression modeling for continuous outcome prediction
- Demographic and health indicator feature analysis
- Multiple regression techniques (Linear, Ridge, Lasso, Random Forest, Gradient Boosting)
- Feature importance for underwriting and pricing decisions
- Business application in insurance pricing and risk management

**Key Insights:** Enable data-driven, risk-adjusted premium pricing strategies.

---

### 4. **Product Review Sentiment Analysis** ⭐
**Objective:** Build NLP models to classify product reviews as positive or negative sentiment.

**What You'll Learn:**
- Text preprocessing and normalization for NLP
- Feature extraction: Bag-of-Words, TF-IDF, Word2Vec embeddings
- Classification with Naive Bayes, SVM, Logistic Regression
- Sentiment analysis for e-commerce and brand monitoring
- Automated review processing at scale

**Key Insights:** Automate monitoring of customer sentiment to drive product improvements and marketing strategies.

---

### 5. **Movie Review Sentiment Analysis** 🎬
**Objective:** Develop sentiment classification using text embeddings and transformer models.

**What You'll Learn:**
- Word embeddings (Word2Vec) for semantic representation
- Transformer-based embeddings (BERT/Sentence Transformers)
- Deep learning with Keras and neural networks
- Contextual understanding of language
- Entertainment industry applications

**Key Insights:** Gauge audience reception and extract NLP insights from film reviews.

---

### 6. **Stock News Sentiment Analysis** 📈
**Objective:** Build an AI-driven system to classify financial news sentiment and support investment decisions.

**What You'll Learn:**
- Financial NLP and market sentiment analysis
- Chronological train/test splits to prevent data leakage
- Multiple embedding strategies: Bag-of-Words, Word2Vec, BERT
- Model comparison: Random Forest vs Neural Networks on text
- BERT + Neural Network achieving 80.28% accuracy on financial news
- Class imbalance handling in sentiment classification

**Key Insights:** Enable data-driven, real-time trading decisions through automated sentiment analysis.

---

### 7. **Sales vs Advertising Analysis** 📊
**Objective:** Build linear regression to quantify advertising impact on sales and optimize marketing budget.

**What You'll Learn:**
- Linear regression model development and interpretation
- Correlation analysis between marketing spend and revenue
- ROI calculation and business forecasting
- Model diagnostics: R², RMSE, residual analysis
- Data-driven budget allocation strategies

**Key Insights:** Calculate revenue per advertising dollar to optimize marketing ROI.

---

### 8. **Kartify E-commerce Chatbot** 🤖
**Objective:** Develop an NLU-based conversational AI for order queries and customer support.

**What You'll Learn:**
- Natural Language Understanding (NLU) and intent recognition
- Dialogue management and context tracking
- Integration with order management systems
- Multi-turn conversation handling
- Chatbot deployment strategies

**Key Insights:** Reduce support costs and improve customer experience through 24/7 automated assistance.

---

### 9. **Getting Started with Python** 🐍
**Objective:** Learn Python fundamentals through real-world retail analytics using WOW Superstore data.

**What You'll Learn:**
- Python basics: variables, data types, functions
- Data loading and exploration with pandas
- Data manipulation and statistical analysis
- Visualization with matplotlib and seaborn
- Real business analytics workflow

**Key Insights:** Foundation for all data science and ML work — essential prerequisite for other notebooks.

---

### How to Choose a Case Study

- **Interested in Customer Analytics?** → Start with Customer Churn Prediction
- **Want to Learn Deep Learning?** → Start with COVID-19 Image Classification
- **Passionate about NLP?** → Start with Stock News or Product Review Sentiment
- **Building Predictive Models?** → Start with Health Insurance Premium
- **Learning Python Basics?** → Start with Getting Started with Python
- **Exploring Business Analytics?** → Start with Sales vs Advertising

All case studies follow the same professional structure:
1. **Executive Summary** — Business context and objectives
2. **Problem Statement** — Business motivation and data overview
3. **Exploratory Data Analysis** — Understand patterns and distributions
4. **Data Preprocessing** — Clean and prepare for modeling
5. **Model Development** — Train and evaluate multiple models
6. **Results & Recommendations** — Key findings and deployment strategy

---

## Key Datasets (`data/`)

| Dataset | Case Study | Description |
|---|---|---|
| `stock_news.csv` | Stock News Sentiment Analysis | NASDAQ stock news (Jan–May 2019) with daily prices & sentiment labels |
| `Churn Prediction.csv` | Customer Churn Prediction | 10,127 bank customer records with churn status & behavioral features |
| `insurance_prediction.csv` | Health Insurance Premium | Customer demographics, health indicators, and insurance premium amounts |
| `movie_review.csv` | Movie Review Sentiment | Movie reviews with sentiment labels for NLP classification |
| `Product_Reviews.csv` | Product Review Sentiment | E-commerce product reviews with customer sentiment |
| `CovidImages.npy` / `CovidLabels.csv` | COVID-19 Image Classification | 251 chest X-ray images (128×128×3) labeled COVID vs Normal |
| `Sales.csv` / `WOWSuperstore.csv` | Sales vs Advertising & Python Fundamentals | Retail sales data with advertising spend and transaction details |
| `StockData.csv` / `Saved_StockData.csv` | Stock Price Analysis | Historical NASDAQ stock price data with volume & market metrics |
| `browbake_data.csv` / `data.csv` | Additional datasets | Miscellaneous datasets for exploratory analysis

---

## Utility Modules (`utils/`)

| Module | Purpose |
|---|---|
| `config.py` | Auto-detects environment (local vs cloud) and configures paths |
| `paths.py` | Defines project directory paths (RAW_DATA_DIR, PROCESSED_DATA_DIR, etc.) |
| `helpers.py` | Common utilities: `load_csv()`, `set_seed()`, data loading functions |
| `__init__.py` | Package initialization |

### Using Utilities in Your Code

```python
# Set up project paths and utilities
import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd().parent.parent))

from utils.helpers import load_csv, set_seed
from utils.paths import RAW_DATA_DIR, PROCESSED_DATA_DIR
from utils.config import load_config

# Load configuration and set random seed for reproducibility
cfg = load_config()
set_seed(cfg['model']['random_state'])

# Load dataset
df = load_csv('churn/ChurnPrediction.csv')

# Access data paths
images = np.load(RAW_DATA_DIR / 'covid' / 'CovidImages.npy')
```