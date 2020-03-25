import sys

import praw

reddit = praw.Reddit('bot1', user_agent='linux:ml.sagafreya.shutupwesleybot:v0.1.0 (by /u/ssw663)')
print(reddit.read_only)

f = open('commented.txt', 'r+')
f.seek(0)
commented = f.read().splitlines()

wes = reddit.redditor('Wesley_Ford')
bot = reddit.redditor('ShutUpWesleyBot')

def delete_comments():
    for c in bot.comments.new(limit=10):
        if c.score < 0:
            print('Deleted: ' + c.body)
            c.delete()

delete_comments()

def main():
    for c in wes.stream.comments():
        if c.id not in commented:
            print('Found: ' + c.body)
            try:
                f.write(c.id + '\n')
                commented.append(c.id)
            except:
                print('Failed to save comment')
                sys.exit()
            try:
                c.reply('Shut up, Wesley.')
                delete_comments()
            except:
                print('Failed to respond to comment')
                main()

main()

f.close()
