import pandas as pd
import matplotlib.pyplot as plt
import string
from collections import Counter

stop_words = {
    'the', 'and', 'is', 'in', 'to', 'it', 'of', 'for', 'on', 'this', 'that', 'a',
    'an', 'with', 'as', 'was', 'but', 'are', 'at', 'by', 'be', 'or', 'from', 'has',
    'have', 'had', 'you', 'we', 'they', 'not', 'so', 'if', 'about', 'can', 'just',
    'do', 'out', 'my', 'your', 'our', 'more', 'too'
}

def clean_text(text):
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return [word for word in words if word.isalpha() and word not in stop_words]

def analyze_feedback(filename, top_n=10):
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        print("File not found:", filename)
        return

    if 'feedback' not in df.columns:
        print("'feedback' column missing in the CSV.")
        return

    all_words = []
    for entry in df['feedback'].dropna():
        all_words.extend(clean_text(str(entry)))

    word_count = Counter(all_words)
    top_words = word_count.most_common(top_n)

    if not top_words:
        print("No valid words found in the feedback.")
        return

    print(f"\nTop {top_n} Frequent Words in Feedback:\n")
    for word, count in top_words:
        print(f"{word}: {count}")

    words, counts = zip(*top_words)
    plt.figure(figsize=(9, 5))
    bars = plt.bar(words, counts, color='lightcoral', edgecolor='black')

    for bar in bars:
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                 str(bar.get_height()), ha='center', fontsize=9)

    plt.title(f"Top {top_n} Word Frequencies in Feedback")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.4)
    plt.show()

if __name__ == "__main__":
    analyze_feedback("data.csv", top_n=10)
