import pandas as pd
import os
import json

# Create directories for processed data
os.makedirs("data/processed", exist_ok=True)

# Function to load JSON data
def load_json(filepath):
    with open(filepath, "r") as file:
        return json.load(file)

# Function to convert data to CSV
def convert_to_csv(data, filename):
    if isinstance(data, list) and isinstance(data[0], str):
        # Handle list of strings
        df = pd.DataFrame(data, columns=[f"{filename}"])
    else:
        # Handle general case
        df = pd.DataFrame(data)
    filepath = f"data/processed/{filename}.csv"
    df.to_csv(filepath, index=False)
    print(f"Data converted to CSV and saved to {filepath}")


# Process products
products_data = load_json("data/raw/products.json")
convert_to_csv(products_data, "products")

# Process users
users_data = load_json("data/raw/users.json")
convert_to_csv(users_data, "users")

# Process carts
carts_data = load_json("data/raw/carts.json")
convert_to_csv(carts_data, "carts")

# Process categories
categories_data = load_json("data/raw/categories.json")
convert_to_csv(categories_data, "categories")