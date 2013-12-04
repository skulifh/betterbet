__author__ = 'skuli'
from twython import Twython, TwythonError
from CheckSpelling import SpellChecker
import sqlite3 as lite
import logging
from users import putUsersInTable, sortUsers
from authentication import auth
from statuses import statuses

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

# set the wtitter authentication
twitter = auth()

# put all the users into table
#putUsersInTable(twitter)

# sort all of the users
#sortUsers(2, 1)

# check the status of all the users
#statuses(twitter)

SpellChecker()

logging.info('Finished')


#followids1 = twitter.get_followers_ids(screen_name='HillaryClinton')
#response = twitter.get_followers_ids(screen_name = "HillaryClinton")



