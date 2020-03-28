import json
import pandas as pd
import sys
import numpy as np

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

	main_graph_topics = pd.read_json(main_graph_topics_file)
	main_graph_topics = main_graph_topics.fillna('')

	next_topic_key_str = main_graph_topics['_key'].iloc[-1]
	topic_key_difference = int(next_topic_key_str[1:])

	main_graph_links = pd.read_json(main_graph_links_file)
	main_graph_links = main_graph_links.fillna('')

	next_link_key_str = main_graph_links['_key'].iloc[-1]
	link_key_difference = int(next_link_key_str[1:])

	print(topic_key_difference, link_key_difference)

	for subgraph_topic_file, subgraph_link_file in subgraphs:
		subgraph_topics = pd.read_json(subgraph_topic_file)
		print(len(subgraph_topics))
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

	if (num_files == 1):
		# Output topics
		main_graph_topics.to_json(output_topics_file + '.json', orient='records')
		# Output links
		main_graph_links.to_json(output_links_file + '.json', orient='records')
	else:
		main_graph_topics = np.array_split(main_graph_topics, num_files)
		main_graph_links = np.array_split(main_graph_links, num_files)
		for i in range (num_files):
			topics_file = output_topics_file + str(i+1) + '.json'
			links_file = output_links_file + str(i+1) + '.json'
			main_graph_topics[i].to_json(topics_file, orient='records')
			main_graph_links[i].to_json(links_file, orient='records')


if __name__ == '__main__':
	main()