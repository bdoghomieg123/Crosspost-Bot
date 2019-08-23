#Sub A IndiaSpeaks  Sub B - IndiaSpeaksTrending
import praw #the Python Reddit API Wrapper

reddit = praw.Reddit('bot1')
while True:
    subreddit = reddit.subreddit('IndiaSpeaks') #mofify the text inside the quotes to change where to crosspost FROM
    for submission in subreddit.hot(limit=2):
        if submission.stickied: 
            crosspost_subreddit = "indiaspeakstrending" #change this to change where to crosspost TO
            submission.crosspost(subreddit=crosspost_subreddit.lower(),send_replies=False)
            exit()
