from connect import fire
from azure import getClass

#pushes a json item to the db
def push(item, db=fire):
    return db.push(item)

def get(db=fire):
    return db.get()

def write_to_db(title, anger, disgust, fear, joy, sadness, analytical, confident, tentative, openess, conscientiousness, extraversion, agreeableness, emotionalRange, actor, director, genre, age, runtime):
    po, pi, good = getClass(anger, disgust, fear,sadness, joy, analytical, confident, tentative, openess, conscientiousness, extraversion, agreeableness, emotionalRange, actor, director, genre, age, runtime)
    out = {
            "title":title,
            "p0":po,
            "p1":pi,
            "good":good,
            "anger":anger,
            "disgust":disgust,
            "fear":fear,
            "sadness":sadness,
            "joy":joy
            }

    push(out)
