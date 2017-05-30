# imports
from flask import  Flask, render_template, request, session, flash,redirect, url_for, g

import sqlite3

#configuration
DATABASE = 'blog.py'

app = Flask(__name__)

#Pulls in app configuration by looking for UPPERCASE variables

app.config.from_object(__name__)

#function used for connecting to the database

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

#add the two views
@app.route('/')
def login():
	return render_template('login.html')

@app.route('/main')
def main():
	return render_template('main.html')

if __name__ =='__main__':
	app.run(debug=True)