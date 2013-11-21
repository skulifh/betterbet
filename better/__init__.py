__author__ = 'skuli'
from twython import Twython, TwythonError
import sqlite3 as lite
import logging
from users import putUsersInTable, sortUsers
from authentication import auth

# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='./myapp.log',
                    filemode='w')
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)

logging.info('Starting')


twitter = auth()
putUsersInTable(twitter)
#sortUsers(2, 2)

logging.info('Finished')


#followids1 = twitter.get_followers_ids(screen_name='HillaryClinton')
#response = twitter.get_followers_ids(screen_name = "HillaryClinton")



