#!/usr/bin/python2.4

import psycopg2
import sys


#function queries database based on the two numbers passed through
def getRange(connection,min,max):
        cur = connection.cursor()
        cur.execute("select * from tweetwordcount where count >= '%s' and count <= '%s' order by count asc" % (min, max))
        results = cur.fetchall()

        conn.commit()
        conn.close()

	return results




###main program

#establishing connection
try:
	conn = psycopg2.connect(database="Tcount", user="postgres", password="12345", host="localhost", port="5432")
except:
        print "Could not connect to database."

#queries and prints data based on ranges given
try:
	inputArr = sys.argv[1].split(',')
	minNum = inputArr[0]
	maxNum = inputArr[1]
	results = getRange(conn,minNum,maxNum)
	if len(results) > 0:
		for item in results:
			print ("%s: %s" % (item[0],item[1]))
	if len(results) == 0:
		print "There are no entries that fall within this range."

except:
        print "Please enter a range."
