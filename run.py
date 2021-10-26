import find_words as fw
import os

# Read text files
path = (os.getcwd() +
        r"\large_texts.txt\eng_news_100K-sentences.txt")

print(path)
rows = fw.read_rows(path)
print(f"\nRead {len(rows)} lines from file {path}")

# Collect words
words = fw.get_words(rows, 4)

# Get a dictonary from words
print("Getting dictionary:")
dct_words = fw.count_occurrences(words)

# Find 10 most common numbers
fw.most_common(dct_words, 10)
