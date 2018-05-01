import praw
import pandas as pd

reddit = praw.Reddit(client_id='tc_fFbWZrkDSRw',
                     client_secret='fTq7nFVzdkCHFZY7jWQvHmkLpwk',
                     user_agent='lhimelman')

# assume you have a Reddit instance bound to variable `reddit`
#top_level_comments = list(submission.comments)
commentFreq = {}
subredditList = ["funny","AskReddit","todayilearned","science","worldnews","pics"]
headers = []
# for subredditname in subredditList:
#     print("subreddit started")
subreddit = reddit.subreddit('worldnews')
for submission in subreddit.hot(limit=1):
    all_comments = submission.comments.list()
    for c in all_comments:
        try:
            print(c.author.name, ":")
            userCFreq = {}
            for comment in reddit.redditor(c.author.name).comments.new(limit=None):
                # print(comment.subreddit)
                if comment.subreddit not in userCFreq:
                    userCFreq[comment.subreddit] = 1
                else:
                    userCFreq[comment.subreddit] += 1
                if comment.subreddit not in headers:
                    headers.append(comment.subreddit)

            commentFreq[c.author.name] = userCFreq
        except:
            pass

df = pd.DataFrame.from_dict(data=commentFreq, orient='index').fillna(0)
df.to_csv('redditData.csv',header=headers)
