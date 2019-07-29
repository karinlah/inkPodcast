# mongodb+srv://karin:<password>@cluster0-ub2ti.mongodb.net/test?retryWrites=true&w=majority
import pymongo
from bson.json_util import dumps

client = pymongo.MongoClient("mongodb+srv://karin:Afeq1012@cluster0-ub2ti.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
podcasts = db.podcasts
# dumps(podcast)
