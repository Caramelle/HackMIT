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
    try:
        if float(info['Metascore'])>=60:
            rating+=1
    except:
        pass
    try:
        if float(info['imdbRating'])>=6:
            rating+=1
    except:
        pass
    try:
        if float(info['tomatoRating'])>=6:
            rating+=1
    except:
        pass
    if rating>=2:
        return 1
    else:
        return 0

def getExtra(title):
    info = getInfo(title)
    m=re.match('([^ \t\n\r\v\f,]* [^ \t\n\r\v\f,]*).*', info['Actors'])
    n=re.match('([^ \t\n\r\v\f,]* [^ \t\n\r\v\f,]*).*', info['Director'])
    return m.group(1) + ',' + n.group(1) + ',' + info['Genre'].split(', ')[0] + ',' + info['Rated'] + ',' + info['Runtime'].split(' ')[0]
