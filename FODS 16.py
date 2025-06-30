import matplotlib.pyplot as plt
from collections import Counter
import re

reviews = [
    "Great product! Loved it.",
    "Not what I expected. Quality is poor.",
    "Excellent quality and fast delivery.",
    "Terrible product. Would not recommend!",
    "Loved it! Will buy again.",
    "Okay product, but delivery was late."
]

text = ' '.join(reviews).lower()
text = re.sub(r'[^a-z\s]', '', text)  # remove punctuation

stopwords = {'is', 'it', 'but', 'not', 'and', 'the', 'i', 'was', 'what'}
words = [word for word in text.split() if word not in stopwords]

counts = Counter(words)
top = counts.most_common(5)
labels, values = zip(*top)

plt.bar(labels, values, color='darkblue')
plt.title("Top 5 Frequent Words")
plt.ylabel("Count")
plt.show()

positive = {'great', 'loved', 'excellent', 'fast', 'recommend'}
negative = {'poor', 'terrible', 'late'}

pos = sum(counts.get(w, 0) for w in positive)
neg = sum(counts.get(w, 0) for w in negative)

if pos + neg > 0:
    plt.pie([pos, neg], labels=['Positive', 'Negative'], colors=['lightgreen', 'red'], autopct='%1.1f%%')
    plt.title("Positive & Negative REVIEWS")
    plt.show()
