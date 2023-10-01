from decouple import config

CLIENT_ID = config('APP_ID')
CLIENT_SECRET =  config('APP_SECRET')
LONG_TOKEN = config("LONG_LIVED_ACCESS_TOKEN")
SHORT_TOKEN = 'a'