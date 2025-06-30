import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create new sample dataset
data = pd.DataFrame({
    'customer_id': ['A101', 'A102', 'A103', 'A101', 'A104', 'A102', 'A105', 'A105', 'A106', 'A104'],
    'order_date': ['2024-06-01', '2024-06-02', '2024-06-03', '2024-06-04', '2024-06-05',
                   '2024-06-06', '2024-06-07', '2024-06-08', '2024-06-09', '2024-06-10'],
    'product_name': ['Monitor', 'Keyboard', 'Mouse', 'Monitor', 'Laptop',
                     'Mouse', 'Laptop', 'Keyboard', 'Mouse', 'Monitor'],
    'order_quantity': [1, 2, 3, 1, 1, 2, 1, 2, 3, 1],
    'unit_price': [150, 40, 20, 150, 700, 20, 700, 40, 20, 150]
})

# Step 2: Save and Read CSV
data.to_csv('new_order_data.csv', index=False)
df = pd.read_csv('new_order_data.csv')
df['order_date'] = pd.to_datetime(df['order_date'])

# Step 3: Analysis

# Total orders per customer
order_counts = df['customer_id'].value_counts()

# Total sales per product
df['total_price'] = df['order_quantity'] * df['unit_price']
sales_per_product = df.groupby('product_name')['total_price'].sum()

# Earliest and latest order date
start_date = df['order_date'].min()
end_date = df['order_date'].max()

# Display outputs
print("Order count per customer:\n", order_counts)
print("\nTotal sales per product:\n", sales_per_product)
print(f"\nOrder period: {start_date.date()} to {end_date.date()}")

# Step 4: Visualizations

# Total orders per customer
plt.figure(figsize=(6, 4))
order_counts.plot(kind='bar', color='lightgreen')
plt.title("Number of Orders per Customer")
plt.xlabel("Customer ID")
plt.ylabel("Orders")
plt.tight_layout()
plt.show()

# Total sales per product
plt.figure(figsize=(6, 4))
sales_per_product.plot(kind='bar', color='coral')
plt.title("Total Sales per Product")
plt.xlabel("Product")
plt.ylabel("Sales ($)")
plt.tight_layout()
plt.show()
