import tweepy
from config import create_client

client = create_client()

response = client.create_tweet(text='hello world')