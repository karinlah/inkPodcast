from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


# searching in title, descritopn and tras
@app.route('/smart_search')
def smart_search():
    return "Hello World!"


@app.route('/tags/get')
def get_tags():
    return "Hello World!"


@app.route('/tags/add')
def add_tags():
    return "Hello World!"


if __name__ == '__main__':
    app.run()
