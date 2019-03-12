# -*- coding: utf-8 -*-

import sys
import codecs
import csv
import time
import json

reload(sys)
sys.setdefaultencoding('utf8')
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

#Convert 1 -> name -> database ID


authors_file = 'authors1.csv'
publications_files = ['publications1.csv']
others_file = 'OtherNodes.csv'
links_file = 'new_links.csv'

nodes_json_file = "C:\\Users\\kaush\\Downloads\\export20190209c02\\export20190209c02\\dump\\nodes_ca15fd43dfaeb80eb8c125735e0479b0.data.json"
links_json_file = "C:\\Users\\kaush\\Downloads\\export20190209c02\\export20190209c02\\dump\\nodes_categorizations_3a669ba138278690dc04dac6a777abe3.data.json"

output_file = "new_links_a.csv"
missed_file = "missing_a.csv"

class Link:
	def __init__(self,link1,link2):
		self.link1 = link1
		self.link2 = link2

def load_nodes(nodes_file):
	nodes = dict()
	with open(nodes_file) as f:
		for line in f:
			data = json.loads(line)
			#print data[i]
			#a_id = str(data[i][0])
			#name = str(data[i][1])

			a_id = str(data['data']['_key'])
			name = str(data['data']['t'])
			nodes[name] = a_id;
	print("Loaded nodes")
	return nodes
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

def load_tempID_name_pairs(fileName):
	pairs = dict()
	with open(fileName,'r+') as f:
		reader = csv.reader(f)
		for row in reader:
			if len(row) < 3:
				continue
			ID = str(row[1])
			name = str(row[2])
			pairs[ID] = name
	print("Loaded " + fileName)
	return pairs
def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z
def linkExists(id1,id2, links):
	if(links.get(id1) == None):
		print(id1)
		return False
	for id in links.get(id1):
		if id == id2:
			return True
			print id1, id2
	return False

def main():
	authors_nodes = load_tempID_name_pairs(authors_file)
	publications_nodes = dict()
	for publications_file in publications_files:
		temp_pubs = load_tempID_name_pairs(publications_file)
		publications_nodes = merge_two_dicts(publications_nodes, temp_pubs)

	other_nodes = load_tempID_name_pairs(others_file)

	database_nodes = load_nodes(nodes_json_file)
	links = load_links(links_json_file,authors_nodes,publications_nodes,other_nodes,database_nodes)
	counter = 0
	rowsWritten = 0
	z = 0
	with open(output_file, 'w+') as csvfile1:
		writer1 = csv.writer(csvfile1,lineterminator = '\n')
		with open(missed_file, 'w+') as csvfile2:
			writer2 = csv.writer(csvfile2,lineterminator='\n')
			with open(links_file,'r+') as f:
				reader = csv.reader(f)
				length = 786116#sum(1 for row in reader)
				for row in reader:
					z = z + 1
					if(z % 3000 == 0):
						print(z * 100.0/ length)
					if(len(row)) < 5:
						continue
					id_1 = str(row[1])
					id_2 = str(row[2])
					if(linkExists(id_1,id_2, links)):
						continue
					if(int(id_1) > 8000000):
						new_id1 = str(id_1)
					elif(authors_nodes.get(str(id_1)) != None):
						new_id1 = database_nodes.get(authors_nodes[id_1])
					elif(other_nodes.get(str(id_1)) != None):
						new_id1 = database_nodes.get(other_nodes[id_1])
					elif(publications_nodes.get(str(id_1)) != None):
						new_id1 = database_nodes.get(publications_nodes[id_1].replace('"','""'))
					else:
						new_id1 = None

					if(int(id_2) > 8000000):
						new_id2 = str(id_2)
					elif(authors_nodes.get(str(id_2)) != None):
						new_id2 = database_nodes.get(authors_nodes[id_2])
					elif(other_nodes.get(str(id_2)) != None):
						new_id2 = database_nodes.get(other_nodes[id_2])
					elif(publications_nodes.get(str(id_2)) != None):
						publication_name = publications_nodes.get(str(id_2))

						if(publication_name[-1] == '"' and ';' not in publication_name):
							new_publication_name = publication_name.replace('"','""')
						elif(publication_name[0] == '"' and ';' not in publication_name):
							new_publication_name = publication_name.replace('"','""')
						elif(';' in publication_name):
							new_publication_name = '"' + publication_name[:publication_name.find(';')]
						else:
							new_publication_name = publication_name[0] + publication_name[1:-1].replace('"','""') + publication_name[-1]

						if('""' in new_publication_name):
							new_publication_name = '"' + new_publication_name + '"'
							#print publication_name, new_publication_name, database_nodes.get(publication_name), database_nodes.get(new_publication_name)
						
						new_id2 = database_nodes.get(new_publication_name)
					else:
						new_id2 = None

					if(new_id1 == None or new_id2 == None):
						counter = counter + 1  #+ " ERROR: " + new_id1 + " " + new_id2
						writer2.writerow(row)
						#writer1.writerow(['CL',str(id_1),str(id_2),row[3],row[4]])
					else:
						writer1.writerow(['CL',str(new_id1),str(new_id2),row[3],row[4]])
						rowsWritten = rowsWritten + 1
	print(str(counter))
	print(str(rowsWritten))

if __name__ == '__main__':
	main()