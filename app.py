# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request, redirect
from datetime import datetime
from model import getImageUrlFrom
import os

# -- Initialization section --
app = Flask(__name__)
app.config['GIPHY_KEY'] = os.getenv('GIPHY_KEY')


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', time=datetime.now())

@app.route('/yourgif', methods=['GET', 'POST'])
@app.route('/your-gif', methods=['GET', 'POST'])
def yourgif():
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        userQuery = request.form['interest']
        print(userQuery)
        key = app.config['GIPHY_KEY']
        imageURL = getImageUrlFrom(userQuery, key)
        return render_template('yourgif.html', time=datetime.now(), interest = userQuery, imageURL = imageURL)
