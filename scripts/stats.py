import psycopg2
import json
import pandas as pd

# Database connection configuration
CONFIG_FILE = "config/db_config.json"
# Load database configuration
def load_db_config():
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"ERROR: Config file {CONFIG_FILE} not found.")
        exit(1)

DB_CONFIG = load_db_config()

# SQL Queries
queries = {
    "Top 5 Products by Revenue": """
        SELECT 
            p.product_name,
            p.description,
            SUM(s.product_total_price) AS total_revenue
        FROM 
            sales_fact_table s
        JOIN 
            product_dimension p ON s.product_id = p.product_id
        GROUP BY 
            p.product_name, p.description
        ORDER BY 
            total_revenue DESC
        LIMIT 5;
    """,
    "Top Customers by Spending": """
        SELECT 
            u.first_name || ' ' || u.last_name AS customer_name,
            u.email,
            SUM(s.total_cart_price) AS total_spent
        FROM 
            sales_fact_table s
        JOIN 
            user_dimension u ON s.user_id = u.user_id
        GROUP BY 
            u.first_name, u.last_name, u.email
        ORDER BY 
            total_spent DESC;
    """,
    "Revenue by Category": """
        SELECT 
            c.category_name,
            SUM(s.product_total_price) AS total_revenue
        FROM 
            sales_fact_table s
        JOIN 
            category_dimension c ON s.category_id = c.category_id
        GROUP BY 
            c.category_name
        ORDER BY 
            total_revenue DESC;
    """
}

# Execute Queries and Display Results
def run_queries():
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        for title, query in queries.items():
            print(f"\n Running Query: {title}")
            cur.execute(query)
            rows = cur.fetchall()
            
            # Convert to Pandas DataFrame for better display
            colnames = [desc[0] for desc in cur.description]
            df = pd.DataFrame(rows, columns=colnames)
            print(df)

        cur.close()
        conn.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_queries()
