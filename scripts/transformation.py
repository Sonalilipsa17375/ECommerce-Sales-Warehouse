import os
import json
import pandas as pd

# Define directories
raw_data_path = "data/raw"
processed_data_path = "data/processed"

# Ensure the processed directory exists
os.makedirs(processed_data_path, exist_ok=True)

# Load JSON files
with open(os.path.join(raw_data_path, "categories.json")) as f:
    categories = json.load(f)

with open(os.path.join(raw_data_path, "products.json")) as f:
    products = json.load(f)

with open(os.path.join(raw_data_path, "users.json")) as f:
    users = json.load(f)

with open(os.path.join(raw_data_path, "carts.json")) as f:
    carts = json.load(f)

# 1. Category Dimension
category_dimension = pd.DataFrame({
    "category_id": range(1, len(categories) + 1),
    "category_name": categories
})
category_mapping = dict(zip(categories, range(1, len(categories) + 1)))

# Save to CSV
category_dimension.to_csv(os.path.join(processed_data_path, "category_dimension.csv"), index=False)

# 2. Product Dimension
product_dimension = pd.DataFrame(products)
product_dimension = product_dimension.rename(columns={
    "id": "product_id",
    "title": "product_name",
    "price": "price",
    "description": "description",
    "image": "image_url"
})[["product_id", "price", "product_name", "description", "image_url"]]

# Save to CSV
product_dimension.to_csv(os.path.join(processed_data_path, "product_dimension.csv"), index=False)

# 3. User Dimension
user_dimension = pd.DataFrame(users)
user_dimension = user_dimension.rename(columns={
    "id": "user_id",
    "email": "email",
    "username": "username",
    "phone": "phone_num"
})

user_dimension["first_name"] = user_dimension["name"].apply(lambda x: x["firstname"])
user_dimension["last_name"] = user_dimension["name"].apply(lambda x: x["lastname"])
user_dimension["street"] = user_dimension["address"].apply(lambda x: x["street"])
user_dimension["city"] = user_dimension["address"].apply(lambda x: x["city"])
user_dimension["zip_code"] = user_dimension["address"].apply(lambda x: x["zipcode"])
user_dimension["long"] = user_dimension["address"].apply(lambda x: x["geolocation"]["long"])
user_dimension["lat"] = user_dimension["address"].apply(lambda x: x["geolocation"]["lat"])

user_dimension = user_dimension[[
    "user_id", "email", "username", "first_name", "last_name", "phone_num",
    "street", "city", "zip_code", "long", "lat"
]]

# Save to CSV
user_dimension.to_csv(os.path.join(processed_data_path, "user_dimension.csv"), index=False)

# 4. Cart Dimension
cart_dimension = pd.DataFrame(carts)
cart_dimension = cart_dimension.rename(columns={"id": "cart_id", "date": "cart_date"})[["cart_id", "cart_date"]]

# Save to CSV
cart_dimension.to_csv(os.path.join(processed_data_path, "cart_dimension.csv"), index=False)

# 5. Sales Fact Table
sales_fact_table = []
cart_prices = {}
cart_items = {}

for cart in carts:
    cart_id = cart["id"]
    user_id = cart["userId"]
    cart_total_price = 0
    distinct_products_in_cart = len(cart["products"])
    for product in cart["products"]:
        product_id = product["productId"]
        quantity = product["quantity"]
        price = product_dimension.loc[product_dimension["product_id"] == product_id, "price"].values[0]
        product_total_price = price * quantity
        
        rating_count = products[product_id - 1]["rating"]["count"]
        rating_rate = products[product_id - 1]["rating"]["rate"]
        
        sales_fact_table.append({
            "sales_id": len(sales_fact_table) + 1,
            "product_id": product_id,
            "category_id": category_mapping[products[product_id - 1]["category"]],
            "cart_id": cart_id,
            "user_id": user_id,
            "quantity_purchased": quantity,
            "product_total_price": product_total_price,
            "rating_count": rating_count,
            "rating_rate": rating_rate,
            "total_cart_price": None,  # Placeholder
            "distinct_products_in_cart": None  # Placeholder
        })
    
    cart_prices[cart_id] = cart_total_price
    cart_items[cart_id] = distinct_products_in_cart

# Add cart-level data to sales fact table
for row in sales_fact_table:
    row["total_cart_price"] = cart_prices[row["cart_id"]]
    row["distinct_products_in_cart"] = cart_items[row["cart_id"]]

sales_fact_table = pd.DataFrame(sales_fact_table)

# Save to CSV
sales_fact_table.to_csv(os.path.join(processed_data_path, "sales_fact_table.csv"), index=False)

print("Data transformation complete. Files saved to 'data/processed'.")
