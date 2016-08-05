from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import psycopg2
#from redis import StrictRedis

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
#        self.redis = StrictRedis()

    def process(self, tup):
        word = tup.values[0]

        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount
        # Table name: Tweetwordcount
        # you need to create both the database and the table in advance.
        conn = psycopg2.connect(database="Tcount", user="postgres", password="12345", host="localhost", port="5432")

        #Rather than executing a whole query at once, it is better to set up a cursor that encapsulates the query,
        #and then read the query result a few rows at a time. One reason for doing this is
        #to avoid memory overrun when the result contains a large number of rows.

        cur = conn.cursor()
        cur.execute("select * from tweetwordcount where word = '%s'" % word)
        results = len(cur.fetchall())
        if results > 0:
               cur.execute("UPDATE tweetwordcount SET count = %s where word = %s", (self.counts[word], word))
	if results == 0:
               cur.execute("INSERT INTO tweetwordcount (word,count) VALUES ('%s', 1)" % word)

        conn.commit()
        conn.close()



        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))

