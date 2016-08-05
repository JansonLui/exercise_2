#!/usr/bin/python2.4

import psycopg2
import sys


#function queries database based on variable passed through
def getCount(connection,word):

        cur = connection.cursor()
        cur.execute("select * from tweetwordcount where word = '%s'" % word)
        results = cur.fetchall()
        conn.commit()
        conn.close()
        return results

#function queries and returns whole table in ascending order
def showAll(connection):

        cur = connection.cursor()
        cur.execute("select * from tweetwordcount order by word asc")
        results = cur.fetchall()
        return results





###main program

#establishing database connection
try:
        conn = psycopg2.connect(database="Tcount", user="postgres", password="12345", host="localhost", port="5432")
except:
        print "Could not connect to database."


#querying and printing data if variable is given
try:
	word = sys.argv[1]
	results = getCount(conn,word)
	if len(results) > 0:
		for item in results:
			print '''Total number of occurences of "%s": %s''' % (item[0], item[1])
	if len(results) == 0:
		print "This word is not in the table."

#printing whole table if a variable is not entered
except:
        results = showAll(conn)
        if len(results) > 0:
                for item in results:
                        print '''Total number of occurences of "%s": %s''' % (item[0], item[1])
        if len(results) == 0:
                print "This table is empty."

