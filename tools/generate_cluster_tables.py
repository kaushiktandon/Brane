import csv
import pandas as pd

def main():
	topics_file = 'topics.csv'
	links_file = 'links.csv'
	output_topics_for_code_file = 'topics.txt'
	output_links_for_code_file = 'links.txt'

	topics = pd.read_csv(topics_file)
	topics = topics.fillna('')

	links = pd.read_csv(links_file)
	links = links.fillna('')

	last_key = 0
	error = False
	with open(output_topics_for_code_file, 'w+') as f:
		f.write("# Create generic properties\nproperties = dict()\n")
		for key in topics.keys():
			f.write("properties['" + key + "'] = ''\n")
		f.write('\n')
		for rowidx in range(len(topics)):
			topic_row = topics.iloc[rowidx,:]
			f.write('# ' + str(topic_row['_key']) +'\n')
			for key in topic_row.keys():
				f.write("properties['" + key + "'] = '" + topic_row[key] +"'\n")
			f.write("cluster_topics.append(create_topic(properties))\n")
			last_key += 1
			if (last_key != int(topic_row['_key'][1:])):
				print("POTENTIAL ERROR: " + str(topic_row['_key']))
				error = True
		f.write("\nfinal_topic = " + str(last_key) + "\n")
		if (error):
			print("FINAL_TOPIC MAY BE WRONG")
	last_key = 0
	error = False
	with open(output_links_for_code_file, 'w+') as f:
		f.write("# Create links\nproperties = dict()\n")
		for key in links.keys():
			f.write("properties['" + key + "'] = ''\n")
		f.write('\n')
		for rowidx in range(len(links)):
			link_row = links.iloc[rowidx,:]
			f.write('# ' + str(link_row['_key']) +'\n')
			for key in link_row.keys():
				f.write("properties['" + key + "'] = '" + link_row[key] +"'\n")
			f.write("cluster_links.append(create_link(properties))\n")
			last_key += 1
			if (last_key != int(link_row['_key'][1:])):
				print("POTENTIAL ERROR: " + str(link_row['_key']))
				error = True
		f.write("\nfinal_link = " + str(last_key) + "\n")
		if (error):
			print("FINAL_LINK MAY BE WRONG")

if __name__ == '__main__':
	main()