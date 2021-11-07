from flask import Flask
from markupsafe import escape
from flask import render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    return render_template('search.html')
