import csv
import requests
from BeautifulSoup import *
import sys
import json

reload(sys)
sys.setdefaultencoding('utf8')
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

merged_file = '../merge_nodes/new_merged_converted.csv'
new_links_file = '3_gram_full.csv'
nodes_file = '../merge_nodes/nodes_ca15fd43dfaeb80eb8c125735e0479b0.data.json'

output_file = '3_gram_full_v1.csv'
output_file2 = "3_gram_full_v1_with_names.csv"

def load_nodesJSON(nodes_file):
	nodes = dict()
	print ("Loading nodes")
	with open(nodes_file) as f:
		for line in f:
			data = json.loads(line)
			a_id = str(data['data']['_key'])
			name = str(data['data']['t'])
			if(name == ' '):
				continue
			nodes[a_id] = name
	print ("Loaded nodes")
	return nodes

def load_merged(merged_file):
	merged = list()
	with open(merged_file) as f:
		reader = csv.reader(f)
		for row in reader:
			if(len(row) >= 1):
				id1 = str(row[0].split(';')[1])
				id2 = str(row[0].split(';')[2])
				merged.append(id2)
	return merged


def main():
	nodes = load_nodesJSON(nodes_file)
	merged_nodes = load_merged(merged_file)
	with open(output_file, 'w+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		with open(output_file2, 'w+') as csvfile2:
			writer2 = csv.writer(csvfile2,lineterminator = '\n')
			with open(new_links_file, 'r+') as f:
				reader = csv.reader(f)
				for row in reader:
					if(len(row) == 5):
						id_1 = str(row[1])
						id_2 = str(row[2])
						if id_1 in merged_nodes or id_2 in merged_nodes:
							continue
						writer.writerow(row)
						name1 = nodes.get(id_1)
						name2 = nodes.get(id_2)
						writer2.writerow(['CL',str(id_1),str(id_2),'is related to', 'is related to', name1, name2])


if __name__ == '__main__':
	main()