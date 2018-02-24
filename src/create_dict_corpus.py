import os
import numpy as np
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly as py
import plotly.graph_objs as go

init_notebook_mode(connected=True) #do not miss this line

from gensim import corpora, models, similarities

import warnings
import pandas as pd
import gensim
import logging
import tempfile
from nltk.corpus import stopwords
from string import punctuation
from gensim import corpora
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

warnings.filterwarnings("ignore")


def create_dict_and_corpus(inputFile, outputFolder, filename='data'):

        tweets = pd.read_csv(inputFile, encoding='latin1')
        tweets = tweets.assign(Time=pd.to_datetime(tweets.Time)).drop('row ID', axis='columns')

        tweets.head(10)

        range(len(tweets['Tweet']))
        tweets['Time'] = pd.to_datetime(tweets['Time'], format='%y-%m-%d %H:%M:%S')
        tweetsT = tweets['Time']

        corpus=[]
        a=[]
        for i in range(len(tweets['Tweet'])):
                a=tweets['Tweet'][i]
                corpus.append(a)

        print('Folder "{}" will be used to save temporary dictionary and corpus.'.format(outputFolder))



        # remove common words and tokenize
        list1 = ['RT','rt']
        stoplist = stopwords.words('english') + list(punctuation) + list1

        texts = [[word for word in str(document).lower().split() if word not in stoplist] for document in corpus]

        dictionary = corpora.Dictionary(texts)
        dictionary.save(os.path.join(outputFolder, filename + '.dict'))  # store the dictionary, for future reference

myInput = 'input/data_elonmusk.csv'
outputFolder = 'output'

create_dict_and_corpus(myInput, outputFolder=outputFolder, filename='elon')
