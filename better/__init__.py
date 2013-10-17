__author__ = 'skuli'
from twython import Twython, TwythonError

twitter = Twython("7pdvVotiZRfbJ1e7mpIVqA", "EpBnZpC1qKY6yJ0Uett07zrORpfb5XV7yQfSwoik", "1954450040-1pNgKK2bSIN7qRYhy7fUFdSgPhpTuzEKT3xXqCy"
, "pWpWbwp12xBoZcY3E3cQH4NiGpOLniNeYuoT6EFnXc")

try:
    search_results = twitter.search(q='TheFooTypster', count=50)
except TwythonError as e:
    print e

for tweet in search_results['statuses']:
    print 'Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'), tweet['created_at'])
    print tweet['text'].encode('utf-8'), '\n'
