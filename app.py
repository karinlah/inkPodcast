from flask import Flask
app = Flask(__name__)


################################################################################
# BASIC
################################################################################

'''
TODO
'''
@app.route('/')
def default():
	return 'This is the default, try adding some parameters'

'''
TODO
'''
@app.route('/search/<keywords>')
def search(keywords):
	'''
	Format for keywords is flexible so long as you specify the keyword delimiter 
	that's passed in the http request
	In published API, should specify and set the delimiter as a constant

	Returns a dictionary in the format {'keywords': ['list', 'of', 'keywords']}

	FOR LATER: Going to run into a problem with searching for phrases....
	'''
	keywords_dict = parse_keywords_for_db(keywords, keywords_delimiter=';')
	return keywords_dict


################################################################################
# GET
################################################################################

'''
TODO
'''
@app.route('/get/trans')
def get_trans():
	raise NotImplemented
	return -1

'''
TODO
'''
@app.route('/get/tags')
def get_tags():
	raise NotImplemented
	return -1

'''
TODO
'''
@app.route('/get/episode/show_notes')
def get_episode_show_notes():
	raise NotImplemented
	return -1

'''
TODO
'''
@app.route('/get/podcast/host')
def get_podcast_host():
	raise NotImplemented
	return -1

'''
TODO
'''
@app.route('/get/podcast/copyright')
def get_podcast_copyright():
	raise NotImplemented
	return -1

'''
TODO
'''
@app.route('/get/podcast/name')
def get_podcast_name():
	raise NotImplemented
	return -1

'''
TODO
'''
@app.route('/get/podcast/email')
def get_podcast_email():
	raise NotImplemented
	return -1

'''
TODO
'''
@app.route('/get/podcast/episodes')
def get_podcast_episodes():
	raise NotImplemented
	return -1

'''
TODO
'''
@app.route('/get/episode')
def get_episode():
	raise NotImplemented
	return -1

'''
TODO
'''
@app.route('/get/episode/description')
def get_episode_description():
	raise NotImplemented
	return -1

'''
TODO
'''
@app.route('/get/episode/duration')
def get_episode_duration():
	raise NotImplemented
	return -1

'''
TODO
'''
@app.route('/get/episode/pub')
def get_episode_pub():
	raise NotImplemented
	return -1

'''
TODO
'''
@app.route('/get/episode/image')
def get_episode_image():
	raise NotImplemented
	return -1

'''
TODO
'''
@app.route('/get/episode/mp3')
def get_episode_mp3():
	raise NotImplemented
	return -1



################################################################################
# SET 
################################################################################

'''
TODO
'''
@app.route('/set/tags')
def set_tags():
	raise NotImplemented
	return -1

'''
TODO
'''
@app.route('/set/tags/add')
def add_tags():
	raise NotImplemented
	return -1


################################################################################
# FUNCTIONS FOR DEALING WITH DB 
################################################################################

def parse_keywords_for_db(keywords, keywords_delimiter):
	assert 'keywords=' in keywords, 'Keywords not found in HTTP request'
	values = keywords.split('=')[1]
	keywords_dict = {}
	keywords_dict['keywords'] = [word for word in values.split(keywords_delimiter)]
	return keywords_dict


if __name__ == '__main__':
	app.debug = True
	app.run()
