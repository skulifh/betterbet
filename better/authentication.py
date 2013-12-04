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

keys = [(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET), (APP_KEY2, APP_SECRET2, OAUTH_TOKEN2, OAUTH_TOKEN_SECRET2),
        (APP_KEY3, APP_SECRET3, OAUTH_TOKEN3, OAUTH_TOKEN_SECRET3), (APP_KEY4, APP_SECRET4, OAUTH_TOKEN4, OAUTH_TOKEN_SECRET4),
        (APP_KEY5, APP_SECRET5, OAUTH_TOKEN5, OAUTH_TOKEN_SECRET5)]

def auth():
    twitter = Twython(APP_KEY5, APP_SECRET5, OAUTH_TOKEN5
        , OAUTH_TOKEN_SECRET5)
    return twitter


class Authenticator:
    def __init__(self):
        self.key = 0;
        self.auth_APP_KEY = keys[self.key][0]
        self.auth_APP_SECRET = keys[self.key][1]
        self.auth_OAUTH_TOKEN = keys[self.key][2]
        self.auth_OAUTH_TOKEN_SECRET = keys[self.key][3]
        self.twython = Twython(self.auth_APP_KEY, self.auth_APP_SECRET, self.auth_OAUTH_TOKEN, self.auth_OAUTH_TOKEN_SECRET)
        print self.auth_OAUTH_TOKEN

    def switchKey(self):
        if self.key == 4:
            self.key = 0
            self.auth_APP_KEY = keys[self.key][0]
            self.auth_APP_SECRET = keys[self.key][1]
            self.auth_OAUTH_TOKEN = keys[self.key][2]
            self.auth_OAUTH_TOKEN_SECRET = keys[self.key][3]

        else:
            self.key += 1
            self.auth_APP_KEY = keys[self.key][0]
            self.auth_APP_SECRET = keys[self.key][1]
            self.auth_OAUTH_TOKEN = keys[self.key][2]
            selfauth_OAUTH_TOKEN_SECRET = keys[self.key][3]

        self.twython = Twython(self.auth_APP_KEY, self.auth_APP_SECRET, self.auth_OAUTH_TOKEN, self.auth_OAUTH_TOKEN_SECRET)