__author__ = 'skuli'
from twython import Twython
def auth():
    APP_KEY = "0rHl9NF4J0p2jKjS70Y7Lg"
    APP_SECRET = "3zMKTV9sXcvqm0tYESye0DQ0UR1RS4OEn01inQuYno"
    OAUTH_TOKEN = "1954450040-LL5L2nnUmuAMHqawhQRNlRviB2T8GN8nuQ8FAXS"
    OAUTH_TOKEN_SECRET = "Kkn8ArYeWcbypg5EyCgBUoaPFLnCuLt0hwq943BrJjc"
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    return twitter