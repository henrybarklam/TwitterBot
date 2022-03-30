import tweepy
import time

mango_counter = 1

CONSUMER_KEY = 'qONkRYulgiGT3go3uKlhu0l7a'
CONSUMER_SECRET = 'SlVMrASGJiRuUok6To4NoFEWaxAHxDgcYONhHpX3doav9nYeSD'
ACCESS_KEY = '1508946544862670855-FG2FtgH6lOg7zTtIeYwVgzgWxJ30I9'
ACCESS_SECRET = 'zjvXUApw3fzkqa2DvurghIAhCULHrLAwbCfw6Ln0Wvl3z'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


# for mention in mentions:
#     print(mentions[0].id)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

# mentions = api.mentions_timeline()
# for mention in reversed(mentions):
#         print(str(mention.id) + ' - ' + mention.text)
#         last_seen_id = mention.id
#         store_last_seen_id(last_seen_id, FILE_NAME)
def reply_to_tweets(mango_counter):
    print('retrieving and replying to tweets...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(since_id = last_seen_id, tweet_mode = 'extended')

    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)

        if mention.author.screen_name == 'Little_Shmeet':
            api.update_status('@' + mention.author.screen_name + ' Enjoy your mango, @Little_Shmeet! This is mango number ' + str(mango_counter) + " for you")
            mango_counter += 1

        else:
            api.update_status('@' + mention.author.screen_name + ' Hello to you now! So far, @Little_Shmeet has been reminded about this ' + str(mango_counter) + ' times today! @Little_Shmeet , eat your mango!')
            mango_counter += 1
    return mango_counter
           # # print(mentions[0].__dict__.keys()
    # for mention in mentions:
    #     print(mentions[0].author.screen_name)

while True:
    mango_counter = reply_to_tweets(mango_counter)
    time.sleep(120)
