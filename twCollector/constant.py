
import  os

DBPATH=None
consumer_key = None
consumer_secret = None
access_token = None
access_token_secret = None

if "ACCESS_TOKEN" in os.environ:

    DBPATH = os.environ['DBPATH']
    consumer_key = os.environ['CONSUMER_KEY']
    consumer_secret = os.environ['CONSUMER_SECRET_KEY']
    access_token = os.environ['ACCESS_TOKEN']
    access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
else:

    DBPATH = "mongodb://fotercim:212427123a1@ds121349.mlab.com:21349/data-science-database"
    consumer_key = 'GF7CSQPUIVtNYfjcCFDaO81aN'
    consumer_secret = 'uYzrrOqo3vX3P3zcRO4KPzLl6C7pNSO7kdkbBhUT0Rz32OrsfQ'
    access_token = '165432951-aQH41KBBuDfqpRQQfh6S0ocRbO7UpXn9f5Ri6CUk'
    access_token_secret = 'yFsvWY1dkY25BwWfB5RZMKE7V9b9fmOTEvjTsCcLUeeDO'
db_name = 'data-science-database'
collection_name= 'Tweets'
