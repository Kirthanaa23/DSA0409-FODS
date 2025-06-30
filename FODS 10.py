import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Updated sales data with abbreviations and new values
monthly_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales': [10000, 12500, 11800, 13200, 14500, 13800,
              14200, 15500, 14800, 16000, 16200, 17500]
}

# Step 2: Create DataFrame
df = pd.DataFrame(monthly_data)

# Step 3: Line chart for sales trend
plt.figure(figsize=(9, 4))
plt.plot(df['Month'], df['Sales'], marker='s', linestyle='--', color='darkorange', linewidth=2)
plt.title("Sales Trend Over the Year")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Step 4: Bar chart for monthly sales comparison
plt.figure(figsize=(9, 5))
bars = plt.bar(df['Month'], df['Sales'], color='steelblue', edgecolor='black')

# Add data labels on top of bars
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 200,
             f"{bar.get_height()}", ha='center', va='bottom', fontsize=8)

plt.title("Monthly Sales Overview")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.tight_layout()
plt.show()
