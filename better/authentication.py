__author__ = 'skuli'
from twython import Twython
def auth():

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

    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN
        , OAUTH_TOKEN_SECRET)
    return twitter