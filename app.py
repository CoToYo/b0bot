from flask import Flask
from dotenv import load_dotenv
import os
from twarc import Twarc2, expansions
import json
import tweepy

# Load variables from .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')
API_KEY_SECRET = os.getenv('API_KEY_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET ')

# OAuth1.0 User Context for Twitter API(v2) using Tweepy
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_KEY_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# In case some features of older version of Twitter API(v1.1) are needed,
# use the following codes to authenticate for using the API.
auth = tweepy.OAuth1UserHandler(
   API_KEY, API_KEY_SECRET,
   ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)

# OAuth2.0 Authorization Code Flow with PKCE (User Context)
# Upgraded authentication with stronger security level, but needs more complex authenticating process.
# Not needed for now.
# 
# oauth2_user_handler = tweepy.OAuth2UserHandler(
#     client_id = CLIENT_ID,
#     redirect_uri="http://example.com",
#     scope = ["tweet.write"],
#     # Client Secret is only necessary if using a confidential client
#     client_secret = CLIENT_SECRET
# )


client.create_tweet(text="Hello Twitter!")
# client.retweet(1664086413741277185)