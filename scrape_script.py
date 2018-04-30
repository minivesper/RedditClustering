import praw
import pylab as plt
from scipy.stats import ttest_ind

reddit = praw.Reddit(client_id='tc_fFbWZrkDSRw',
                     client_secret='fTq7nFVzdkCHFZY7jWQvHmkLpwk',
                     user_agent='lhimelman',
                    username = 'lhimelman',
                    password = 'madisonave77')

# assume you have a Reddit instance bound to variable `reddit`
#top_level_comments = list(submission.comments)
commentFreq = {}
subredditList = ["funny","AskReddit","todayilearned","science","worldnews","pics"]
for subredditname in subredditList:
    subreddit = reddit.subreddit('funny')
    for submission in subreddit.hot(limit=1):
        all_comments = submission.comments.list()
        for c in all_comments:
            try:
                print(c.author.name, ":")
                userCFreq = {}
                for comment in reddit.redditor(c.author.name).comments.new(limit = 10):
                    print(comment.subreddit)
                    if comment.subreddit not in userCFreq:
                        userCFreq[comment.subreddit] = 1
                    else:
                        userCFreq[comment.subreddit] += 1
                commentFreq[c.author.name] = userCFreq
            except:
                pass
            print(commentFreq)
