import pymongo
from bson.json_util import dumps

client = pymongo.MongoClient("mongodb+srv://karin:Afeq1012@cluster0-ub2ti.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
podcasts_col = db.podcasts
# dumps(podcast)


# returning range of podcast the answering the query
def get_podcasts_by_keyword(keywork):
    keywork = ".*"+keywork+".*"
    # yield podcasts_col.find({'$text': {'$search': keywork}})
    # # yield podcasts_col.find( { "episodes": { '$or': [ { title: keywork }, { desc: keywork } ] } )
    # yield podcasts_col.find( { "episodes": { '$or' : [ { 'title': keywork }, { 'desc': keywork } ] }})
    return podcasts_col.find( {"$or":[{ 'episodes.title':  {'$regex': keywork}},
                                      { 'episodes.desc':  {'$regex': keywork}},
                                      { 'desc':  {'$regex': keywork}},
                                      { 'name':  {'$regex': keywork}}] })

