""" contains the auth() function as well as 5 twitter_dev informations """
__author__ = 'skuli'
from twython import Twython

#Fra Skula
APP_KEY = '0rHl9NF4J0p2jKjS70Y7Lg'
APP_SECRET = '3zMKTV9sXcvqm0tYESye0DQ0UR1RS4OEn01inQuYno'
OAUTH_TOKEN = '1954450040-LL5L2nnUmuAMHqawhQRNlRviB2T8GN8nuQ8FAXS'
OAUTH_TOKEN_SECRET = 'Kkn8ArYeWcbypg5EyCgBUoaPFLnCuLt0hwq943BrJjc'

#Fra Asgeiri
APP_KEY2 = 'OjqtGZukBSx8176uD9OcQ'
APP_SECRET2 = 'HUiaIEjpWVeDT02D4ntX1rKuftGZvuEoFOjR08bI'
OAUTH_TOKEN2 = '3323813109-7zmzmckEvYfglZlGXtBHvQZ9l0nhfhNrZ7zJFzmJ'
OAUTH_TOKEN_SECRET2 = 'dOdX2i9K8fnqscPo2QpoojrNxmHEq2p4LSnLvH5Hu64'

#Nyja fra Asgeiri
APP_KEY3 = 'nD3jDCrPnjoGHvnuVj6fMQ'
APP_SECRET3 = 'gZ4I8PdFAnYGxcPM5d3WpTAiNLBuRxhZqERiYct1biI'
OAUTH_TOKEN3 = '323813109-MPDpGNtJxtugv0F1Um3bT3V7dfgty71VyWVfhABt'
OAUTH_TOKEN_SECRET3 = 'XauF4si2geyCrAaJ1rko1gw8bQfHWgLoCdLQn43iE'

#Nyjasta fra Skula
APP_KEY4 = 'VOWM6G4i8rtFktRlgHbIwg'
APP_SECRET4 = 'tLoBHWrUAPknkzIWq9F1l51f3vZe3MU5JAfNNCK4'
OAUTH_TOKEN4 = '2187937866-Vn4TCGqEfzSzQ5w5ZLlVS0WP07QhOlgjfLclhG6'
OAUTH_TOKEN_SECRET4 = 'WivD28HQwbncHw1SGcFKKEtHbVPXgFdIGEiuSpWGsOGdM'

APP_KEY5 = 'evJC5xknfbZlDS9JtvbkA'
APP_SECRET5 = '5dEiQWOvxTq7mTMoziimDkKseqnuEZotGlHGFwnM'
OAUTH_TOKEN5 = '2187937866-1djGOO5q2mlvCxaOegBVOzG1b5kigIHV1q1Bliv'
OAUTH_TOKEN_SECRET5 = '0iKZRFhiOTlmUOoFPgHGPNNtsPmsO4VMbQc212FrBlQ3b'


def auth():
    """ Authorises the twitter_dev account and project in order to use
    the twitter api"""
    twitter = Twython(APP_KEY5, APP_SECRET5, OAUTH_TOKEN5
        , OAUTH_TOKEN_SECRET5)
    return twitter