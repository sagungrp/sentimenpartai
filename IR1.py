import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key = 'ICxjRfEpvDm8XZWl2bBA6MbTj'
consumer_secret = 'qm5kdAjHLjSVNBoclAlzPVPAyJPTXmEhwCUdJixvdll5CmqRVz'
access_token = '1070195239707586560-wjbg5Rog9s8MX0ZuImdBXe0BUCLflQ'
access_token_secret = 'HVbRVALs3iwqSQKQ5k3QkLN4mms5GMd9AgVIa3H0kHxAg'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 2 - Retrieve Tweets
public_tweets = api.search('2019gantipresiden')

for tweet in public_tweets:
    #Step 3 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
 