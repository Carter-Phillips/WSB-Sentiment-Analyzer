from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from ratelimit import limits, sleep_and_retry
from google.cloud import language_v1
import json

CALLS = 450
TIME_PERIOD = 60

class Analyzer():
    def __init__(self, maxThreads = 10):
        self.client = language_v1.LanguageServiceClient()
        self.threadpool = ThreadPoolExecutor(maxThreads)

    def analyze(self, posts):
        sentiments = []

        x = 0

        for post in posts:
            post, commentText = self.formatPost(post)
            postSentiment = self.threadpool.submit(self.getSentiment, post)
            for text in commentText:
                sentiments.append(self.threadpool.submit(self.getSentiment, text))

            commentSentiment = []
            for sentiment in sentiments:
                try:
                    commentSentiment.append(sentiment.result())
                except:
                    continue

            sentiments.append({'postSentiment': postSentiment.result(), 'commentSentiment': commentSentiment})
            x = x+1
            print('done post #', x)

        return sentiments


    @sleep_and_retry
    @limits(calls=CALLS, period=TIME_PERIOD)
    def getSentiment(self, text):

        document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
        try:
            response = self.client.analyze_sentiment(request={'document': document})
        except: #other languages can cause an exception, wack
            return []
        return response.sentiment.score


    def formatPost(self, post):
        formatted = []
        comments = post.comments
        commentText = []
        for comment in comments:
            try:
                commentText.append(comment.body)
            except:
                return post.selftext, commentText

        return post.selftext, commentText