# Reddit-Conversations

Reddit collector made using https://praw.readthedocs.io/en/latest/

This script now works both executing with python or with Scala. However if we
execute it from Scala we cannot use the parser as the reception of the data is
received on the stdin.

To the correct execution of the program we need to specify a value to the global
boolean variable of SCALA_FLAG where we specify either if we call it with python
or Scala

SCALA_FLAG = True  ->  We call the program with Scala
SCALA_FLAG = False ->  We call the program with python


## Python

Remember to set SCALA_FLAG = False
Usage:

```
python reddit.py [-h] [-u URL] [-i ID] [-c CREDENTIALS_FILE] [-l]
```

Arguments:
  -h: Shows the help
  -u: URL of conversation. I.E: https://www.reddit.com/r/news/comments/6187ay/couple_donates_bug_collection_worth_10m_a/
  -i: ID of conversation. I.E: 6187ay
  -c: File with private information required to the use of the API
  -l: Use the URL to get the conversation. By default use the ID.

Note that we can get a conversation by its URL or its ID. We will normally use the
ID since its more confortable. To get the ID of a conversation you just need to check
the URL after the comments/ string.

The feedback of the program will print a message on the screen each 100 messages
readed so we known it is working correctly. To get a large conversation can be slow
due to the requests required to get all messages (API workflow)

The output will be saved in JSON format. Each message will be saved in JSON line.
We can modify the global variable of the json_file to wherever we want to save the
output.

## Scala

TO BE CONTINUED
