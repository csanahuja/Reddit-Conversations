# -- coding: utf-8 --
import praw
from praw.models import MoreComments
from private import Credentials

#Global vars
i = 1
output = open('reddit.txt', 'w+')

def printCommentAndReplies(comment, i):
    if isinstance(comment, MoreComments):
        for more in comment.comments():
            pass
    else:
        output.write(str(i) + ": " + comment.body.encode('utf-8') + "\n")
        i += 1

        for reply in comment.replies.replace_more():
            i = printCommentAndReplies(reply, i)
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
    # conversation_id = "618nlp"
    conversation_url = "https://www.reddit.com/r/news/comments/6187ay/couple_donates_bug_collection_worth_10m_a/"

    submission = reddit.submission(id=conversation_id)
    # submission = reddit.submission(url=conversation_url)

    top_comments = submission.comments

    for comment in top_comments.replace_more(limit=2):
         i = printCommentAndReplies(comment, i)
    print i
