import psycopg2
import csv
import os

# Database connection details
DB_DETAILS = {
    "dbname": "sales_dw",
    "user": "postgres",
    "password": "admin",
    "host": "localhost",
    "port": "5432"
}

# Define the path for the insights folder
BASE_DIR = os.getcwd()
INSIGHTS_FOLDER = os.path.join(BASE_DIR, "data", "insights")

# Ensure the insights folder exists
os.makedirs(INSIGHTS_FOLDER, exist_ok=True)

def connect_to_db():
    """
    Establish a connection to the PostgreSQL database.
    """
    try:
        conn = psycopg2.connect(**DB_DETAILS)
        print("Database connection successful.")
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def execute_query(conn, query):
    """
    Execute a SQL query and return the results.
    """
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
            return results
    except Exception as e:
        print(f"Error executing query: {e}")
        return None

def print_results(results, headers):
    """
    Display query results in a readable format.
    """
    print(f"\n{' | '.join(headers)}")
    print("-" * (len(headers) * 15))
    for row in results:
        print(" | ".join(map(str, row)))

def save_to_csv(results, headers, filename):
    """
    Save query results to a CSV file in the insights folder.
    """
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(results)
        print(f"Results saved to {filename}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def main():
    """
    Main function to generate insights from the data warehouse.
    """
    conn = connect_to_db()
    if not conn:
        return

    try:
        # Total revenue per category
        print("\nFetching total revenue per category...")
        revenue_query = """
        SELECT c.categories, SUM(p.price * cart.quantity) AS total_revenue
        FROM Carts cart
        JOIN Products p ON cart.productId = p.ProductsId
        JOIN Categories c ON p.CategoryId = c.CategoryId
        GROUP BY c.categories;
        """
        results = execute_query(conn, revenue_query)
        if results:
            headers = ["Category", "Total Revenue"]
            print_results(results, headers)
            save_to_csv(results, headers, os.path.join(INSIGHTS_FOLDER, "total_revenue_per_category.csv"))

        # Top 5 selling products
        print("\nFetching top 5 selling products...")
        top_products_query = """
        SELECT p.title, SUM(cart.quantity) AS total_sold
        FROM Carts cart
        JOIN Products p ON cart.productId = p.ProductsId
        GROUP BY p.title
        ORDER BY total_sold DESC
        LIMIT 5;
        """
        results = execute_query(conn, top_products_query)
        if results:
            headers = ["Product", "Total Sold"]
            print_results(results, headers)
            save_to_csv(results, headers, os.path.join(INSIGHTS_FOLDER, "top_5_selling_products.csv"))

        # Sales trends over time
        print("\nFetching sales trends over time...")
        sales_trends_query = """
        SELECT DATE_TRUNC('month', cart.date) AS sales_month, SUM(p.price * cart.quantity) AS total_revenue
        FROM Carts cart
        JOIN Products p ON cart.productId = p.ProductsId
        GROUP BY sales_month
        ORDER BY sales_month;
        """
        results = execute_query(conn, sales_trends_query)
        if results:
            headers = ["Sales Month", "Total Revenue"]
            print_results(results, headers)
            save_to_csv(results, headers, os.path.join(INSIGHTS_FOLDER, "sales_trends_over_time.csv"))

    finally:
        conn.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()