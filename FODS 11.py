import matplotlib.pyplot as plt

# Updated data
months = ['May', 'Jun', 'Jul', 'Aug']
sales = [130, 170, 110, 190]

# Create a 2x2 grid of subplots
plt.figure(figsize=(10, 6))

# Line Plot
plt.subplot(2, 2, 1)
plt.plot(months, sales, marker='s', linestyle='-', color='green', linewidth=2)
plt.title('Line Plot')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)

# Scatter Plot
plt.subplot(2, 2, 2)
plt.scatter(months, sales, color='purple', s=80)
plt.title(' Scatter Plot')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)

# Bar Plot
plt.subplot(2, 2, 3)
plt.bar(months, sales, color='teal', edgecolor='black')
plt.title('Bar Plot')
plt.xlabel('Month')
plt.ylabel('Sales')

# Pie Chart
plt.subplot(2, 2, 4)
explode = [0.05 if s == max(sales) else 0 for s in sales]  # highlight max
plt.pie(sales, labels=months, autopct='%1.1f%%', explode=explode,
        startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title('Pie Chart')

# Layout
plt.tight_layout()
plt.show()
