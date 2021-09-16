import praw
from psaw import PushshiftAPI
from datetime import datetime, timedelta
import json


def scrape(subreddit):

    data = ''

    with open('./credentials.json') as jsonFile:
        data = json.load(jsonFile)

    # create the reddit client using our credentials file
    reddit = praw.Reddit(client_id=data['credentials']['client_id'],
                         client_secret=data['credentials']['client_secret'],
                         user_agent=data['credentials']['user_agent'],
                         username=data['credentials']['username'],
                         password=data['credentials']['password'])

    # innit posts
    posts = []

    # get top 100 posts of the day
    for submission in reddit.subreddit(subreddit).top(time_filter='day'):
        posts.append(submission)

    return posts
