from connect import fire

#pushes a json item to the db
def push(item, db=fire):
    return db.push(item)

def get(db=fire):
    return db.get()
