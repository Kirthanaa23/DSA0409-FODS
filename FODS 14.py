import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create sample dataset
sales_data = {
    'Cust_ID': [101, 102, 103, 104, 105, 106, 107],
    'Cust_Age': [21, 30, 21, 40, 35, 30, 25],
    'Amount_Spent': [140, 190, 170, 300, 260, 200, 150],
    'Date_of_Purchase': ['2025-06-02', '2025-06-05', '2025-06-08', '2025-06-12',
                         '2025-06-19', '2025-06-22', '2025-06-29']
}

# Step 2: Create DataFrame
df = pd.DataFrame(sales_data)

# Step 3: Convert to datetime
df['Date_of_Purchase'] = pd.to_datetime(df['Date_of_Purchase'])

# Step 4: Filter for a date range (June 2025)
june_df = df[(df['Date_of_Purchase'] >= '2025-06-01') & (df['Date_of_Purchase'] <= '2025-06-30')]

# Step 5: Calculate frequency distribution of customer ages
age_dist = june_df['Cust_Age'].value_counts().sort_index()

# Step 6: Display result
print("Frequency of Customer Ages in June 2025:\n")
print(age_dist)

# Step 7: Plot the distribution
plt.figure(figsize=(6, 4))
age_dist.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Customer Age Distribution (June 2025)')
plt.xlabel('Age')
plt.ylabel('Number of Customers')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
