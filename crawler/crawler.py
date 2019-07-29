
def insert_podcast(rssfeed):
    import feedparser
    d = feedparser.parse(rssfeed)
    import pymongo

    client = pymongo.MongoClient(
        "mongodb+srv://karin:Afeq1012"
        "@cluster0-ub2ti.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test
    mycol = db['podcasts']
    if not 'title' in d['feed']:
        return
    print(d['feed']['title'])
    myquery = {"name": d['feed']['title']}
    mydoc = mycol.find(myquery)
    fits = [x for x in mydoc]
    if not len(fits):
        temp_pod = {'name': d['feed']['title'],
                    'author': d['feed']['author'],
                    'desc': d['feed']['description'],
                    'episods': [
                        {'link': d['entries'][i]['link'], 'title': d['entries'][i]['title'],
                         'desc': d['entries'][i]['description']} for i in range(min(10,len(d['entries'])))]}
        mycol.insert_one(temp_pod)

def get_rss_feeds(html_file,rss_file):
    with open(html_file,'r') as g:
        f=open(rss_file,'a')
        import re
        pattern = re.compile("a href=\"[^\"]*rss.xml\"")

        for i, line in enumerate(g):
            for match in re.finditer(pattern, line):
                # print(match.group()[8:-1])
                f.write(match.group()[8:-1]+'\n')
def insert_podcasts(rss_file):
    with open(rss_file,'r') as f:
        for line in f.readlines():
            # print(line.strip())
            insert_podcast(line.strip())
            pass
def main():
    insert_podcasts('podcastrss.txt')
    # get_rss_feeds('Top 50 BBC Podcasts in Google Reader.html','podcastrss.txt')
    #     # text = g.read()
if __name__ == '__main__':
    main()