import urllib2
import re
import json

def getInfo(title, year=None):
    url = 'http://www.omdbapi.com/?t='+title+'&tomatoes=true'
    if year:
        url+='&y='+year
    url=re.sub(' ','%20',url)
    api = urllib2.urlopen(url)
    info = json.loads(api.read())
    return info

def isGood(title, year=None):
    info = getInfo(title, year)
    rating=0
    if float(info['Metascore'])>=60:
        rating+=1
    if float(info['imdbRating'])>=6:
        rating+=1
    if float(info['tomatoRating'])>=6:
        rating+=1
    return rating>=2
