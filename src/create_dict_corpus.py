import os
import numpy as np
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly as py
import plotly.graph_objs as go
import argparse

# init_notebook_mode(connected=True) #do not miss this line

from gensim import corpora, models, similarities

import warnings
import pandas as pd

import logging
from nltk.corpus import stopwords
from string import punctuation
from gensim import corpora
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
warnings.filterwarnings("ignore")


def create_stop_words(custom_stop_words):
        # remove common words and tokenize
        # list1 = ['RT', 'rt', 'get', 'got', 'would', 'think', 'thought', '"']
        my_stopwords = []
        with open(custom_stop_words) as f:
            for word in f:
                my_stopwords.append(word.rstrip('\n'))

        stoplist = stopwords.words('english') + list(punctuation) + my_stopwords

        return stoplist


def clean_text_data(text_array, stop_words):
    stop_list = create_stop_words(stop_words)
    texts = [[word for word in str(document).lower().split() if word not in stop_list] for document in text_array]

    return texts


def get_parser():
    """Get parser for command line arguments."""
    parser = argparse.ArgumentParser(description="Tweet Cleaning and Creating Corpus and Dictionary files")
    parser.add_argument("-i",
                        "--input",
                        dest="inputs",
                        help="the path of the csv input file",
                        default='input/data_elonmusk.csv')

    parser.add_argument("-s",
                        "--separator",
                        dest="separator",
                        help="Separator of the csv input file",
                        default=",")

    parser.add_argument("-e",
                        "--encoding",
                        dest="encoding",
                        help="Encoding of the csv input file",
                        default="latin1")

    parser.add_argument("-o",
                        "--outputFolder",
                        dest="out",
                        help="the path of the output folder",
                        default="output")


    parser.add_argument("-t",
                        "--textHeader",
                        dest="textHeader",
                        help="the header of text column",
                        default='Tweet')

    parser.add_argument("-n",
                        "--fileName",
                        dest="fileName",
                        help="the name of the output file",
                        default='elon')

    parser.add_argument("-w",
                        "--stopwords",
                        dest="stopwordsFile",
                        help="Path to stopwords file",
                        default='input/stopwords.txt')

    return parser


def create_dict_and_corpus(inputFile, separator, encoding, outputFolder, text_header='Tweet', filename='data', stop_words='input/stopwords.txt'):
        tweets = pd.read_csv(inputFile, sep=separator, encoding=encoding)
        all_tweets = tweets[text_header]

        corpus = []
        for tweet in all_tweets:
            corpus.append(tweet)

        logging.info('total tweets: ' + str(len(corpus)))

        print('Folder "{}" will be used to save dictionary and corpus.'.format(outputFolder))
        texts = clean_text_data(corpus, stop_words)

        dictionary = corpora.Dictionary(texts)
        dictionary.save(os.path.join(outputFolder, filename + '.dict'))  # store the dictionary, for future reference

        corpus = [dictionary.doc2bow(text) for text in texts]
        corpora.MmCorpus.serialize(os.path.join('output', filename + '.mm'), corpus)  # store to disk, for later use


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    create_dict_and_corpus(args.inputs, args.separator, args.encoding, args.out, args.textHeader, args.fileName, args.stopwordsFile)
    print("done")
