# -*- coding: utf-8 -*-
import unittest
import app
import pickle
import time


class TestApp(unittest.TestCase):

    def test_add(self):

        res1 = """1"Via @washingtonpost by @costareports: “Trump says he is serious about 2016 bid, is hiring staff and delaying TV gig”http://www.washingtonpost.com/politics/trump-says-he-is-serious-about-2016-bid-is-hiring-staff-and-delaying-tv-gig/2015/02/25/4e9d3804-bd07-11e4-8668-4e7ba8439ca6_story.html …"<br><br>"""
        res2 = """1Another health insurer is pulling back due to 'persistent financial losses on #Obamacare plans.' Only the beginning!http://www.nbcnews.com/business/business-news/aetna-pulls-back-obamacare-health-insurance-plans-2017-n631656 …<br><br>2"Via @washingtonpost by @costareports: “Trump says he is serious about 2016 bid, is hiring staff and delaying TV gig”http://www.washingtonpost.com/politics/trump-says-he-is-serious-about-2016-bid-is-hiring-staff-and-delaying-tv-gig/2015/02/25/4e9d3804-bd07-11e4-8668-4e7ba8439ca6_story.html …"<br><br>3"We will repeal & replace #Obamacare, which has caused soaring double-digit premium increases. It is a disaster!https://amp.twimg.com/v/ddb1eaf1-bdc5-44b3-b090-dc20494568f7 …"<br><br>"""

        #with open('save.pickle', 'rb') as f:
        #    matrix = pickle.load(f)
        #with open('cleantweet.pickle', 'rb') as f1:
        #    cleantweet = pickle.load(f1)
        #with open('tweetids.pickle', 'rb') as f2:
        #    tweetIds = pickle.load(f2)


        #printTopSimilarTweets(tf_idf, tweet, cleanTweet, tweetIDs, n=20)
        time.sleep(60)
        self.assertEqual(app.printTopSimilarTweets(app.matrix, 'russia is leaded by putin', app.cleanTweet, app.tweetIDs, n=1), res1)
        self.assertEqual(app.printTopSimilarTweets(app.matrix, 'obamacare is great', app.cleanTweet, app.tweetIDs, n=3), res2)        


if __name__ == '__main__':
    unittest.main()
