import pymongo
from bson.json_util import dumps

client = pymongo.MongoClient("mongodb+srv://karin:Afeq1012@cluster0-ub2ti.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
podcasts_col = db.podcasts
# dumps(podcast)


# returning range of podcast the answering the query
def get_podcasts_by_keyword(keywork):
    return podcasts_col.find({'$text': {'$search': keywork}})

def get_mp3_for_podcast(podcast_name, episode_name, output_file):
    pod = podcasts_col.find({'name': podcast_name}).next()
    url = ""
    for episode in pod['episodes']:
        if episode["title"] == episode_name:
            url = episode['link']

    if url =="":
        return
    import wget
    wget.download(url, 'temp.html')
    with open('temp.html', 'r') as g:
        import re
        pattern = re.compile("href=\"[^\"]*\.mp3\"")

        for i, line in enumerate(g):
            for match in re.finditer(pattern, line):
                # print(match.group()[8:-1])
                wget.download("https:"+match.group()[6:-1], output_file)
    import os
    os.remove("temp.html")