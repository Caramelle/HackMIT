# coding: utf-8
import tweepy
import json

auth = tweepy.OAuthHandler("SFp7wv96ak2R1UxtPrAg5pKwY", "0shnNX1DfrBgVNwHaCLQlSfWZAHAUrije1bSR3KXsS5ZmpHhe6")
auth.set_access_token("455064135-Xq71sKiQQUqBP7fWDWfjSqczQz1kTJwUhcy5T5Fs", "rGt7lms4cXFfJ2n7K3psUOGgeAGQkeSScwgLgzm2qliFF")

api = tweepy.API(auth)

searchText = "barbie"
searchNumber = "10"
movie_tweets = api.search(searchText, rpp=searchNumber)

tweets = "";

for tweet in movie_tweets:
	if "http" in tweet.text:
		ok = 1
	else:
		tweets += tweet.text

































































