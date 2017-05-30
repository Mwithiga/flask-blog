#sql.py - create an SQLite3 table and populate it with data

import sqlite3

#create a new database if the database is not available

with sqlite3.connect("blog.db") as connection:
	#get a cursor used to exceute SQL commands

	c = connection.cursor()

	#create the table

	c.execute("""CREATE TABLE posts
	            (title TEXT, post TEXT)
	           """)
	#insert Dummy data into the table

	c.execute('INSERT INTO posts VALUES("GOOD","I\'m good.")')
	c.execute('INSERT INTO posts VALUES("WELL","I\'m well.")')
	c.execute('INSERT INTO posts VALUES("EXCELENT","I\'m excllent.")')
	c.execute('INSERT INTO posts VALUES("GUCCI","I\'m okay.")')
