# **E-Commerce Sales Data Warehouse**

This repository showcases the development of a complete ETL pipeline and a data warehouse tailored for e-commerce analytics. It includes data ingestion from APIs, data transformation, schema design in PostgreSQL, and the generation of business insights through SQL queries and Python visualizations. The project follows data engineering best practices and is documented with a comprehensive IEEE-style report.

## **Key Features**
- **Data Ingestion**: Automated data retrieval from the [Fake Store API](https://fakestoreapi.com/).
- **Data Transformation**: Cleaning, normalizing, and structuring raw data into relational tables.
- **Data Warehousing**: Implementation of a star schema in PostgreSQL for efficient querying and analytics.
- **Insights Generation**: SQL queries and Python scripts to generate actionable business insights.
- **Documentation**: Detailed reports and documentation following professional standards.


## Project Structure
```
ECommerce-Sales-Warehouse/
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
├── reports/               # Generated reports and analysis
│   ├── images/            # Project images and visualizations
│   ├── final_report.pdf   # Comprehensive IEEE-style final report
└── └── stats_report.md    # Summary of findings and insights
```

## **ETL Pipeline Overview**

1. **Data Source**:  
   Data is retrieved from the [Fake Store API](https://fakestoreapi.com/), a publicly available API that simulates e-commerce data. The API provides various datasets:
   - **Products**: Product titles, categories, prices, ratings, and descriptions.
   - **Users**: Customer profiles, including names, contact details, and addresses.
   - **Carts**: Order history detailing user purchases and quantities.
   - **Categories**: Product classifications to group items effectively.

2. **Ingestion**:  
   The `ingestion.py` script automates data extraction from the API. Raw JSON data is saved in the `data/raw/` directory, preserving the original structure for reference and reproducibility.

3. **Transformation**:  
   The `transformation.py` script cleans and normalizes the ingested JSON data. Key transformations include:
   - Flattening nested JSON fields (e.g., product ratings).
   - Ensuring consistent data types for analytical readiness.
   - Generating processed CSV files stored in the `data/processed/` directory.

4. **Data Warehouse**:  
   The PostgreSQL database follows a **star schema** design, optimizing the data for analytical queries and OLAP operations.
   - **Fact Table**: `sales_fact_table` holds transactional data for all sales activities.
   - **Dimension Tables**: 
     - `user_dimension`: Customer details.
     - `product_dimension`: Product specifications.
     - `category_dimension`: Classification of products.
     - `cart_dimension`: Purchase event metadata.

   - **ERD Diagram**: [ERD.png](reports/images/ERD.png) provides a visual representation of the schema relationships.

5. **Insights Generation**:  
   Business insights are generated using SQL queries (`queries.sql`), and visualizations are created using Python in `stats.py`. The insights focus on sales performance, customer behavior, and category-specific trends.

## **Setup Instructions**
1. **Clone the repository**:
   ```bash
   git clone https://github.com/YourGitHubUsername/ECommerce-Sales-Warehouse
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure database and API details**:
    - Edit the `config/db_config.json` file with your PostgreSQL credentials.
    - Modify `config/api_config.json` if using different APIs.

4. **Run the ETL pipeline**:
    ```bash
    python scripts/ingestion.py
    python scripts/transformation.py
    python scripts/modeling.py
    ```
5. **Generate Insights**:
    ```bash
    python scripts/stats.py
    ```

## **Reports and Documentation**

- [**Final Report**](reports/Design_and_Implementation_of_an_ETL_Pipeline_and_Data_Warehouse_for_E-Commerce_Business_Insights.pdf): Comprehensive IEEE-style documentation detailing the project workflow, challenges, and insights.
- [**Business Insights**](reports/stats_report.md): Key findings and visualizations summarized.


## **Contributors**

- [**Walid K. W. Alsafadi**](https://github.com/WalidAlsafadi) 
- [**Ameer T. F. Alzerei**](https://github.com/AmeerAlzerei)
- [**Hamza M. H. Obaid**](https://github.com/hobaid1) 
- [**Hazem A. A. Muanes**](https://github.com/HazemMuannes)

## **License**
This project is licensed under the [Apache License 2.0](LICENSE).