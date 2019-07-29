import pymongo
from bson.json_util import dumps

client = pymongo.MongoClient("mongodb+srv://karin:Afeq1012@cluster0-ub2ti.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
podcasts_col = db.podcasts
# dumps(podcast)


# returning range of podcast the answering the query
def get_podcasts_by_keyword(keywork):
    return podcasts_col.find({'$text': {'$search': keywork}})


