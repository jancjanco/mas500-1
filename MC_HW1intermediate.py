import mediacloud, datetime
import logging
import unittest


logging.basicConfig(filename="DebugFile.log", filemode = 'w', level=logging.INFO)

def callMediaCloud():
	API_File = open('MC_ApiKey.txt','r')
	API_KEY = API_File.read()tg bg b

	mc = mediacloud.api.MediaCloud(API_KEY)

	logging.info ('Woohoo, we have a connection!')

	res = mc.sentenceCount('(spooky AND action AND distance)', solr_filter=[mc.publish_date_query( datetime.date( 2015, 10, 20), datetime.date( 2015, 11, 18) ), 'media_sets_id:1' ])
	logging.info ('Logging: Spooky Action at a Distance')

	return res


res = callMediaCloud()
print "Count of (spooky AND action AND distance) occurences:", res['count'] #prints count of sentences that reference (spooky, action, distance)

   
#ran successfully. Count of (spooky AND action AND distance) occurences: 24