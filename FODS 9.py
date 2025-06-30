import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create updated property dataset
property_df = pd.DataFrame({
    'property_id': [201, 202, 203, 204, 205],
    'location': ['Uptown', 'Midtown', 'Countryside', 'Uptown', 'Beachside'],
    'bedrooms': [3, 5, 2, 4, 6],
    'area_sqft': [1500, 2500, 1300, 2000, 3100],
    'listing_price': [300000, 450000, 210000, 370000, 600000]
})

# Step 2: Average price by location
location_avg_price = property_df.groupby('location')['listing_price'].mean()
print("1. Average Price by Location (₹):")
print(location_avg_price.apply(lambda x: f"₹{x:,.0f}"))

# Step 3: Count properties with more than 4 bedrooms
high_bedroom_count = property_df[property_df['bedrooms'] > 4].shape[0]
print(f"\n 2. Properties with More Than 4 Bedrooms: {high_bedroom_count}")

# Step 4: Find property with maximum area
max_area_row = property_df.loc[property_df['area_sqft'].idxmax()]
print("\n 3. Property with the Largest Area:")
print(max_area_row)

# Step 5: Visualize with horizontal bar chart
plt.figure(figsize=(7, 4))
location_avg_price.sort_values().plot(kind='barh', color='skyblue', edgecolor='black')
plt.title('Average Property Price by Location')
plt.xlabel('Average Listing Price (₹)')
plt.ylabel('Location')
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
