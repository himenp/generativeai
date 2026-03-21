# Generative AI — Learning & Project Repository

A structured Python project containing notebooks, utilities, datasets, and applications covering Generative AI, Machine Learning, and NLP fundamentals.

---

## Project Structure

```
GenerativeAI/
├── config/                        # Runtime configuration
│   └── config.json
├── data/                          # All datasets (CSV, NPY, XLSX)
├── docs/
│   ├── guides/                    # GenAI & Colab reference PDFs
│   └── ml-sessions/               # ML session slide decks & summaries
├── notebooks/
│   ├── setup/                     # Google Colab setup notebook
│   ├── python-fundamentals/       # Intro Python & Pandas notebooks
│   ├── machine-learning/          # Linear regression hands-on notebooks
│   ├── case-studies/              # End-to-end case study notebooks
│   └── projects/                  # Submission-ready project notebooks
├── src/                           # Reusable Python utilities
│   ├── __init__.py
│   ├── config.py                  # Environment-aware path config
│   ├── data_loader.py             # Dataset loading helpers
│   └── notebook_init.py           # Notebook bootstrapping helpers
├── apps/
│   └── kartify/                   # Kartify chatbot Flask app + Dockerfile
├── .gitignore
├── requirements.txt
└── setup.py
```

---

## Getting Started

### 1. Create and activate a virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Jupyter
```bash
jupyter lab
```
Then open any notebook under `notebooks/`.

### 4. Google Colab
See `notebooks/setup/COLAB_SETUP.ipynb` for step-by-step Colab setup instructions.

---

## Notebook Catalogue

| Folder | Notebooks | Topic |
|---|---|---|
| `notebooks/setup/` | COLAB_SETUP | Google Colab environment setup |
| `notebooks/python-fundamentals/` | PythonForDataScience_intro, Hands_on_Notebook_Pandas | Python & Pandas basics |
| `notebooks/machine-learning/` | 14 notebooks | Linear regression, MSE, R², encoders |
| `notebooks/case-studies/` | 9 notebooks | Churn, insurance, sentiment, stock, COVID, chatbot |
| `notebooks/projects/` | Learner_Notebook_For_Submission + others | Final project submissions |

---

## Key Datasets (`data/`)

| File | Description |
|---|---|
| `stock_news.csv` | NASDAQ stock news + daily prices (sentiment analysis) |
| `Churn Prediction.csv` | Customer churn labels and features |
| `insurance_prediction.csv` | Health insurance premium prediction |
| `movie_review.csv` | Movie review text for sentiment analysis |
| `Product_Reviews.csv` | E-commerce product reviews |
| `CovidImages.npy` / `CovidLabels.csv` | COVID-19 chest X-ray image classification |
| `Sales.csv` / `WOWSuperstore.csv` | Retail sales data |
| `StockData.csv` / `Saved_StockData.csv` | Historical stock price data |

---

## Applications (`apps/`)

### Kartify Order Query Chatbot
A Flask-based GenAI chatbot for order status queries backed by a SQLite database.

```bash
cd apps/kartify
pip install flask openai
python app.py
```

Or run via Docker:
```bash
docker build -t kartify .
docker run -p 5000:5000 kartify
```

---

## Utility Modules (`src/`)

| Module | Purpose |
|---|---|
| `config.py` | Auto-detects Colab vs local environment and sets `data_path` |
| `data_loader.py` | Helper functions for loading project datasets |
| `notebook_init.py` | Bootstraps path setup at the top of any notebook |

Usage in a notebook:
```python
import sys
sys.path.insert(0, '../../src')
from config import CONFIG
data_path = CONFIG['data_path']
```
