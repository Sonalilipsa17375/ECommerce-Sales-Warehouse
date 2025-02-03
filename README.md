# **ETL and Data Warehouse for E-Commerce Analytics**

This repository demonstrates the development of an end-to-end ETL pipeline and a data warehouse for analyzing e-commerce sales data. The project includes extracting, transforming, and loading data from an API, designing a relational data warehouse schema, and generating insights to support decision-making.

## Key Features
- **Data Ingestion**: Automated data retrieval from the [Fake Store API](https://fakestoreapi.com/).
- **Data Transformation**: Cleaning and normalizing raw data into structured tables.
- **Data Warehousing**: Implementation of a star schema in PostgreSQL for efficient analytics.
- I**nsights Generation**: SQL queries and Python scripts for actionable insights.

## Project Structure
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

## ETL Pipeline Overview
1. **Data Source**: Data is retrieved from the [Fake Store API](https://fakestoreapi.com/), providing information on:
    - **Products**: Titles, categories, prices, ratings.
    - **Users**: Customer details.
    - **Carts**: Order history and quantities.
    - **Categories**: Product categories.
2. **Ingestion**: The `ingestion.py` script fetches and stores raw JSON/CSV files in the `data/raw/` directory.
3. **Transformation**: The `transformation.py` script normalizes and cleans the raw data for loading into the warehouse.
4. **Data Warehouse**:
    - Schema: Designed as a star schema for fast and efficient querying.
    - Fact Table: `sales`.
    - Dimension Tables: `users`, `products`, `categories`, and `time`.
5. **Insights**: Key statistics and trends are generated using SQL queries and Python.

## Insights and Use Cases
- Total revenue by product category.
- Top customers by purchase amount.
- Sales trends over time (daily, monthly, yearly).
  
## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/WalidAlsafadi/ETL-Data-Warehouse
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure database and API details in `config/`

## Contributors

- [**Walid Alsafadi**](https://github.com/WalidAlsafadi) 
- [**Ameer Alzerei**](https://github.com/AmeerAlzerei)
- [**Hamza Obaid**](https://github.com/hobaid1) 
- [**Hazem Muanes**](https://github.com/HazemMuannes)
