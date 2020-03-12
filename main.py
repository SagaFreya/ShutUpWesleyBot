from time import sleep
import threading

import praw

reddit = praw.Reddit('bot1', user_agent='linux:ml.sagafreya.shutupwesleybot:v0.1.0 (by /u/ssw663)')

print(reddit.read_only)

f = open('commented.txt', 'r+')

commented = f.read().splitlines()

wes = reddit.redditor('Wesley_Ford')

bot = reddit.redditor('ShutUpWesleyBot')

def delete_comments():
    while True:
        sleep(10)
        for c in bot.comments.new(limit=20):
            if c.score < 0:
                print('Deleted: ' + c.body)
                c.delete()

t = threading.Thread(target=delete_comments)

t.start()

for c in wes.stream.comments():
    if c.id not in commented:
        print(c.body)
        f.write(c.id + '\n')
        c.reply('Shut up, Wesley.')

t.join()
f.close()
