import csv
import requests
import sys
import json
import codecs
import pandas as pd
import sqlite3
from sqlite3 import Error
import operator
import time

reload(sys)
sys.setdefaultencoding('utf8')
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

database = 'links.db'

#only run if need to recreate table
def deleteTable():
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute("DROP TABLE data")
		conn.commit()
	except Error as e:
		print(e)
	finally:
		conn.close()
def loadDatabase(links_file):
	link_ids = dict()
	uptexts = dict()
	downtexts = dict()
	print("Loading links")
	#deleteTable()
	with open(links_file,'r+') as f:

		#sql = sqlite3.connect(str(database))
		#cur = sql.cursor()
		#Create the data table
		#cur.execute('''CREATE TABLE IF NOT EXISTS data(link1 TEXT, link2 TEXT, link_id TEXT, uptext TEXT, downtext TEXT)''')

		numRows = 0
		for line in f:
			data = json.loads(line)
			key1 = str(data['data']['_from'])
			id_1 = key1[6:]
			key2 = str(data['data']['_to'])
			id_2 = key2[6:]
			key3 = str(data['data']['_key'])
			uptext = data['data'].get('u')
			downtext = data['data'].get('d')
			if(uptext != None):
				uptext = str(uptext)

			if(downtext != None):
				downtext = str(downtext)

			#cur.execute('''INSERT INTO data VALUES(?,?,?,?,?)''',(id_1,id_2,key3,uptext,downtext))
			if((id_1,id_2) not in link_ids):
				link_ids[id_1,id_2] = 1
				numRows = numRows + 1
			else:
				link_ids[id_1,id_2] = link_ids[id_1,id_2] + 1
				uptexts[id_1,id_2] = uptext
				downtexts[id_1,id_2] = downtext
		f.close()
		#sql.commit()
		#sql.close()
	print("Loaded Links")
	return numRows, link_ids, uptexts, downtexts
def load_nodesJSON(nodes_file):
	nodes = dict()
	print ("Loading nodes")
	with open(nodes_file) as f:
		for line in f:
			data = json.loads(line)
			a_id = str(data['data']['_key'])
			name = str(data['data']['t'])
			nodes[a_id] = name
	print ("Loaded nodes")
	return nodes

if __name__ == '__main__':
	if(len(sys.argv) != 4):
		print("USAGE: python new_delete_links.py [Input JSON Nodes File] [Input JSON Links File] [Name of output csv file]")
		print("If there is a space in any of the files, put the name in quotes \"[NAME]\" ")
		print("Example: python link_recursion.py nodes.json \"All links.json\" output.csv ")
	else:
		nodes_file = sys.argv[1]
		links_file = sys.argv[2]#'All links.json'
		created_CSV_file = sys.argv[3]#'output_All deleted.csv'

		count = 0.0
		startTime = time.time()
		nodes = load_nodesJSON(nodes_file)
		length, link_ids, uptexts, downtexts = loadDatabase(links_file)
		dbTime = time.time()
		with open(created_CSV_file, 'w+') as csvfile:
			writer = csv.writer(csvfile,lineterminator = '\n')
			sql = sqlite3.connect(str(database))
			cur = sql.cursor()
			for keyPair, value in link_ids.iteritems():
				count = count + 1
				if (count % 3000 == 0):
					print (count * 100 / length, '%')
			
				if(value == 1): continue
				
				#print keyPair
				writer.writerow(['DL',keyPair[0],keyPair[1]])
				uptext = uptexts[keyPair]
				downtext = downtexts[keyPair]
				if(nodes.get(str(keyPair[1])) != None and nodes.get(str(keyPair[0])) != None):
					if(uptext == None and downtext == None):
						writer.writerow(['CL',keyPair[0],keyPair[1]])
					else:
						writer.writerow(['CL',keyPair[0],keyPair[1],uptext,downtext])
		endTime = time.time()
		print(str(endTime - startTime) + " seconds to run. ")
		print(str(dbTime - startTime)  + " seconds to load db. ")
		print(str(endTime - dbTime) + " seconds to find duplicates. ")