import tweepy

print("this is my twitter bot")

CONSUMER_KEY = 'qONkRYulgiGT3go3uKlhu0l7a'
CONSUMER_SECRET = 'SlVMrASGJiRuUok6To4NoFEWaxAHxDgcYONhHpX3doav9nYeSD'
ACCESS_KEY = '1508946544862670855-FG2FtgH6lOg7zTtIeYwVgzgWxJ30I9'
ACCESS_SECRET = 'zjvXUApw3fzkqa2DvurghIAhCULHrLAwbCfw6Ln0Wvl3z'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)