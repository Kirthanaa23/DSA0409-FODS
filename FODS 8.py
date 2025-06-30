import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Updated sales dataset with different values
sales_data = {
    'sale_date': ['2025-06-02', '2025-06-04', '2025-06-06', '2025-06-09', '2025-06-11',
                  '2025-06-14', '2025-06-17', '2025-06-21', '2025-06-24', '2025-06-28'],
    'item_name': ['Tablet', 'Mousepad', 'Tablet', 'Keyboard', 'Mousepad',
                  'Webcam', 'Tablet', 'Keyboard', 'Webcam', 'Mousepad'],
    'units_sold': [1, 6, 2, 4, 3, 5, 1, 3, 2, 7]
}

# Step 2: Create DataFrame
df = pd.DataFrame(sales_data)

# Step 3: Convert sale_date to datetime format
df['sale_date'] = pd.to_datetime(df['sale_date'])

# Step 4: Filter records from the past 30 days
cutoff_date = pd.Timestamp.today() - pd.Timedelta(days=30)
filtered_df = df[df['sale_date'] >= cutoff_date]

# Step 5: Group by item and sum the sales
sales_summary = filtered_df.groupby('item_name')['units_sold'].sum()

# Step 6: Identify top 5 selling products
top_products = sales_summary.sort_values(ascending=False).head(5)

# Step 7: Print result
print("Top 5 Items Sold in the Last 30 Days:")
print(top_products)

# Step 8: Plot the result
plt.figure(figsize=(7, 4))
top_products.plot(kind='barh', color='mediumseagreen', edgecolor='black')
plt.title("Top 5 Selling Items - Last 30 Days")
plt.xlabel("Units Sold")
plt.ylabel("Item Name")
plt.tight_layout()
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.show()
