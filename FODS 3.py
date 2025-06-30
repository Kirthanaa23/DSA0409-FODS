import numpy as np

# Columns: [Bedrooms, SquareFootage, SalePrice]
house_data = np.array([
    [4, 1500, 300000],
    [5, 2400, 500000],
    [6, 3200, 650000],
    [3, 1300, 250000],
    [7, 3500, 720000],
    [5, 2200, 480000]
])

# Filter houses with more than 4 bedrooms
filtered_houses = house_data[house_data[:, 0] > 4]

# Calculate average sale price of those houses
average_price = np.mean(filtered_houses[:, 2])
print(f"Average sale price of houses with >4 bedrooms: ${average_price:.2f}")
