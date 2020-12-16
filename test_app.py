import unittest
import app
import pickle
# -*- coding: utf-8 -*-


class TestApp(unittest.TestCase):

    def test_add(self):

        res1 = """1"Via @washingtonpost by @costareports: “Trump says he is serious about 2016 bid, is hiring staff and delaying TV gig”http://www.washingtonpost.com/politics/trump-says-he-is-serious-about-2016-bid-is-hiring-staff-and-delaying-tv-gig/2015/02/25/4e9d3804-bd07-11e4-8668-4e7ba8439ca6_story.html …"<br><br>"""
        res2 = """1“Obamacare Data Mismatch Could Leave Thousands Uninsured” http://www.usnews.com/news/articles/2014/09/16/obamacare-data-mismatch-could-leave-thousands-uninsured-at-election-time … ObamaCare is not working and has missed all targets.<br><br>2"Via @washingtonpost by @costareports: “Trump says he is serious about 2016 bid, is hiring staff and delaying TV gig”http://www.washingtonpost.com/politics/trump-says-he-is-serious-about-2016-bid-is-hiring-staff-and-delaying-tv-gig/2015/02/25/4e9d3804-bd07-11e4-8668-4e7ba8439ca6_story.html …"<br><br>3President Obama is under pressure from Democrats to undo his lie on ObamaCare. His problem is that such a move would end ObamaCare.<br><br>"""

        #with open('save.pickle', 'rb') as f:
        #    matrix = pickle.load(f)
        #with open('cleantweet.pickle', 'rb') as f1:
        #    cleantweet = pickle.load(f1)
        #with open('tweetids.pickle', 'rb') as f2:
        #    tweetIds = pickle.load(f2)


        #printTopSimilarTweets(tf_idf, tweet, cleanTweet, tweetIDs, n=20)

        self.assertEqual(app.printTopSimilarTweets(app.matrix, 'russia is leaded by putin', app.cleanTweet, app.tweetIDs, n=1), res1)
        self.assertEqual(app.printTopSimilarTweets(app.matrix, 'obamacare is great', app.cleanTweet, app.tweetIDs, n=3), res2)        


if __name__ == '__main__':
    unittest.main()
