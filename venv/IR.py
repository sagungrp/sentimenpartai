# coding: utf-8
import re
import sys
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob
from pathlib import Path

import pprint

negations = {'tak','bkn','tdk','gak','gk','ga','enggak','tidak','bukan','bukanlah','tidaklah'}
# % of positive tweet
pos = 0
# % of negative tweet
neg = 0
# % of neutral tweet
net = 0

class TwitterClient(object): 
	''' 
	Generic Twitter Class for sentiment analysis. 
	'''
	
	def __init__(self): 
		''' 
		Class constructor or initialization method. 
		'''
		# keys and tokens from the Twitter Dev Console 
		consumer_key = 'ICxjRfEpvDm8XZWl2bBA6MbTj'
		consumer_secret = 'qm5kdAjHLjSVNBoclAlzPVPAyJPTXmEhwCUdJixvdll5CmqRVz'
		access_token = '1070195239707586560-wjbg5Rog9s8MX0ZuImdBXe0BUCLflQ'
		access_token_secret = 'HVbRVALs3iwqSQKQ5k3QkLN4mms5GMd9AgVIa3H0kHxAg'
		
		p = open("positive.txt", "r")
		self.positiveWords = set(p.read().splitlines())
		p = open("negative.txt", "r")
		self.negativeWords = set(p.read().splitlines())

		self.oppositeConjWords = {'tapi', 'tetapi', 'namun'}

		# attempt authentication 
		try: 
			# create OAuthHandler object 
			self.auth = OAuthHandler(consumer_key, consumer_secret) 
			# set access token and secret 
			self.auth.set_access_token(access_token, access_token_secret) 
			# create tweepy API object to fetch tweets 
			self.api = tweepy.API(self.auth) 
		except: 
			print("Error: Authentication Failed") 

		

	def clean_tweet(self, tweet): 
		''' 
		Utility function to clean tweet text by removing links, special characters 
		using simple regex statements. 
		'''
		tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
		#Convert to lower case
		tweet = tweet.lower()
		#Convert www.* or https?://* to URL
		tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
		#Remove additional white spaces
		tweet = re.sub('[\s]+', ' ', tweet)
		#Replace #word with word
		tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
		#Delete @username
		tweet = re.sub('@[^\s]+','', tweet)
		#trim
		tweet = tweet.strip('\'"')
		#Delete reiterant letters
		tweet = re.sub(r'([a-z])\1+', r'\1', tweet)
		#Remove single-letter words
		tweet = ' '.join( [w for w in tweet.split() if len(w)>1] )
		return tweet

	def get_tweet_sentiment(self, tweet): 
		''' 
		Utility function to classify sentiment of passed tweet 
		using textblob's sentiment method 
		'''
		positiveScore = 0
		negativeScore = 0
		oppositeSentimentScore = 0
		totalScore = 0
		NEGATION_WEIGHT = 2
		OPPOSITE_CONJUNCTION_WEIGHT = -1

		tweet = self.clean_tweet(tweet)
		
		words = tweet.split()

		#  1. Analyze negation word window — first pass
		for idx, word in enumerate(words):
			if word in negations:
				j = 0
				while j != 2 and idx+j < len(words):
					if words[idx+j] in self.positiveWords:
						positiveScore -= NEGATION_WEIGHT
					if words[idx+j] in self.negativeWords:
						negativeScore -= NEGATION_WEIGHT
					j += 1

		#  2. Calculate sentiment rank of separate words — second pass
		for idx, word in enumerate(words):
			if word in self.positiveWords:
				positiveScore += 1
			if word in self.negativeWords:
				negativeScore += 2

		#  3. Global view of a sentence for handling opposite conjunctions — third pass 
		for idx, word in enumerate(words):
			sentimentCount = 0

			if word in self.positiveWords:
				sentimentCount += 1
			if word in self.negativeWords:
				sentimentCount -= 1
			if word in self.oppositeConjWords:
				oppositeSentimentScore = OPPOSITE_CONJUNCTION_WEIGHT * sentimentCount / 2
		
		totalScore = positiveScore - negativeScore + oppositeSentimentScore

		# create TextBlob object of passed tweet text 
		# analysis = TextBlob(tweet) 
		# set sentiment 
		if totalScore > 0: 
			return 'positive'
		elif totalScore == 0: 
			return 'neutral'
		else: 
			return 'negative'

	def get_tweets(self, query, count = 1000): 
		''' 
		Main function to fetch tweets and parse them. 
		'''
		# empty list to store parsed tweets 
		tweets = [] 

		try: 
			# call twitter api to fetch tweets 
			fetched_tweets = self.api.search(q = query, count = count) 

			# parsing tweets one by one 
			for tweet in fetched_tweets: 
				# empty dictionary to store required params of a tweet 
				parsed_tweet = {} 

				# saving text of tweet 
				parsed_tweet['text'] = tweet.text.encode('UTF-8')
				# saving sentiment of tweet 
				parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) 

				# appending parsed tweet to tweets list 
				if tweet.retweet_count > 0: 
					# if tweet has retweets, ensure that it is appended only once 
					if parsed_tweet not in tweets: 
						tweets.append(parsed_tweet) 
				else: 
					tweets.append(parsed_tweet) 

			# return parsed tweets 
			return tweets 

		except tweepy.TweepError as e: 
			# print error (if any) 
			print("Error : " + str(e)) 

def main(partai, get): 
	# creating object of TwitterClient Class
	api = TwitterClient() 
	# calling function to get tweets
	tweets = api.get_tweets(query = partai, count = 1000)
	result = ""

	# picking positive tweets from tweets 
	ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
	
	# percentage of positive tweets 
	result+="<h3>"+("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))+"</h3>"
	pos = (100*len(ptweets)/len(tweets))
	
	# picking negative tweets from tweets 
	ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
	
	# percentage of negative tweets
	result+="<h3>"+("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))+"</h3>"
	neg = (100*len(ntweets)/len(tweets))
	
	# percentage of neutral tweets
	result+="<h3>"+("Neutral tweets percentage: {} %".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))+"</h3>" + "<br/>"
	net = (100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets))
	
	# printing first 5 positive tweets 
	result+=("<h3>Positive tweets:</h3>") + "<br/>"
	for tweet in ptweets[:10]: 
		result+=str(tweet['text']) + "<br/><br/>"

	# printing first 5 negative tweets 
	result+=("<h3>Negative tweets:</h3>") + "<br/>"
	for tweet in ntweets[:10]: 
		result+=str(tweet['text']) + "<br/><br/>"
	
	if get == "pos":
		return pos
	elif get == "neg":
		return neg
	elif get == "net":
		return net
	else:
		return(str(result))

	#pp = pprint.PrettyPrinter(indent=4)
	#pp.pprint(ptweets)

	
if __name__ == "__main__": 
	# calling main function 
	main() 