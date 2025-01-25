import psycopg2
import pandas as pd
import os

# Database connection details
DB_DETAILS = {
    "dbname": "sales_dw",
    "user": "postgres",
    "password": "admin",
    "host": "localhost",
    "port": "5432"
}

# Path to the SQL schema file
SCHEMA_FILE = "sql/dw_schema.sql"

# Paths to processed CSV files
BASE_DIR = os.getcwd()  # Project root directory
FILE_PATHS = {
    "categories": os.path.join(BASE_DIR, "data", "processed", "dimension_categories.csv"),
    "products": os.path.join(BASE_DIR, "data", "processed", "dimension_products.csv"),
    "carts": os.path.join(BASE_DIR, "data", "processed", "fact_carts.csv"),
    "users": os.path.join(BASE_DIR, "data", "processed", "dimension_users.csv"),
    "address": os.path.join(BASE_DIR, "data", "processed", "dimension_address.csv"),
}

def create_tables():
    """
    Connect to PostgreSQL and create tables using the SQL script from dw_schema.sql.
    """
    try:
        # Read the SQL script from the file
        with open(SCHEMA_FILE, "r") as file:
            create_tables_sql = file.read()

        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**DB_DETAILS)
        cursor = conn.cursor()

        # Execute the SQL script
        cursor.execute(create_tables_sql)
        conn.commit()
        print("Tables created successfully.")
    except Exception as e:
        print(f"Error creating tables: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            print("Connection closed.")

def load_csv_to_postgres(file_path, table_name, conn):
    """
    Load a CSV file into a PostgreSQL table.
    """
    print(f"Loading data into {table_name} from {file_path}...")
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Generate a list of tuples from the DataFrame
        data = list(df.itertuples(index=False, name=None))

        # Generate the INSERT statement dynamically
        columns = ", ".join(df.columns)
        placeholders = ", ".join(["%s"] * len(df.columns))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        # Execute the INSERT statement
        with conn.cursor() as cursor:
            cursor.executemany(query, data)
            conn.commit()
        print(f"Data loaded into {table_name} successfully.")
    except Exception as e:
        print(f"Error loading data into {table_name}: {e}")

def insert_data():
    """
    Validate files and load data into PostgreSQL tables.
    """
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(**DB_DETAILS)
        print("Database connection successful.")

        # Load data into each table
        load_csv_to_postgres(FILE_PATHS["categories"], "categories", conn)
        load_csv_to_postgres(FILE_PATHS["products"], "products", conn)
        load_csv_to_postgres(FILE_PATHS["address"], "address", conn)
        load_csv_to_postgres(FILE_PATHS["users"], "users", conn)
        load_csv_to_postgres(FILE_PATHS["carts"], "carts", conn)

    except Exception as e:
        print(f"Error inserting data: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            print("Connection closed.")

if __name__ == "__main__":
    print("Creating tables...")
    create_tables()

    print("\nInserting data into tables...")
    insert_data()