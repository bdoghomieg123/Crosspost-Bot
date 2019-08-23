#Sub A IndiaSpeaks  Sub B - IndiaSpeaksTrending
import praw
import os
import time
from common import clear

reddit = praw.Reddit('bot1')
while True:
    subreddit = reddit.subreddit('IndiaSpeaks')
    for submission in subreddit.hot(limit=2):
        if submission.stickied:
            submission.crosspost(subreddit="indiaspeakstrending",send_replies=False)
            exit()
