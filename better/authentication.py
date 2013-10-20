__author__ = 'skuli'
from twython import Twython
def auth():

    #Fra Skula
    APP_KEY = '7pdvVotiZRfbJ1e7mpIVqA'
    APP_SECRET = 'EpBnZpC1qKY6yJ0Uett07zrORpfb5XV7yQfSwoik'
    OAUTH_TOKEN = '1954450040-1pNgKK2bSIN7qRYhy7fUFdSgPhpTuzEKT3xXqCy'
    OAUTH_TOKEN_SECRET = 'uh4Plp6goHs9kSioeJfn6ePzfDWJXkRWu1GJIfb8'

    #Fra Asgeiri
    APP_KEY2 = 'OjqtGZukBSx8176uD9OcQ'
    APP_SECRET2 = 'HUiaIEjpWVeDT02D4ntX1rKuftGZvuEoFOjR08bI'
    OAUTH_TOKEN2 = '3323813109-7zmzmckEvYfglZlGXtBHvQZ9l0nhfhNrZ7zJFzmJ'
    OAUTH_TOKEN_SECRET2 = 'dOdX2i9K8fnqscPo2QpoojrNxmHEq2p4LSnLvH5Hu64'

    #Nyja fra Asgeiri
    APP_KEY = 'nD3jDCrPnjoGHvnuVj6fMQ'
    APP_SECRET = 'gZ4I8PdFAnYGxcPM5d3WpTAiNLBuRxhZqERiYct1biI'
    OAUTH_TOKEN = '323813109-MPDpGNtJxtugv0F1Um3bT3V7dfgty71VyWVfhABt'
    OAUTH_TOKEN_SECRET = 'XauF4si2geyCrAaJ1rko1gw8bQfHWgLoCdLQn43iE'

    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN
        , OAUTH_TOKEN_SECRET)
    return twitter