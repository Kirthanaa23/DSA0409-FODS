import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\balaj\OneDrive\Documents\monthly_weather_data.csv")
data.columns = data.columns.str.strip()

months = data['Month']
temp = data['Temperature(C)']
rain = data['Rainfall(mm)']

plt.plot(months, temp, label='Temp', marker='o')
plt.plot(months, rain, label='Rain', marker='s')
plt.title('Line Plot')
plt.legend()
plt.show()

plt.scatter(months, temp, color='red', label='Temp')
plt.scatter(months, rain, color='blue', label='Rain')
plt.title('Scatter Plot')
plt.legend()
plt.show()

plt.bar(months, temp, color='orange', label='Temp')
plt.bar(months, rain, color='lightblue', alpha=0.6, label='Rain')
plt.title('Bar Plot')
plt.xlabel('Month')
plt.ylabel('Values')
plt.legend()
plt.show()
