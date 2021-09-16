import praw
from psaw import PushshiftAPI
from datetime import datetime, timedelta
import json


def scrape(subreddit):

    data = ''

    with open('./credentials.json') as jsonFile:
        data = json.load(jsonFile)

    ##create the reddit client using our credentials file
    reddit = praw.Reddit(client_id=data['credentials']['client_id'],
                         client_secret=data['credentials']['client_secret'],
                         user_agent=data['credentials']['user_agent'],
                         username=data['credentials']['username'],
                         password=data['credentials']['password'])
    pushApi = PushshiftAPI()

    ## get all posts for the last day that have the '$' character in them and have the due dilligence tag

    #epoch for 1 day ago
    start_epoch = int((datetime.today() - timedelta(days=1)).timestamp())

    #get list of posts
    posts = (pushApi.search_submissions(after=start_epoch, subreddit=subreddit))


    #innit posts
    #posts will have the post text, upvotes, comments, and their upvotes
    # posts[0] = {text: string, upvotes: number, comments: {text: string, upvotes: number, responses: {commentsObject}[]}}[]
    posts = []

    print("Posts:", posts)