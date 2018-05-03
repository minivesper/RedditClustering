import praw
import pandas as pd
import sys

def scrapeUsers(reddit, subredditList, postNum):
    subnum = 0
    for subredditname in subredditList:
        users = []
        posts = reddit.subreddit(subredditname).hot(limit=postNum)
        pc = 0
        for submission in posts:
            all_comments = submission.comments.list()
            for c in all_comments:
                try:
                    name = c.author.name
                    if name not in users:
                        users.append(name)
                except:
                    pass
            pc = pc + 1
            print( pc, "post")
        subnum = subnum + 1
        print( subnum, "subreddit")
    return users

if __name__ == "__main__":

    ##To use, add cmdline parameters of where csv should be saved, what initial sub to use, and how manyn posts on that sub to look at.
    SaveFile = sys.argv[1]
    initSubs = sys.argv[2].split(",")
    postNum = int(sys.argv[3])

    reddit = praw.Reddit(client_id='tc_fFbWZrkDSRw',
                         client_secret='fTq7nFVzdkCHFZY7jWQvHmkLpwk',
                         user_agent='lhimelman')

    users = scrapeUsers(reddit,initSubs,postNum)

    f = open(SaveFile, "w+")
    f.write(str(len(users)))
    f.write("\n")
    for i in users:
        f.write(i)
        f.write(",")
    f.close()
