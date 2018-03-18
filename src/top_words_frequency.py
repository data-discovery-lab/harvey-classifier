from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from core.tweet_reader import TweetReader

reader = TweetReader('/home/long/TTU-SOURCES/ttu-texas-water/data/tweets/twdb_monthly/2017-01.csv',  text_column='text', separator='\001', encoding='utf8')
wfreq = reader.extract_words_frequency(num_words=20, stop_word_file='input/stopwords.txt', ordered='asc')

words_names = []
words_count = []
for (word, freq) in wfreq:
    words_names.append(word)
    words_count.append(freq)

print(wfreq)

show_plot = False

if show_plot == True:
    #
    fig, ax = plt.subplots()
    width = 0.56 # the width of the bars
    ind = np.arange(len(words_count))  # the x locations for the groups
    ax.barh(ind, words_count, width, color="blue")
    ax.set_yticks(ind+width/2)
    ax.set_yticklabels(words_names, minor=False)
    plt.title('Word Frequency')
    plt.xlabel('Frequencies')
    plt.ylabel('Words')
    for i, v in enumerate(words_count):
        ax.text(v + 0.2, i - .15, str(v), color='blue', fontweight='bold')
    plt.show()

