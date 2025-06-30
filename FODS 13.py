import string
from collections import Counter
import matplotlib.pyplot as plt

# Step 1: Read text from file
try:
    with open('sample_text.txt', 'r', encoding='utf-8') as f:
        raw_text = f.read()
except FileNotFoundError:
    print("File not found. Make sure 'sample_text.txt' is in the correct directory.")
    exit()

# Step 2: Clean the text
clean_text = raw_text.lower().translate(str.maketrans('', '', string.punctuation))

# Step 3: Tokenize words
words_list = clean_text.split()

# Step 4: Count word occurrences
freq_counter = Counter(words_list)

# Step 5: Display top 10 words
top_words = freq_counter.most_common(10)
print("Top 10 Frequent Words:")
for word, count in top_words:
    print(f"{word}: {count}")

# Step 6: Plot the results
labels, values = zip(*top_words)

plt.figure(figsize=(9, 5))
bars = plt.bar(labels, values, color='mediumseagreen', edgecolor='black')

# Add data labels
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             str(bar.get_height()), ha='center', fontsize=9)

plt.title("Top 10 Word Frequencies", fontsize=14)
plt.xlabel("Words")
plt.ylabel("Count")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
