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

n_tweets_to_read = 5000 # Choose the number of tweets to read

cosine_similarity = lambda a, b: np.inner(a, b) / norm(a) * norm(b) if norm(a) != 0.0 and norm(b) != 0.0 else 0.0

def TermDocumentMatrix(docs, docIDs=None):
    vectorizer = CountVectorizer(lowercase=True, stop_words=None)
    tdm = vectorizer.fit_transform(docs)
    tdm_feature_names = vectorizer.get_feature_names()
    #
    df = pd.DataFrame(tdm.toarray(), columns=tdm_feature_names, dtype="float64")
    if docIDs is not None:
        df.index = docIDs    
    return df

#Initialisation
ps = PorterStemmer()

# Read the data and remove duplicates if exist
tweets = []
with open("data/data.txt", encoding="utf-8") as file:
    for i, line in enumerate(file):
        if i < n_tweets_to_read:
            tweets.append(line)
        else:
            break  
tweets = list(set(tweets)) # delete duplicates
print("{} unique Tweets loaded\n".format(len(tweets)))

# Data Cleanning and prepocesing phase
cleanTweet = []
tweetIDs = []
tweetsProcessed = []
for tweet in tweets:
    try:
        doc = tweet.split("\t") 
        if len(doc)==7:
            cleanTweet.append(doc[5])
            tweetIDs.append(doc[0])     # add ID to a list
            doc = doc[5:6]   # remove everything that's note the tweet content      
            tok_doc = word_tokenize(" ".join(doc))    # tokenize remaining document
            stemmed_doc = [ps.stem(word) for word in tok_doc] 
            tweetsProcessed.append(" ".join(stemmed_doc))   #stemmed words
    except:
        pass

# TF-IDF construction part

# Terms frequency
tdf = TermDocumentMatrix(tweetsProcessed, tweetIDs)

# Document frequency
documentFrequencies = []
for index, series in tdf.iteritems(): 
    documentFrequencies.append(len(series.nonzero()[0])) 

# TF-IDF weight
tdf.applymap(lambda x: 1.0 + np.log10(x) if x > 0.0 else 0.0) # log frequency weight
idf = pd.Series(np.log10(len(tweets)/np.array(documentFrequencies))) # Inverse document frequency
matrix = tdf * idf.values


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
        res =  printTopSimilarTweets(matrix, details['text-to-analyse'], cleanTweet, tweetIDs)
    return render_template('index.html', result = res )

if __name__ == '__main__':
    app.run(host='0.0.0.0')
	
	
	
	
	
