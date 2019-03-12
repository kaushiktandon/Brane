# -*- coding: utf-8 -*-

import json
import csv
import sys
import codecs

reload(sys)
sys.setdefaultencoding('utf8')
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

links_json = "C:\\Users\\kaush\\Downloads\\export20190209c02\\export20190209c02\\dump\\nodes_categorizations_3a669ba138278690dc04dac6a777abe3.data.json"
full_links_file = 'new_links.csv'

output_file = 'still_missing.csv'
class Link:
	def __init__(self,link1,link2):
		self.link1 = link1
		self.link2 = link2

def load_links(links_file):
	links = dict()
	with open(links_file) as f:
		for line in f:

			data = json.loads(line)
			from_ = str(data['data']['_from'])[6:]
			to_ = str(data['data']['_to'])[6:]
			if(links.get(from_) == None):
				links[from_] = [to_]
			else:
				links[from_].append(to_)
			#links.append(Link(from_,to_))
	print("Loaded links")
	return links

def main():
	links = load_links(links_json)
	length = 786116
	with open(full_links_file, 'r+') as f:
		with open(output_file, 'w+') as csvfile:
			writer1 = csv.writer(csvfile,lineterminator = '\n')
			reader = csv.reader(f)
			counter = 0
			for row in reader:
				if(len(row) != 5):
					continue
				counter = counter + 1
				if(counter % 3000 == 0):
					print(counter * 100.0 / length)
				new_from = str(row[1])
				new_to = str(row[2])
				if(links.get(new_from) == None):
					writer1.writerow(['CL',new_from,new_to,row[3],row[4]])
				elif(new_to not in links.get(new_from)):
					writer1.writerow(['CL',new_from,new_to,row[3],row[4]])					

if __name__ == '__main__':
	main()