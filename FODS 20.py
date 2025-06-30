import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Customer ID': [101, 102, 103, 104, 105, 106],
    'Age': [25, 32, 45, 29, 38, 50],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Female', 'Male'],
    'Total Spending': [3000, 8000, 17000, 9000, 20000, 16000]
}

df = pd.DataFrame(data)

def segment(spending):
    if spending >= 15000:
        return 'High Spender'
    elif spending >= 7000:
        return 'Medium Spender'
    else:
        return 'Low Spender'

df['Segment'] = df['Total Spending'].apply(segment)

avg_age = df.groupby('Segment')['Age'].mean().round(1)
print("Average Age per Segment:\n")
print(avg_age)

counts = df['Segment'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(counts, labels=counts.index, autopct='%1.1f%%',
        colors=['lightcoral', 'gold', 'skyblue'])
plt.title("Customer Segmentation Pie Chart")
plt.show()
