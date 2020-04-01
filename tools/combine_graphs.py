# -*- coding: utf-8 -*-

import json
import pandas as pd
import sys
import numpy as np
import codecs

def output_to_file(info, file):
	with open(file, 'w', encoding='utf-8') as f:
		f.write('[\n')
	with codecs.open(file, 'a', encoding='utf-8') as f:
		i = 0
		for idx, topic in info.iterrows():
			json.dump(topic.to_dict(), f, ensure_ascii=False)
			if i != len(info) - 1:
				f.write(",\n")
			else:
				f.write('\n')
			i = i + 1
		f.write(']')

def deduplicate(subgraph_topics, subgraph_links, main_graph_topics, main_graph_links):
	for idx, subgraph_row in subgraph_topics.iterrows():
		topic_title = subgraph_row['title']

		new_df = main_graph_topics[main_graph_topics['title'] == topic_title]
		# Is this a duplicate title
		if (len(new_df) == 0):
			continue
		main_key = new_df['_key'].iloc[0]
		subgraph_key = subgraph_row['_key']

		potential_links = subgraph_links[subgraph_links['_from'] == subgraph_key]
		potential_links2 = subgraph_links[subgraph_links['_to'] == subgraph_key]
		# Right now only worrying about is affiliated with links
		num_is_affiliated_with = len(potential_links[potential_links['name'] == 'is affiliated with']) + len(potential_links2[potential_links2['name'] == 'is affiliated with']) 
		if num_is_affiliated_with == 0:
			continue

		# Update topic key in subgraph _from column to main_key
		subgraph_links.loc[subgraph_links['_from'] == subgraph_key] = main_key
		# Update topic key in subgraph _to column to main_key
		subgraph_links.loc[subgraph_links['_to'] == subgraph_key] = main_key

		# Remove topic from subgraph_topics
		print("Removing " + subgraph_key + " which is now " + main_key + " " + topic_title)
		subgraph_topics.drop(idx, inplace=True)
	return subgraph_topics, subgraph_links

def main():
	main_graph_topics_file = 'data/covid_topics.json'
	main_graph_links_file = 'data/covid_links.json'

	print("Enter number of json files when running")
	num_files = int(sys.argv[1])
	print(str(num_files * 2) + " total (topic + link) will be outputted")

	subgraphs = []
	subgraphs.append(['data/grid_topics.json', 'data/grid_links.json'])

	output_topics_file = 'full_graph_output/full_graph_topics'
	output_links_file = 'full_graph_output/full_graph_links'

	main_graph_topics = pd.read_json(main_graph_topics_file, encoding='utf8')
	main_graph_topics = main_graph_topics.fillna('')

	next_topic_key_str = main_graph_topics['_key'].iloc[-1]
	topic_key_difference = int(next_topic_key_str[1:])

	main_graph_links = pd.read_json(main_graph_links_file)
	main_graph_links = main_graph_links.fillna('')

	next_link_key_str = main_graph_links['_key'].iloc[-1]
	link_key_difference = int(next_link_key_str[1:])

	print(len(main_graph_topics), len(main_graph_links))

	for subgraph_topic_file, subgraph_link_file in subgraphs:
		subgraph_topics = pd.read_json(subgraph_topic_file, encoding='utf8')
		subgraph_topics = subgraph_topics.fillna('')
		# Set T1 cluster to cluster
		subgraph_topics.iloc[0, 1] = 'cluster'
		# Update topic keys
		keys = subgraph_topics.loc[:, '_key'].str[1:]
		keys = pd.to_numeric(keys)
		keys += topic_key_difference
		keys = keys.astype(str)
		keys = 'T' + keys
		subgraph_topics.loc[:, '_key'] = keys

		# Read links
		subgraph_links = pd.read_json(subgraph_link_file)
		subgraph_links = subgraph_links.fillna('')
		print(len(subgraph_topics), len(subgraph_links))
		# Change encompasses to categorizes
		subgraph_links.loc[subgraph_links['_type'] == 'encompasses', ['_type']] = 'categorizes'
		# Update link keys
		keys = subgraph_links.loc[:, '_key'].str[1:]
		keys = pd.to_numeric(keys)
		keys += link_key_difference
		keys = keys.astype(str)
		keys = 'L' + keys
		subgraph_links.loc[:, '_key'] = keys
		# Update _from
		froms = subgraph_links.loc[:, '_from'].str[1:]
		froms = pd.to_numeric(froms)
		froms += topic_key_difference
		froms = froms.astype(str)
		froms = 'T' + froms
		subgraph_links.loc[:, '_from'] = froms
		# Update to
		to = subgraph_links.loc[:, '_to'].str[1:]
		to = pd.to_numeric(to)
		to += topic_key_difference
		to = to.astype(str)
		to = 'T' + to
		subgraph_links.loc[:, '_to'] = to

		print("Deduplicating")
		print("Original length of topics: " + str(len(subgraph_topics)) + "\n Original length of links: " + str(len(subgraph_links)))
		subgraph_topics, subgraph_links = deduplicate(subgraph_topics, subgraph_links, main_graph_topics, main_graph_links)
		print("New length of topics: " + str(len(subgraph_topics)) + "\n New length of links: " + str(len(subgraph_links)))
		print("Deduplicating complete")

		# Append subgraph topics to main graph
		main_graph_topics = main_graph_topics.append(subgraph_topics, sort=False)
		main_graph_topics.reset_index(inplace=True, drop=True)
		# Append subgraph links to main graph
		main_graph_links = main_graph_links.append(subgraph_links, sort=False)
	
		# Link subgraph and main graph
		next_link_key_str = main_graph_links['_key'].iloc[-1]
		new_link_key_difference = int(next_link_key_str[1:])

		new_link = dict()
		new_link['_key'] = 'L' + str(new_link_key_difference + 1)
		new_link['_type'] = 'encompasses'
		new_link['name'] = ''
		new_link['definition'] = ''
		new_link['value'] = ''
		new_link['_from'] = 'T1'
		new_link['_to'] = 'T' + str(topic_key_difference + 1)
		main_graph_links = main_graph_links.append(new_link, ignore_index=True)

		print(main_graph_links.tail())
		main_graph_links.reset_index(inplace=True, drop=True)
		# Update link_key_difference and topic_key_difference
		next_topic_key_str = main_graph_topics['_key'].iloc[-1]
		topic_key_difference = int(next_topic_key_str[1:])
	
		next_link_key_str = main_graph_links['_key'].iloc[-1]
		link_key_difference = int(next_link_key_str[1:])

	main_graph_topics = main_graph_topics.fillna('')
	main_graph_links = main_graph_links.fillna('')
	print("Original length of topics: " + str(len(main_graph_topics)) + "\n Original length of links: " + str(len(main_graph_links)))
	dups = main_graph_links[main_graph_links.duplicated(subset=['_from', '_to', '_type', 'name', 'value'], keep='first')]
	main_graph_links = main_graph_links[~main_graph_links.duplicated(subset=['_from', '_to', '_type', 'name', 'value'], keep='first')]
	print("New length of topics: " + str(len(main_graph_topics)) + "\n New length of links: " + str(len(main_graph_links)))	
	print("Expected drop : " + str(len(dups)))
	print("Outputting to files")
	if (num_files == 1):
		# Output topics
		output_to_file(main_graph_topics, output_topics_file + '.json')
		# Output links
		output_to_file(main_graph_links, output_links_file + '.json')
	else:
		main_graph_topics = np.array_split(main_graph_topics, num_files)
		main_graph_links = np.array_split(main_graph_links, num_files)

		for i in range (num_files):
			topics_file = output_topics_file + str(i+1) + '.json'
			links_file = output_links_file + str(i+1) + '.json'
			output_to_file(main_graph_topics[i], topics_file)
			print(topics_file + " done")
			output_to_file(main_graph_links[i], links_file)
			print(links_file + " done")
			# main_graph_topics[i].apply(lambda x: [x.dropna()], axis=1).to_json(topics_file, orient='records', lines=True)
			# main_graph_links[i].apply(lambda x: [x.dropna()], axis=1).to_json(links_file, orient='records', lines=True)


if __name__ == '__main__':
	main()