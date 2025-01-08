import requests
import json
import os
import pandas as pd

# Create directories for raw data
os.makedirs("data/raw", exist_ok=True)

# Function to fetch data from the API and save to a JSON file
def fetch_and_save(endpoint, filename):
    url = f"https://fakestoreapi.com/{endpoint}"
    print(f"Fetching data from {url}...")
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        filepath = f"data/raw/{filename}.json"
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {filepath}")
        return data
    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
        return None

# Fetch and save data from all endpoints
products = fetch_and_save("products", "products")
categories = fetch_and_save("products/categories", "categories")
users = fetch_and_save("users", "users")
carts = fetch_and_save("carts", "carts")

# Optionally convert data to CSV files
def save_to_csv(data, filename):
    if data:
        df = pd.DataFrame(data)
        filepath = f"data/raw/{filename}.csv"
        df.to_csv(filepath, index=False)
        print(f"Data converted to CSV and saved to {filepath}")

# Convert JSON to CSV for better readability
save_to_csv(products, "products")
save_to_csv(users, "users")
save_to_csv(carts, "carts")

# Categories are a simple list, convert manually
if categories:
    categories_df = pd.DataFrame(categories, columns=["category"])
    categories_df.to_csv("data/raw/categories.csv", index=False)
    print("Categories data converted to CSV.")