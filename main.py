import praw

reddit = praw.Reddit('bot1', user_agent='linux:ml.sagafreya.shutupwesleybot:v0.0.2 (by /u/ssw663)')

print(reddit.read_only)

f = open('commented.txt', 'r+')

commented = f.read().splitlines()

wes = reddit.redditor('Wesley_Ford')

for c in wes.stream.comments():
    if c.id not in commented:
        print(c.body)
        f.write(c.id + '\n')
