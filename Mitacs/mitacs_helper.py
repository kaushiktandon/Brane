import requests
import sys
import codecs
import csv
import time
import json

reload(sys)
sys.setdefaultencoding('utf8')
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

nodes_file = 'nodes_ca15fd43dfaeb80eb8c125735e0479b0.data.json'
input_file = 'mitacs_minus_extra.csv'
output_file = 'new_links.csv'


def load_nodesJSON(nodes_file):
	nodes = dict()
	print ("Loading nodes")
	with open(nodes_file) as f:
		for line in f:
			data = json.loads(line)
			a_id = int(data['data']['_key'])
			if(a_id < 91567675):
				continue
			a_id = str(a_id)
			name = str(data['data']['t'])
			if(name == ' '):
				continue
			nodes[name] = a_id
	print ("Loaded nodes")
	return nodes

def main():
	nodes = load_nodesJSON(nodes_file)
	ids_to_check = list()
	with open(input_file,'r+') as f:
		reader = csv.reader(f)
		for row in reader:
			if(len(row) >= 3):
				if("(Project)" in row[2] or "(Sector)" in row[2]):
					continue
				if(row[0] == 'CL' and (row[1] == '10') or (row[1] == '85166882')):
					ids_to_check.append(str(row[2]))

	with open(input_file,'r+') as f:
		with open(output_file, 'w+') as csvfile:
			writer = csv.writer(csvfile,lineterminator = '\n')
			reader = csv.reader(f)
			for row in reader:
				if(len(row) >= 3):
					if("(Project)" in row[2] or "(Sector)" in row[2]):
						continue
					if(row[0] == 'CN' and row[1] in ids_to_check):
						name = row[2]
						new_id = nodes.get(name)
						if(new_id == None):
							print name
						else:
							writer.writerow(['CL',str(new_id),'85294980','is affiliated with', 'is affiliated with'])

if __name__ == '__main__':
	main()

