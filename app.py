from flask import Flask, request
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
@app.route('/search')
def search():
	# URL formatted as /search?keywords=['kw1','kw2'] --> returns the list of keywords
	return request.args.get('keywords')


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



if __name__ == '__main__':
	app.debug = True
	app.run()
