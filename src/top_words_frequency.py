from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import string


# # Read CSV file, get author names and counts.
# df = pd.read_csv("books.csv", index_col="id")
# counter = Counter(df['author'])
# author_names = counter.keys()
# author_counts = counter.values()
#
# # Plot histogram using matplotlib bar().
# indexes = np.arange(len(author_names))
# width = 0.7
# plt.bar(indexes, author_counts, width)
# plt.xticks(indexes + width * 0.5, author_names)
# plt.show()




freq={}
read_text=open('WordCount.txt','r')
final_text=read_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', final_text)
match_pattern[:3]

for word in match_pattern:
    count = freq.get(word, 0)
    freq[word]=count + 1

frequency_list = freq.keys()

results = []
for word in frequency_list:
    tuple = (word, freq[word])
    results.append(tuple)

byFreq = sorted(results, key=lambda word: word[1], reverse=True)

words_names=[]
words_count=[]
for (word, freq) in byFreq[:10]:
    print (word, freq)
    words_names.append(word)
    words_count.append(freq)


# Plot histogram using matplotlib bar()
plt.xlabel('Top 10 Words')
plt.ylabel('Frequency')
plt.title('Plotting Word Frequency')
indexes = np.arange(len(words_names) )
width = .4
plt.bar(indexes, words_count, width)
plt.xticks(indexes + width * .4, words_names)
#plt.legend()
plt.tight_layout()
plt.show()