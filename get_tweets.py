import tweepy
import argparse

# Consumer keys and access tokens, used for OAuth
consumer_key = '<your-key>'
consumer_secret = '<your-secret>'
access_token = '<your-token>'
access_token_secret = '<your-token-secret>'

# Input arg (should be user to scrape)
parser = argparse.ArgumentParser()
parser.add_argument('-u','--user', help='twiter user to scrape', required=True)
args = parser.parse_args()

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

for status in tweepy.Cursor(api.user_timeline, screen_name=args.user).items():
    print(status._json['text'])