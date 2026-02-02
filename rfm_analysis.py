import pandas as pd
from datetime import timedelta

# 1. Load the cleaned data we created in the last step
df = pd.read_csv('cleaned_master_data.csv')

# 2. Convert date strings to actual Python datetime objects
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# 3. Set a 'Snapshot Date' (Since this is old data, we pretend 'today' is one day after the last order)
snapshot_date = df['order_purchase_timestamp'].max() + timedelta(days=1)

# 4. Group by Customer and calculate R, F, and M
rfm = df.groupby('customer_unique_id').agg({
    'order_purchase_timestamp': lambda x: (snapshot_date - x.max()).days, # Recency
    'order_id': 'nunique',                                              # Frequency
    'price': 'sum'                                                       # Monetary
})

# 5. Rename columns for clarity
rfm.rename(columns={
    'order_purchase_timestamp': 'Recency',
    'order_id': 'Frequency',
    'price': 'Monetary'
}, inplace=True)

print("RFM Table Created Successfully!")
print(rfm.head())

# Save this for Power BI
rfm.to_csv('customer_rfm_segments.csv')