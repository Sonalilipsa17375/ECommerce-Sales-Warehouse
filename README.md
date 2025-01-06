# Data Warehousing Final Project

This repository contains the deliverables for the Data Warehousing Final Project, including:
- Python scripts for ETL (data ingestion, transformation, modeling).
- A PostgreSQL data warehouse schema (star/snowflake).
- SQL queries and reports for generating insights.

## Directory Structure
```
ETL-Data-Warehoure/
├── README.md              # Project overview and setup instructions
├── .gitignore             # Ignored files and directories
├── .gitattributes         # Repository-specific attributes for file handling and language statistics
├── requirements.txt       # Python dependencies for the project
├── LICENSE                # Open-source license (Apache License 2.0)
├── data/                  # Raw and processed data
│   ├── raw/               # Downloaded or ingested raw data files
│   └── processed/         # Cleaned and transformed data files
├── scripts/               # Python scripts for ETL and modeling
│   ├── ingestion.py       # Script for data ingestion
│   ├── transformation.py  # Script for data transformation
│   ├── modeling.py        # Script for DW schema creation
│   └── stats.py           # Script to generate stats and insights
├── sql/                   # SQL scripts for schema creation and queries
│   ├── staging_schema.sql # SQL for staging schema
│   ├── dw_schema.sql      # SQL for data warehouse schema
│   └── queries.sql        # Example queries for stats
├── notebooks/             # Optional Jupyter notebooks for exploration
│   └── exploration.ipynb  # Data exploration notebook
├── config/                # Configuration files for APIs and DB
│   ├── db_config.json     # Database connection details
│   └── api_config.json    # API keys and configurations
└── reports/               # Generated reports and analysis
    └── stats_report.md    # Summary of findings and insights
```
## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/WalidAlsafadi/ETL-Data-Warehouse
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure database and API details in `config/`.

## Contributors

- **Walid Alsafadi**
- **Ameer Alzerei**
- **Hamza Obaid**
- **Hazem Muanes**
