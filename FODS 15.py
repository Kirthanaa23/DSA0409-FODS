import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Username': ['anu', 'bobby', 'caroline', 'dev', 'emily', 'francis'],
    'Likes':    [12, 25, 12, 40, 25, 18],
    'Shares':   [3, 7, 3, 5, 6, 2]
}

df = pd.DataFrame(data)
df['Total Engagement'] = df['Likes'] + df['Shares']

like_counts = df['Likes'].value_counts()

print("Frequency of Likes:")
for like, count in like_counts.items():
    print(f"{like} likes → {count} user(s)")

print("\nTotal Users:", len(df))
print("Most Liked Post:", df.loc[df['Likes'].idxmax(), 'Username'], "→", df['Likes'].max(), "likes")
print("Most Shared Post:", df.loc[df['Shares'].idxmax(), 'Username'], "→", df['Shares'].max(), "shares")


plt.figure(figsize=(6, 6))
plt.pie(df['Shares'], labels=df['Username'], autopct='%1.1f%%',
        colors=['lightcoral', 'gold', 'skyblue', 'lightgreen', 'violet', 'orange'])
plt.title("Share Contribution by User")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
bar_width = 0.35
x = range(len(df))

plt.bar(x, df['Likes'], width=bar_width, label='Likes', color='skyblue')
plt.bar([i + bar_width for i in x], df['Shares'], width=bar_width, label='Shares', color='lightgreen')

plt.xticks([i + bar_width / 2 for i in x], df['Username'])
plt.title("Likes and Shares per User")
plt.xlabel("Username")
plt.ylabel("Count")
plt.legend()
plt.tight_layout()
plt.show()

print("Total Users:", len(df))
print("Most Liked Post:", df.loc[df['Likes'].idxmax(), 'Username'], "→", df['Likes'].max(), "likes")
print("Most Shared Post:", df.loc[df['Shares'].idxmax(), 'Username'], "→", df['Shares'].max(), "shares")
