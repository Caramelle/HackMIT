import urllib2
import json 
from key import api_key

def getClass(anger,disgust,fear,sadness,joy,analytical,confident,tentative,openess,conscientiousness,extraversion,agreeableness,emotionalRange,actor,director,genre,age,runtime):
    data =  {

            "Inputs": {

                    "input1":
                    {
                        "ColumnNames": ["title", "anger", "disgust", "fear", "joy", "sadness", "analytical", "confident", "tentative", "openess", "conscientiousness", "extraversion", "agreeableness", "emotionalRange", "rating", "actor", "director", "genre", "age", "runtime"],
                        "Values": [ [ "title", anger, disgust, fear, joy, sadness, analytical, confident, tentative, openess, conscientiousness, extraversion, agreeableness, emotionalRange, 0, actor, director, genre, age, runtime ] ]
                    },        },
                "GlobalParameters": {
    }
        }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/e998d9efb75c4bb9942afc8a2a906d07/services/d444694bd7a84b7daff40eb12c53a5af/execute?api-version=2.0&details=true'

    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib2.Request(url, body, headers) 

    try:
        response = urllib2.urlopen(req)

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers) 
        # response = urllib.request.urlopen(req)

        result = response.read()
        #returns data as [p(0),p(1),predicted class]
        return json.loads(result)['Results']['output1']['value']['Values'][0][-3:]
    except urllib2.HTTPError, error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())

        print(json.loads(error.read()))                 

