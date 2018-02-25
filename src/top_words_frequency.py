from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from core.tweet_reader import TweetReader

reader = TweetReader('data/pos_neg/neg_comment.csv',  text_column='text', separator='\001', encoding='utf8')
freq = reader.extract_words_frequency(num_words=10, stop_word_file='input/stopwords.txt')

words_names=[]
words_count=[]
for (word, freq) in freq:
    words_names.append(word)
    words_count.append(freq)


# Plot histogram using matplotlib bar()
plt.xlabel('Top Words')
plt.ylabel('Frequency')
plt.title('Plotting Word Frequency')
indexes = np.arange(len(words_names) )
width = .4
plt.bar(indexes, words_count, width)
plt.xticks(indexes + width * .4, words_names)
#plt.legend()
plt.tight_layout()
plt.show()