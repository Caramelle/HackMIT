import json
import csv
import tweepy
from imdb import *
from watson_developer_cloud import ToneAnalyzerV3


tone_analyzer = ToneAnalyzerV3(
    username= "ccfdcb77-1c60-42c6-8195-cd149e3f4a63",
    password= "0TGSUHaFxcpf",
    version="2016-02-11")


auth = tweepy.OAuthHandler("SFp7wv96ak2R1UxtPrAg5pKwY", "0shnNX1DfrBgVNwHaCLQlSfWZAHAUrije1bSR3KXsS5ZmpHhe6")
auth.set_access_token("455064135-Xq71sKiQQUqBP7fWDWfjSqczQz1kTJwUhcy5T5Fs", "rGt7lms4cXFfJ2n7K3psUOGgeAGQkeSScwgLgzm2qliFF")

api = tweepy.API(auth)


with open('movies.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
		movie_tweets = api.search(row, rpp=30)

		tweets = "";


		for tweet in movie_tweets:
			if "http" in tweet.text:
				ok = 1
			else:
				tweets += tweet.text

		if len(tweets) > 0:
			results = json.dumps(tone_analyzer.tone(text=tweets), indent=2)
			data = json.loads(results)


			title = str(row);
			anger = data['document_tone']['tone_categories'][0]['tones'][0]['score']
			disgust = data['document_tone']['tone_categories'][0]['tones'][1]['score']
			fear = data['document_tone']['tone_categories'][0]['tones'][2]['score']
			joy = data['document_tone']['tone_categories'][0]['tones'][3]['score']
			sadness = data['document_tone']['tone_categories'][0]['tones'][4]['score']
			analytical = data['document_tone']['tone_categories'][1]['tones'][0]['score']
			confident = data['document_tone']['tone_categories'][1]['tones'][1]['score']
			tentative = data['document_tone']['tone_categories'][1]['tones'][2]['score']
			openess = data['document_tone']['tone_categories'][2]['tones'][0]['score']
			conscientiousness = data['document_tone']['tone_categories'][2]['tones'][1]['score']
			extraversion = data['document_tone']['tone_categories'][2]['tones'][2]['score']
			agreeableness = data['document_tone']['tone_categories'][2]['tones'][3]['score']
			emotionalRange = data['document_tone']['tone_categories'][2]['tones'][4]['score']
			good = isGood(title)

			if good == 1:
				output = [title, anger, disgust, fear, joy, sadness, analytical, confident, tentative, openess, conscientiousness, extraversion, agreeableness, emotionalRange]

				ofile  = open('scores.csv', "a")
				writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

				writer.writerow(output)

				ofile.close()
