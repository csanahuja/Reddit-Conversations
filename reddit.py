# -- coding: utf-8 --
import praw
import json
import argparse
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
    # print dir(submission)
    message = {}
    message['id'] = submission.id
    message['url'] = submission.url
    message['votes'] = submission.ups
    # Check attribute
    # message['upvote_ratio'] = submission.ratio
    message['author'] = submission.author.name
    message['text'] = submission.selftext
    message['parent'] = "ROOT"
    json_data = json.dumps(message)
    json_file.write(json_data + "\n")


# For debug purposes
def saveRawText(comment):
    txt_file.write("LEVEL: " + str(level) + " NUMº: " + str(i) +
                   " BODY: " + comment.body.encode('utf-8') + "\n")


if __name__ == '__main__' :

    # DEFAULT VALUES
    credentials_file = "credentials.txt"
    conversation_id = "6187ay"
    conversation_url = "https://www.reddit.com/r/news/comments/6187ay/couple_donates_bug_collection_worth_10m_a/"

    # Parse arguments
    parser = argparse.ArgumentParser(description = 'Parser for reddit.py')
    parser.add_argument('-u','--url', default = conversation_url, type = str, help = 'URL of Conversation', dest = 'url')
    parser.add_argument('-i','--id', default = conversation_id, type = str, help = 'ID of Conversation', dest = 'id')
    parser.add_argument('-c','--credentials', default = credentials_file, type = str, help = 'Credentials of API', dest = 'credentials_file')
    parser.add_argument('-l', '--link', default = False, action = "store_true", help = 'Use URL of Conversation, default ID', dest = 'use_link')
    args = parser.parse_args()

    cdr = Credentials(args.credentials_file)
    reddit = praw.Reddit(client_id=cdr.client_id,
                         client_secret=cdr.client_secret,
                         user_agent=cdr.user_agent,
                         username=cdr.username,
                         password=cdr.password)

    try:
        # Either get submission by ID or URL
        if args.use_link:
            submission = reddit.submission(url=args.url)
        else:
            submission = reddit.submission(id=args.id)

        saveSubmission(submission)

        # Start reading and parsing the Conversation
        print "STARTED: Reading the Conversation"
        print "Expected " + str(submission.num_comments) + \
              " Comments (On large conversations the expected number is not reached)"
        i = printCommentAndReplies(submission.comments)
        print "ENDED: Readed " + str(i) + " Comments"
    except Exception:
        print "Reddit API failed. Check Internet connectivity and credentials / parameters"
