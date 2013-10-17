__author__ = 'skuli'
from twython import Twython, TwythonError
from authentication import auth

twitter = auth()

try:
    search_results = twitter.search(q='TheFooTypster', count=50)
except TwythonError as e:
    print e

for tweet in search_results['statuses']:
    print 'Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'), tweet['created_at'])
    print tweet['text'].encode('utf-8'), '\n'
