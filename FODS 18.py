import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

data = {
    'Age': [25, 48, 30, 53, 27, 40, 35, 44, 39, 38, 29, 49, 50, 34, 41, 33, 43, 36],
    'FatPercent': [19.0, 26.5, 21.4, 30.2, 18.7, 23.5, 20.3, 25.0, 24.1, 23.8, 19.5, 28.0, 27.3, 21.1, 24.0, 20.0, 25.7, 22.4]
}

df = pd.DataFrame(data)

print("Age Statistics")
print("Mean:", round(df['Age'].mean(), 2))
print("Median:", round(df['Age'].median(), 2))
print("Std Dev:", round(df['Age'].std(), 2))

print("\nBody Fat % Statistics")
print("Mean:", round(df['FatPercent'].mean(), 2))
print("Median:", round(df['FatPercent'].median(), 2))
print("Std Dev:", round(df['FatPercent'].std(), 2))

print("\nPearson Correlation (Age vs Fat%):", round(df['Age'].corr(df['FatPercent']), 2))

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
sns.histplot(df['Age'], bins=6, kde=True, color='teal')
plt.title("Age Distribution")

plt.subplot(1, 2, 2)
sns.histplot(df['FatPercent'], bins=6, kde=True, color='coral')
plt.title("Body Fat % Distribution")
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(x=df['Age'], color='lightgreen')
plt.title("Boxplot - Age")
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(x=df['FatPercent'], color='lightpink')
plt.title("Boxplot - Body Fat %")
plt.show()

plt.figure(figsize=(6, 4))
sns.regplot(x='Age', y='FatPercent', data=df, color='darkblue')
plt.title("Age vs Body Fat % (with Trend Line)")
plt.show()

plt.figure(figsize=(6, 4))
stats.probplot(df['Age'], dist="norm", plot=plt)
plt.title("Q-Q Plot - Age")
plt.grid(True)
plt.show()

plt.figure(figsize=(6, 4))
stats.probplot(df['FatPercent'], dist="norm", plot=plt)
plt.title("Q-Q Plot - Body Fat %")
plt.grid(True)
plt.show()
