import praw

reddit = praw.Reddit('bot1', user_agent='linux:ml.sagafreya.shutupwesleybot:v0.0.1 (by /u/ssw663)')

print(reddit.read_only)

wes = reddit.redditor('Wesley_Ford')

for c in wes.stream.comments():
    print(c.body)
