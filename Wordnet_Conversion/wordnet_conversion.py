import csv
import json

def T1():
	topic_json_struct = {}
	topic_json_struct['_key'] = 'T1'
	topic_json_struct["_type"] = "system"
	topic_json_struct['title'] = 'Wordnet'
	topic_json_struct['definition'] = 'WordNet® is a large lexical database of English. Nouns, verbs, adjectives and adverbs are grouped into sets of cognitive synonyms (synsets), each expressing a distinct concept. Synsets are interlinked by means of conceptual-semantic and lexical relations. The resulting network of meaningfully related words and concepts can be navigated with the browser. WordNet is also freely and publicly available for download. WordNet\'s structure makes it a useful tool for computational linguistics and natural language processing.'
	topic_json_struct['terms'] = ['wordnet']
	topic_json_struct['sources'] = 'https://wordnet.princeton.edu/'
	topic_json_struct['wordnet_version'] = '3.0'
	return topic_json_struct

def L1():
	link_json_struct = {}
	link_json_struct['_key'] = 'L1'
	link_json_struct['_type'] = 'encompasses'
	link_json_struct['name'] = ''
	link_json_struct['definition'] = ''
	link_json_struct['_from'] = 'T1'
	link_json_struct['_to'] = 'T2'
	return link_json_struct

def L2():
	link_json_struct = {}
	link_json_struct['_key'] = 'L2'
	link_json_struct['_type'] = 'encompasses'
	link_json_struct['name'] = ''
	link_json_struct['definition'] = ''
	link_json_struct['_from'] = 'T1'
	link_json_struct['_to'] = 'T4'
	return link_json_struct	

def main():
	csv_file = 'wordnet_graph_import.csv'
	created_topics = dict()
	created_links = list()
	id_to_key = dict()

	created_topics['T1'] = T1()
	created_links.append(L1())
	created_links.append(L2())
	topic_key_val = 2
	link_key_val = 3

	with open(csv_file, 'r', encoding='utf8') as inputFile:
		csv_reader = csv.reader(inputFile)
		for line in csv_reader:
			row_str = ""
			for element in line:
				row_str += element
			line = row_str
			command = line[:2]
			if command == 'CN':
				topic_key = 'T' + str(topic_key_val)
				# Increment key value for next topic
				topic_key_val = topic_key_val + 1
				old_id = line[3:line.find(';',3)]
				id_to_key[int(old_id)] = topic_key

				# Determine topic title
				topic_title_line = line[line.find(old_id) + len(old_id) + 1 :]
				if (topic_title_line.find(';') != -1):
					topic_title = topic_title_line[:topic_title_line.find(';')]
				else:
					topic_title = topic_title_line
				terms = [topic_title.lower()]
				source = 'https://wordnet.princeton.edu/'
				# Determine definition
				if (line[line.find(topic_title) + len(topic_title) + 1: ] != ""):
					# Determine topic definition
					definition = line[line.find(topic_title) + len(topic_title) + len('definition;') + 1: line.find('graph;wordnet')]
				else:
					definition = ''

				attributes = dict()
				attributes['wordnet_version'] = '3.0'
				if (definition != ''):
					attribute_pairs = line[line.find(definition) + len(definition) : ].split(';') 
					val = False
					key = ''
					for attribute in attribute_pairs:
						if (val):
							if key != 'graph':
								attributes[key] = attribute
							val = False
						else:
							key = attribute
							val = True

				# Output topic to JSON format
				topic_json_struct = {}
				topic_json_struct['_key'] = topic_key
				topic_json_struct["_type"] = "topic"
				topic_json_struct['title'] = topic_title
				topic_json_struct['definition'] = definition
				topic_json_struct['terms'] = terms
				topic_json_struct['sources'] = source
				for attribute_key, attribute_val in attributes.items():
					topic_json_struct[attribute_key] = attribute_val

				created_topics[topic_key] = topic_json_struct
			elif (command == 'SC'):
				old_id = int(line[3:])
				created_topics[id_to_key[old_id]]['_type'] = 'cluster'
			elif (command == 'CL'):
				vals = line.split(';')
				old_id1 = int(vals[1])
				old_id2 = int(vals[2])
				id1 = id_to_key[old_id1]
				id2 = id_to_key[old_id2]
				_type = 'link'
				name = vals[4]

				if (vals[3] == 'is a kind of' and vals[4] == 'contains'):
					topic2 = created_topics[id2]
					if topic2['_type'] == 'cluster' or (id2 == 'T3' or id2 == 'T5'):
						_type = 'hasSubclass'
						name = ''
					elif topic2['_type'] == 'topic':
						_type = 'hasInstance'
						name = ''

				if (vals[3] == 'is an instance of' and vals[4] =='contains'):
					_type = 'hasInstance'
					name = ''
					created_topics[id1]['_type'] = 'cluster'

				link_key = 'L' + str(link_key_val)
				# Increment key value for next link
				link_key_val = link_key_val + 1
				# Output link to JSON format
				link_json_struct = {}
				link_json_struct['_key'] = link_key
				link_json_struct['_type'] = _type
				link_json_struct['name'] = name
				link_json_struct['definition'] = ''
				link_json_struct['_from'] = id1
				link_json_struct['_to'] = id2
				created_links.append(link_json_struct)
	# Output topics to file
	with open('output/wordnet_topics.json', 'w') as f:
		f.write('[')
		i = 0
		for old_id, topic in created_topics.items():
			f.write(json.dumps(topic))
			if i != len(created_topics) - 1:
				f.write(",\n")
			else:
				f.write('\n')
			i = i + 1
		f.write(']')
	# Output links to file
	with open('output/wordnet_links.json', 'w') as f:
		f.write('[')
		i = 0
		for link in created_links:
			f.write(json.dumps(link))
			if i != len(created_links) - 1:
				f.write(",\n")
			else:
				f.write('\n')
			i = i + 1
		f.write(']')

if __name__ == '__main__':
	main()