# -- coding: utf-8 --
import praw
from praw.models import MoreComments
from private import Credentials

#Global vars
output = open('reddit.txt', 'w+')

def debug(comments, comments2, index):
    print len(comments)
    print len(comments2)
    for c in comments:
        print "c1 " + c.body.encode('utf-8')
    for c in comments2:
        print "c2 " + c.body.encode('utf-8')

def printCommentAndReplies(comments, i = 0, level=0):
    index = 0
    for comment in comments:
        if isinstance(comment, MoreComments):
            comments.replace_more()
            return printCommentAndReplies(comments[index:], i, level)

            #debug(comments, comments[index:], index)
        else:
            i += 1
            index += 1
            output.write("LEVEL: " + str(level) + " NUMº: " + str(i) +
                        " BODY: " + comment.body.encode('utf-8') + "\n")
            i = printCommentAndReplies(comment.replies, i, level+1)
    return i


if __name__ == '__main__' :
    cdr = Credentials()
    reddit = praw.Reddit(client_id=cdr.client_id,
                         client_secret=cdr.client_secret,
                         user_agent=cdr.user_agent,
                         username=cdr.username,
                         password=cdr.password)


    #print reddit.user.me()

    conversation_id = "6187ay"
    conversation_url = "https://www.reddit.com/r/news/comments/6187ay/couple_donates_bug_collection_worth_10m_a/"

    submission = reddit.submission(id=conversation_id)
    # submission = reddit.submission(url=conversation_url)

    i = printCommentAndReplies(submission.comments)
    print "Readed comments:" + str(i)
