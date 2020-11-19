from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "191748305-u0W3nfaRh4Zd7oZ69KlcOUOn0IBHdsLL2BpiUsRS"
access_token_secret = "3HumtpX1QMbI5CEAqSHEbIeng8K1cklXPfiRyv7fkXGK5"
consumer_key = "AAOr5MRZ1mivbDoZRYDVajhXt"
consumer_secret = "EcbqbRnta3dAfy6tkmghmV5boESaTzs8SWWCu5OO3K6W14cxUQ"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


import simplejson as json


def get_tweet(doc):
    tweetItem = {}

    # Available tweet data
    tweetItem['text'] = doc['text']

    # hashtags are identified and provided as a field in the tweet
    tweetItem['hashtags'] = map(lambda x: x['text'], doc['entities']['hashtags'])

    # user_mentiones are identified and provided as a field
    tweetItem['user_mentions'] = map(lambda x: x['screen_name'], doc['entities']
    ['user_mentions'])  # symbols e.g. $APPL are identified and provided as a field
    tweetItem['symbols'] = map(lambda x: x['text'], doc['entities']['symbols'])
    tweetItem['coordinates'] = doc['coordinates']
    tweetItem['user_id'] = doc['user']['id']
    tweetItem['user_name'] = doc['user']['name']
    try:
        tweetItem['retweet_id'] = doc['retweeted_status']['id']

    except KeyError as e:
        tweetItem['retweet_id'] = 0
        pass

    return tweetItem

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])