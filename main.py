from flask import *
import os
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')
@app.route("/instagram")
def instagram():
    return render_template('instagram.html')
@app.route("/facebook")
def facebook():
    return render_template('facebook.html')
@app.route("/twitter")
def twitter():
    return render_template('twitter.html')
@app.route("/fakenews")
def fakenews():
    return render_template('fakenews.html')
@app.route("/about")
def about():
    return render_template('about.html')