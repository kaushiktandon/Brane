import csv
import sys
import json
import codecs

reload(sys)
sys.setdefaultencoding('utf8')
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

nodes_file = 'nodes_ca15fd43dfaeb80eb8c125735e0479b0.data.json'
output_file = 'merged.csv'

class Node:
	def __init__(self,name,ID,definition):
		self.name = name
		self.ID = ID
		self.definition = definition
def load_nodesJSON(nodes_file):
	nodes = list()
	print ("Loading nodes")
	with open(nodes_file) as f:
		for line in f:

			data = json.loads(line)
			a_id = str(data['data']['_key'])
			name = str(data['data']['t'])
			if(name == ' '):
				continue
			cluster = ""
			if(data['data'].get('cl') != None):
				cluster = str(data['data'].get('cl'))
				if(cluster == "TRUE"):
					continue
			if(data['data'].get('a') == None or data['data']['a'].get('description') == None):
				definition = ""
			else:
				definition = str(data['data']['a']['description'])
			if(definition != "" and definition != " " and definition != "Enter a definition" and definition != "Add a definition"):
				nodes.append(Node(name,a_id,definition))
	print ("Loaded nodes")
	return nodes

def main():
	nodes = load_nodesJSON(nodes_file)
	others = load_nodesJSON(nodes_file)

	count = 0.0
	length = len(nodes) - 700000
	deletedNodes = list()
	with open(output_file, 'w+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		for i in range(length):
			node = nodes[i]
			count = count + 1
			if (count % 50 == 0):
				print (count * 100 / length,count,length, '%')
			if(node.ID in deletedNodes):
				continue
			for j in range(i+1,length):
				other = others[j]
				if(node.ID != other.ID):
					if other.name == node.name and other.definition == node.definition and other.ID not in deletedNodes:
						#print node.ID, other.ID
						writer.writerow(['MN',str(node.ID),str(other.ID),str(node.name),str(other.name)])#,temp2.name,temp.definition])

						deletedNodes.append(other.ID)
					#others.remove(other)

if __name__ == '__main__':
	main()