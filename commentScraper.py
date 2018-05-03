import praw
import pandas as pd
import sys

def scrapeSubreddit(reddit, subredditname, postNum):
    commentFreq = {}
    headers = []
    subreddit = reddit.subreddit(subredditname)
    for submission in subreddit.hot(limit=postNum):
        all_comments = submission.comments.list()
        for c in all_comments:
            try:
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
        print("one post")
    return commentFreq,headers

if __name__ == "__main__":

    ##To use, add cmdline parameters of where csv should be saved, what initial sub to use, and how manyn posts on that sub to look at.
    SaveFile = sys.argv[1]
    initSub = sys.argv[2]
    postNum = int(sys.argv[3])

    reddit = praw.Reddit(client_id='tc_fFbWZrkDSRw',
                         client_secret='fTq7nFVzdkCHFZY7jWQvHmkLpwk',
                         user_agent='lhimelman')

    cfreq,headers = scrapeSubreddit(reddit,initSub,postNum)

    df = pd.DataFrame.from_dict(data=cfreq, orient='index').fillna(0)
    df.to_csv(SaveFile,header=headers)
