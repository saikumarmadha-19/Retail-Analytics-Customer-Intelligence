import pandas as pd
import os

# Set the path to your data folder
data_path = 'data/'

# 1. Load the most important datasets
orders = pd.read_csv(os.path.join(data_path, 'olist_orders_dataset.csv'))
items = pd.read_csv(os.path.join(data_path, 'olist_order_items_dataset.csv'))
customers = pd.read_csv(os.path.join(data_path, 'olist_customers_dataset.csv'))

# 2. Start Merging
# Merge orders with items (gives us price and product_id for each order)
master_df = pd.merge(orders, items, on='order_id', how='inner')

# Merge with customers (gives us the city/state of the buyer)
master_df = pd.merge(master_df, customers, on='customer_id', how='inner')

# 3. Quick Check
print(f"Dataset Loaded! Total rows: {len(master_df)}")
print(master_df.info())

# Save this master file for later use in Power BI or ML
master_df.to_csv('cleaned_master_data.csv', index=False)