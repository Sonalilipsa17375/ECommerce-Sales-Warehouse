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

# Resolve paths dynamically based on the current working directory
BASE_DIR = os.getcwd()  # Project root directory
FILE_PATHS = {
    "categories": os.path.join(BASE_DIR, "data", "processed", "dimension_categories.csv"),
    "products": os.path.join(BASE_DIR, "data", "processed", "dimension_products.csv"),
    "carts": os.path.join(BASE_DIR, "data", "processed", "fact_carts.csv"),
    "users": os.path.join(BASE_DIR, "data", "processed", "dimension_users.csv"),
    "address": os.path.join(BASE_DIR, "data", "processed", "dimension_address.csv"),
}

def check_files_exist():
    """
    Check if all required files exist.
    """
    for table, path in FILE_PATHS.items():
        print(f"Checking {table} file at: {path}")
        if not os.path.exists(path):
            print(f"ERROR: File not found for {table}: {path}")
            return False
        else:
            print(f"File found for {table}: {path}")
    return True

def load_csv_to_postgres(file_path, table_name, conn):
    """
    Load a CSV file into a PostgreSQL table.
    """
    print(f"Loading data into {table_name} from {file_path}...")
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

def main():
    """
    Main function to validate files and load data into PostgreSQL.
    """
    # Validate file paths
    if not check_files_exist():
        print("File validation failed. Exiting...")
        return

    # Connect to the PostgreSQL database
    try:
        conn = psycopg2.connect(**DB_DETAILS)
        print("Database connection successful.")

        # Load data into each table
        load_csv_to_postgres(FILE_PATHS["categories"], "Categories", conn)
        load_csv_to_postgres(FILE_PATHS["products"], "Products", conn)
        load_csv_to_postgres(FILE_PATHS["address"], "Address", conn)
        load_csv_to_postgres(FILE_PATHS["users"], "Users", conn)
        load_csv_to_postgres(FILE_PATHS["carts"], "Carts", conn)

    except Exception as e:
        print(f"Database error: {e}")
    finally:
        conn.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()