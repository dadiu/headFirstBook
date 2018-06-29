from flask import Flask
from vsearch import search4letters

app = Flask(__name__)


@app.route('/')
def hello()->str:
    return 'Hello Word'


@app.route('/search4')
def do_search()->str:
    return str(search4letters(
        phrase='lift, the univers, and everything',
        letters='eiru,!'
    ))


app.run()
