import pandas as pd
from core.tweet_cleaner import TweetCleaner
import csv

class TweetReader:
    def __init__(self, tweet_file, text_column='tweet', separator=',', encoding='latin1', header=None):
        self.tweets_df = pd.read_csv(tweet_file, encoding=encoding, sep=separator, header=header, usecols=[text_column])
        all_tweets = self.tweets_df[text_column]
        self.corpus = []
        for tweet in all_tweets:
            self.corpus.append(tweet)


        # with open(tweet_file, 'r') as csvfile:
        #     reader = csv.DictReader(csvfile)
        #     self.corpus = []
        #     for tweet in reader:
        #         self.corpus.append(tweet[text_column])

    def get_corpus(self):
        return self.corpus

    # def get_tweets_df(self):
    #     return self.tweets_df

    def get_total_tweets(self):
        return len(self.get_corpus())

    def extract_words_frequency(self, num_words=None, stop_word_file='', ordered='desc'):
        my_clean_tweets = []

        if len(stop_word_file) > 0:
            my_clean_tweets = TweetCleaner.clean_text_data(self.corpus, stop_word_file)

        freq = {}

        for tweet in my_clean_tweets:
            for word in tweet:
                count = freq.get(word, 0)
                freq[word] = count + 1

        frequency_list = freq.keys()
        results = []
        for word in frequency_list:
            tuple = (word, freq[word])
            results.append(tuple)

        byFreq = sorted(results, key=lambda word: word[1], reverse=True)

        if num_words is not None:
            byFreq = byFreq[: num_words]

        if ordered == 'asc':
            byFreq = sorted(byFreq, key=lambda word: word[1], reverse=False)

        return byFreq
