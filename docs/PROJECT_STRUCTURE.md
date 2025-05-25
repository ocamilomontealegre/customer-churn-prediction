```bash
  customer_churn_prediction/
│
├── data/                    # Raw and processed data files
│   ├── raw/                 # Original data (e.g., CSVs, from DB)
│   └── processed/           # Cleaned/transformed data
│
├── database/                # SQL scripts and database setup
│   ├── create_tables.sql
│   └── load_data.py         # Script to insert CSV into Postgres
│
├── notebooks/               # Jupyter notebooks for exploration
│   ├── 01_exploration.ipynb
│   └── 02_modeling.ipynb
│
├── src/                     # Source code for data and modeling
│   ├── __init__.py
│   ├── data_loader.py       # Extracts data from PostgreSQL
│   ├── data_cleaning.py     # Cleans and transforms data
│   ├── feature_engineering.py
│   ├── model.py             # Model training and evaluation
│   └── visualization.py     # Data and model visualizations
│
├── models/                  # Trained models (Pickle or Joblib)
│   └── churn_model.pkl
│
├── reports/                 # Insights, conclusions, presentation
│   ├── figures/             # Save plots and visualizations
│   └── report.pdf or .pptx
│
├── app/                     # Optional Streamlit or Flask app
│   └── app.py
│
├── requirements.txt         # Python dependencies
├── README.md                # Project overview and instructions
└── .env                     # (Optional) DB credentials, secrets

```