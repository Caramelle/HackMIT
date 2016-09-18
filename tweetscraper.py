# coding: utf-8
import tweepy
import json

auth = tweepy.OAuthHandler("qLUhXHEaJxt8hn6SUhrTlNYaj", "2oZPOvHAy0vAi9gwEBgNX4W0xgx4SUzIjabgBa2UsIh8ZtSqmO")
auth.set_access_token("455064135-Xq71sKiQQUqBP7fWDWfjSqczQz1kTJwUhcy5T5Fs", "rGt7lms4cXFfJ2n7K3psUOGgeAGQkeSScwgLgzm2qliFF")

api = tweepy.API(auth)

searchText = "titanic"
searchNumber = "10"
movie_tweets = api.search(searchText, rpp=searchNumber)

for tweet in movie_tweets:
	if "http" in tweet.text:
		ok = 1
	else:
		print tweet.text + '\n'
































































