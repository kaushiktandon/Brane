# -*- coding: utf-8 -*-

import sys
import codecs
import csv
import time
import json

reload(sys)
sys.setdefaultencoding('utf8')
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

authors_file = 'authors1.csv'
publications_file = 'publications1.csv'
others_file = 'OtherNodes.csv'
links_file = 'links_to_deimport.csv'

nodes_json_file = "results-thebrane (4).json"
deimport_file = "deimport.csv"

ids = list()

def load_nodes(nodes_file):
	nodes = dict()
	count = 0
	with open(nodes_file) as f:
		data = json.load(f)
		for i in range(len(data)):
			a_id = str(data[i][0])
			name = str(data[i][1])
			#a_id = str(data[i]['_key'])
			#name = str(data[i]['t'])
			#reference = data[i].get('a')
			#if(reference != None):
			#	reference = reference.get('reference')
			#	if(reference != None):
			#		if('https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov' in str(reference)):
			#			ids.append(a_id)
						#print a_id, name
			#			count = count + 1
			nodes[name] = a_id;
	print("C" + str(count))
	return nodes

def load_tempID_name_pairs(fileName):
	pairs = dict()
	with open(fileName,'r+') as f:
		reader = csv.reader(f)
		for row in reader:
			if len(row) < 3:
				continue
			if(row[0] == 'CL'):
				continue
			ID = str(row[1])
			name = str(row[2])
			pairs[name] = ID
	print("Loaded " + fileName)
	return pairs

def main():
	database_nodes = load_nodes(nodes_json_file)

	author_nodes = load_tempID_name_pairs(authors_file)
	pub_nodes = load_tempID_name_pairs(publications_file)
	other_nodes = load_tempID_name_pairs(others_file)

	print(len(author_nodes) + len(pub_nodes) + len(other_nodes))


	#delete links
	with open(deimport_file,'w+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		with open(links_file,'r+') as f:
			reader = csv.reader(f)
			for row in reader:
				writer.writerow(['DL',str(row[1]),str(row[2])])
	'''numNodesDeleted = 0
	with open(deimport_file,'w+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		for name, perm_id in database_nodes.iteritems():
			if(int(perm_id) >= 85385724):
				numNodesDeleted = numNodesDeleted + 1
				if name in other_nodes:
					writer.writerow(['DN',str(perm_id)])
				elif(name in author_nodes):
					writer.writerow(['DN',str(perm_id)])
				elif(name in pub_nodes):
					writer.writerow(['DN',str(perm_id)])
				elif('""' in name):
					writer.writerow(['DN',str(perm_id)])
				elif(len(name) > 0 and name[0] == '"'):
					writer.writerow(['DN',str(perm_id)])
				elif('The occurrence of Trichocorixa reticulata in the Gulf of California' in name or 'Large Area Crop Inventory Experiment' in name or 'Operations analysis (study 2.6).  Volume 4:  Computer specification' in name or 'Research done at DERAT (October 1982 through September 1983)' in name or '9- by 15-Foot Low-Speed Wind Tunnel Acoustic Free Field Evaluation' in name or 'Ultraviolet observations of close-binary and pulsating nuclei of planetary nebulae' in name
					or "Computational Icing Risk Analysis of the D8 'Double Bubble' Aircraft" in name or 'Large Area Crop Inventory Experiment (LACIE).  Baseline documentation' in name or 'CARETS:  A prototype regional environmental information system.  Volume 13:  Utility of CARETS products to local planners' in name or 'Use of Skylab data to assess and monitor change in the southern California environment' in name or 'Large Area Crop Inventory Experiment (LACIE).  Level 3 Baseline' in name
					or 'Space shuttle:  M/DAC delta wing booster' in name or 'Two computerized stream searches among meteor orbits:' in name or "Detection and mapping package.  Analyst's guide" in name or 'Users guide UHMLE/RTCC version' in name or 'Investigation of environmental change pattern in Japan.  Land use classification by spectral pattern analysis' in name or 'Shuttle Electrical Power Analysis Program (SEPAP)' in name):
						writer.writerow(['DN',str(perm_id)])
				else:
					numNodesDeleted = numNodesDeleted - 1
					#print name
	with open(deimport_file, 'a+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		for id in ids:
			writer.writerow(['DN',str(id)])
	print(numNodesDeleted)
	'''
if __name__ == '__main__':
	main()