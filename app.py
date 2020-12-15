from flask import Flask, request, render_template
import json
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import pandas as pd

import numpy as np
from numpy.linalg import norm
import pandas as pd
import nltk
nltk.download('punkt')
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
import pickle

app = Flask(__name__)

cosine_similarity = lambda a, b: np.inner(a, b) / norm(a) * norm(b) if norm(a) != 0.0 and norm(b) != 0.0 else 0.0
ps = PorterStemmer()
with open('save.pickle', 'rb') as f:
        matrix = pickle.load(f)
with open('cleantweet.pickle', 'rb') as f1:
    cleantweet = pickle.load(f1)
with open('tweetids.pickle', 'rb') as f2:
    tweetIds = pickle.load(f2)

def printTopSimilarTweets(tf_idf, tweet, cleanTweet, tweetIDs, n=20):

    
    cleanT = tweet.split()   # tokenize remaining document
    vec = [ps.stem(word) for word in cleanT] 
    tf_idf=tf_idf.append(pd.Series(name='TestTweet'))
    tf_idf=tf_idf.fillna(0)
    for i in vec:
        try:
            tf_idf.loc['TestTweet', i] += 1
        except:
            pass
    a= tf_idf.loc['TestTweet']
    result = tf_idf.apply(lambda row: cosine_similarity(a, row), 
                          axis='columns').sort_values(ascending=False) 
    
    tweets = ''

    for i in range(0, n):
        try:
            tweets += (str(i+1) + cleanTweet[tweetIDs.index(result.index[i])] + "<br><br>")
        except:
            pass
    return tweets


	
	
@app.route('/', methods=['GET', 'POST'])
def index():
    res = ''
    
    if request.method == 'POST':
        details = request.form
        res =  printTopSimilarTweets(matrix, details['text-to-analyse'], cleantweet, tweetIds)
    return render_template('index.html', result = res )

if __name__ == '__main__':
    app.run(host='0.0.0.0')
	
	
	
	
	
