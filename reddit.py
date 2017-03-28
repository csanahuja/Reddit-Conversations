# -- coding: utf-8 --
import praw
import json
from praw.models import MoreComments
from private import Credentials

#Global vars
txt_file = open('reddit.txt', 'w+')
json_file = open('reddit.json','w+')
json_data = None

# Alg. to get all messages
def printCommentAndReplies(comments, i = 0, level=1):
    index = 0
    for comment in comments:
        if isinstance(comment, MoreComments):
            comments.replace_more()
            return printCommentAndReplies(comments[index:], i, level)
        else:
            i += 1
            index += 1
            if i%100 == 0:
                print "Readed " + str(i) + " Comments"
            saveMessage(comment)
            i = printCommentAndReplies(comment.replies, i, level+1)
    return i

# Save message as JSON
def saveMessage(comment):
    global json_data

    #Uncomment to save raw text messages
    #saveRawText(comment)

    #Save Json
    message = {}
    message['id'] = comment.id
    try:
        message['author'] = comment.author.name
    except AttributeError:
        message['author'] = 'deleted'
    message['text'] = comment.body.encode('utf-8')
    message['parent'] = comment.parent().id
    json_data = json.dumps(message)
    json_file.write(json_data + "\n")

def saveSubmission(submission):
    pass


# For debug purposes
def saveRawText(comment):
    txt_file.write("LEVEL: " + str(level) + " NUMº: " + str(i) +
                   " BODY: " + comment.body.encode('utf-8') + "\n")


if __name__ == '__main__' :
    cdr = Credentials()
    reddit = praw.Reddit(client_id=cdr.client_id,
                         client_secret=cdr.client_secret,
                         user_agent=cdr.user_agent,
                         username=cdr.username,
                         password=cdr.password)

    conversation_id = "6187ay"
    conversation_url = "https://www.reddit.com/r/news/comments/6187ay/couple_donates_bug_collection_worth_10m_a/"

    submission = reddit.submission(id=conversation_id)
    # submission = reddit.submission(url=conversation_url)
    print submission.url
    print dir(submission)
    print submission.ups
    print submission.downs
    print submission.over_18
    print submission.locked
    print submission.upvote_ratio
    print submission.selftext

    print "STARTED: Reading the Conversation"
    print "Expected " + str(submission.num_comments) + \
          " Comments (On large conversations the expected number is not reached)"
    i = printCommentAndReplies(submission.comments)
    print "ENDED: Readed " + str(i) + " Comments"
