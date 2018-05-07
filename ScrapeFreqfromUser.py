import praw
import pandas as pd
import sys

def scrapeSubreddit(reddit, users):
    commentFreq = {}
    headers = []
    usernum = 1
    for user in users:
        userCFreq = {}
        try:
            for comment in reddit.redditor(user).comments.new(limit=None):
                sub = comment.subreddit
                if sub not in userCFreq:
                    userCFreq[sub] = 1
                else:
                    userCFreq[sub] += 1
                if sub not in headers:
                    headers.append(sub)
            commentFreq[user] = userCFreq
            usernum = usernum + 1
            print(usernum, "out of", len(users))
        except:
            print("something went wrong")
    return commentFreq,headers

if __name__ == "__main__":

    ##To use, add cmdline parameters of where csv should be saved, what initial sub to use, and how manyn posts on that sub to look at.
    SaveFile = sys.argv[1]
    userfile = open(sys.argv[2],"r")
    next(userfile)
    userlist = userfile.read().split(",")
    userlist = userlist[:-1]
    print(userlist)

    reddit = praw.Reddit(client_id='tc_fFbWZrkDSRw',
                         client_secret='fTq7nFVzdkCHFZY7jWQvHmkLpwk',
                         user_agent='lhimelman')

    cfreq,headers = scrapeSubreddit(reddit,userlist)

    df = pd.DataFrame.from_dict(data=cfreq, orient='index').fillna(0)
    df.to_csv(SaveFile,header=headers)
