import numpy as np

# Each row = product, each column = different sale prices
sales_data = np.array([
    [200, 180, 220],  # Product 1
    [150, 170, 160],  # Product 2
    [300, 310, 295]   # Product 3
])

# Calculate average of all prices
average_price = np.mean(sales_data)
print(f"Average price of all products sold: ${average_price:.2f}")
