from flask import *
import os
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('base.html')