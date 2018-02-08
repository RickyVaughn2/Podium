from __future__ import absolute_import, print_function
from tweepy.streaming import StreamListener
from tweepy import Stream
import tweepy
import argparse

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key = '<your-key>'
consumer_secret = '<your-secret>'
access_token = '<your-token>'
access_token_secret = '<your-token-secret>'

# Creation of the actual interface, using authentication
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# args
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user', help='twiter user to scrape', required=True)
args = parser.parse_args()

# username to id
user = api.get_user(screen_name=args.user)
print('streaming tweets from ' + args.user + '(' + str(user.id) + '):')


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    l = StdOutListener()

    stream = Stream(auth, l)
    # stream tweets from our user
    stream.filter(follow=[str(user.id)])
