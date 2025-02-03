import os
import pandas as pd
import psycopg2
from psycopg2 import sql

# Database connection configuration
DB_CONFIG = {
    "dbname": "sales_analytics",
    "user": "postgres",
    "password": "123123", # This password is exclusive to the local machine used to run the script
    "host": "localhost",
    "port": 5432
}

# Paths to processed CSV files
PROCESSED_DATA_PATH = "data/processed"

# List of tables and their corresponding CSV files
TABLES = {
    "category_dimension": "category_dimension.csv",
    "product_dimension": "product_dimension.csv",
    "user_dimension": "user_dimension.csv",
    "cart_dimension": "cart_dimension.csv",
    "sales_fact_table": "sales_fact_table.csv"
}

# Function to establish a database connection
def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)

# Function to check if a table exists
def table_exists(table_name):
    query = sql.SQL(
        "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = %s);"
    )
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (table_name,))
            return cur.fetchone()[0]  # Extract boolean result

# Function to load CSV data into PostgreSQL
def load_csv_to_postgres(table_name, csv_filename):
    csv_path = os.path.join(PROCESSED_DATA_PATH, csv_filename)

    if not os.path.exists(csv_path):
        print(f"ERROR: File {csv_path} not found.")
        return

    df = pd.read_csv(csv_path)
    print(f"Preview of {table_name}:\n", df.head())

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            if table_exists(table_name):
                print(f"Table {table_name} exists. Updating data...")

                # Load existing data from database
                cur.execute(sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name)))
                existing_data = pd.DataFrame(cur.fetchall(), columns=[desc[0] for desc in cur.description])

                # Merge: Update or Append new records
                updated_data = pd.concat([existing_data, df]).drop_duplicates()

                # Drop and recreate the table
                cur.execute(sql.SQL("DROP TABLE {}").format(sql.Identifier(table_name)))

            else:
                print(f"Table {table_name} does not exist. Creating and inserting data...")

            # Creating table dynamically based on DataFrame
            create_table_query = f"CREATE TABLE {table_name} ({', '.join([f'{col} TEXT' for col in df.columns])});"
            cur.execute(create_table_query)

            # Insert data using COPY (faster than INSERT)
            with open(csv_path, 'r') as f:
                next(f)  # Skip header row
                cur.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV HEADER", f)

        conn.commit()
        print(f"{table_name} successfully loaded.")

# Function to load all tables
def load_all_data():
    for table_name, csv_filename in TABLES.items():
        load_csv_to_postgres(table_name, csv_filename)

# Main function
def main():
    print("Starting database load process...")
    load_all_data()  # Load all tables
    print("All CSVs successfully loaded into PostgreSQL.")

if __name__ == "__main__":
    main()