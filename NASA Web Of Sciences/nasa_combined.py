'''
	Kaushik Tandon
	January 2020
	NASA Web Of Science conversion for The Brane
'''

import json
import csv
import numpy as np
import pandas as pd

class Convert_Researchers():
	def __init__(self):
		print("Protocol B")
	def parse_author(self, author):
		# The form is LastName, FirstName or LastName, FirstName Middle
		# The middle name will remain part of the first name
		author = author.strip()
		last_name = author.split(',')[0].strip().title()
		first_name = author.split(",")[1].strip().title()
		return first_name, last_name
	def form_author_name(self, first_name, last_name):
		return first_name + " " + last_name
	def parse_orcid_id(self, row, authors):
		orcidIDs = dict()
		if (row == ''):
			return orcidIDs
		# First check for /xxxx-xxxx-xxxx-xxxx versus lastName, firstName/xxxx-xxxx-xxxx-xxxx
		if row[0] == '/':
			# In this case, we need the author name. I will assume it is the first, and hopefully only, author
			first_name, last_name = self.parse_author(authors[0])
			author = self.form_author_name(first_name, last_name)
			orcid_id = row[1:]
			orcidIDs[author] = orcid_id
		else:
			# If there is more than one, they will be separated by ;.
			if (row.find(';') == -1):
				# Only one orcidId
				reversed_author = self.parse_author(row[:row.find('/')])
				author = self.form_author_name(reversed_author[0], reversed_author[1])

				orcid_id = row[row.find('/') + 1:]
				# print(row, author, orcid_id)
				orcidIDs[author] = orcid_id
			else:
				# There are multiple
				elements = row.split(';')
				for element in elements:
					if (element != '' and element.find(',') != -1):
						reversed_author = self.parse_author(element[:element.find('/')])
						author = self.form_author_name(reversed_author[0], reversed_author[1])

						orcid_id = element[element.find('/') + 1:]
						orcidIDs[author] = orcid_id

		return orcidIDs

	# Protocol B main function to run
	def convert_researchers(self, data, topic_key_val, link_key_val):
		researcher_topics = list()
		researcher_links = list()

		for rowidx in range(len(data)):
			# Get current row in dataset
			publication_row = data.iloc[rowidx,:]
			# Get the authors using the AF key
			authors = publication_row['AF'].split(";")
			reprint_address_last_name = publication_row['RP'].split(",")[0].title()
			orcidIDs = self.parse_orcid_id(publication_row['OI'], authors)
			for author in authors:
				# Check for incorrectly formatted name - very rare, but has to be done
				if (author.find(',') == -1):
					# Skip if no comma
					continue
				topic_key = 'T' + str(topic_key_val)
				# Increment key value for next topic
				topic_key_val = topic_key_val + 1

				first_name, last_name = self.parse_author(author)
				initials = first_name[0] + "." + last_name[0] + "."
				terms = [self.form_author_name(first_name, last_name), last_name, initials]
				title = self.form_author_name(first_name, last_name)

				if (last_name == reprint_address_last_name):
					email = publication_row['EM']
				else:
					email = ""

				orcid_id = orcidIDs.get(title)
				if (orcid_id == None):
					orcid_id = ''

				# Look for duplicates
				possible_duplicates = []
				duplicate = False
				for topic in researcher_topics:
					if topic['title'] == title:
						# If the orcid IDs match and we can't deduplicate
						if (topic['orcidID'] == orcid_id and orcid_id == ""):
							topic['Possible_Duplicates'].append(topic_key)
							possible_duplicates.append(topic['_key'])
						elif (topic['orcidID'] == orcid_id and orcid_id != ""):
							# This is a duplicate based on orcid id - we don't need to store it
							duplicate = True
				# Skip making a topic for this author
				if (duplicate):
					continue

				# Output topic to JSON format
				topic_json_struct = {}
				topic_json_struct['_key'] = topic_key
				topic_json_struct["_type"] = "individual"
				topic_json_struct['title'] = title
				topic_json_struct['terms'] = terms
				topic_json_struct['definition'] = ''
				topic_json_struct['sources'] = "Web of Science, row " + str(rowidx + 2)
				topic_json_struct['firstName'] = first_name
				topic_json_struct['lastName'] = last_name
				topic_json_struct['initials'] = initials
				topic_json_struct['email'] = email
				topic_json_struct['orcidID'] = orcid_id
				topic_json_struct['Possible_Duplicates'] = possible_duplicates

				# Store in list to output at end
				researcher_topics.append(topic_json_struct)

				link_key = 'L' + str(link_key_val)
				# Increment key value for next link
				link_key_val = link_key_val + 1

				# Output link to JSON format
				link_json_struct = {}
				link_json_struct['_key'] = link_key
				link_json_struct['_type'] = 'hasInstance'
				link_json_struct['name'] = ''
				link_json_struct['definition'] = ''
				link_json_struct['_from'] = 'T3'
				link_json_struct['_to'] = topic_key

				# Store in list to output at end
				researcher_links.append(link_json_struct)
		return researcher_topics, researcher_links, topic_key_val, link_key_val

class Convert_Publications():
	def __init__(self):
		print("Protocol C")
	# Protocol C main function to run
	def convert_publications(self, data, topic_key_val, link_key_val):
		publication_topics = list()
		publication_links = list()

		for rowidx in range(len(data)):
			# Get current row in dataset
			publication_row = data.iloc[rowidx,:]
			issn = publication_row['SN']
			electronic_issn = publication_row['EI']
			isbn = publication_row['BN']
			_type = "publication"
			# Determine which columns to read based off value of ISSN
			if (issn != ""):
				topic_title = publication_row['SO'].title()
				terms = [topic_title, publication_row['J9'].title(), publication_row['JI'].title()]
			else:
				if (publication_row['SE'] != '' and publication_row['SO'] != ''):
					topic_title = (publication_row['SE'] + " - " + publication_row['SO']).title()
				elif (publication_row['SE'] != '' and publication_row['SO'] == ''):
					topic_title = publication_row['SE'].title()
				elif (publication_row['SO'] != '' and publication_row['SE'] == ''):
					topic_title = publication_row['SO'].title()
				terms = [topic_title, publication_row['J9'].title()]

			# Determine whether conference proceeding or journal
			conference = False
			if (publication_row['BN'] != ""):
				conference = True

			# Look for duplicates
			duplicate = False
			for topic in publication_topics:
				if topic['title'] == topic_title:
					# If the ISSN or ISBN match, assuming there is data, then this is a duplicate
					if (topic['ISBN'] == isbn and isbn != "") or (topic['ISSN'] == issn and issn != ""):
						topic['sources'] = topic['sources'] + ', row ' + str(rowidx + 2)
						duplicate = True
					# No data for issn/isbn but electronic issn matches
					elif (isbn == '' and issn == '' and topic['Electronic_ISSN'] == electronic_issn):
						topic['sources'] = topic['sources'] + ', row ' + str(rowidx + 2)
						duplicate = True
			# Skip making a topic for this publication
			if (duplicate):
				continue

			topic_key = 'T' + str(topic_key_val)
			# Increment key value for next topic
			topic_key_val = topic_key_val + 1

			# Output topic to JSON format
			topic_json_struct = {}
			topic_json_struct['_key'] = topic_key
			topic_json_struct["_type"] = _type
			topic_json_struct['title'] = topic_title
			topic_json_struct['terms'] = terms
			topic_json_struct['sources'] = "Web of Science, row " + str(rowidx + 2)
			topic_json_struct['ISSN'] = issn
			topic_json_struct['Electronic_ISSN'] = electronic_issn
			topic_json_struct['ISBN'] = isbn

			# Store in list to output at end
			publication_topics.append(topic_json_struct)

			link_key = 'L' + str(link_key_val)
			# Increment key value for next link
			link_key_val = link_key_val + 1

			# Output link to JSON format
			link_json_struct = {}
			link_json_struct['_key'] = link_key
			link_json_struct['_type'] = 'hasSubclass'
			link_json_struct['name'] = ''
			link_json_struct['definition'] = ''
			link_json_struct['_from'] = 'T12' if conference else 'T11' 
			link_json_struct['_to'] = topic_key

			# Store in list to output at end
			publication_links.append(link_json_struct)
		return publication_topics, publication_links, topic_key_val, link_key_val

# General helper function
def add_new_topics(old_topics, new_topics):
	for topic in new_topics:
		old_topics.append(topic)
	return old_topics

# General helper function
def add_new_links(old_links, new_links):
	for link in new_links:
		old_links.append(link)
	return old_links

def output_to_file(info, file):
	with open(file, 'w') as f:
		# There's probably a better way to output as a list of JSON objects
		f.write('[')
		i = 0
		for topic in info:
			f.write(json.dumps(topic))
			if i != len(info) - 1:
				f.write(",\n")
			else:
				f.write('\n')
			i = i + 1
		f.write(']')

def main():
	# Create list of topics
	new_topics = list()
	new_links = list()

	# Load and clean the data
	data = pd.read_csv("data.csv")
	data = data.fillna('')
	# Starting at key value T24 for topics
	topic_key_val = 24
	# Starting at key value L23 for links
	link_key_val = 23

	print("Converting researchers")
	researcher_runner = Convert_Researchers()
	researcher_topics, researcher_links, topic_key_val, link_key_val = 	researcher_runner.convert_researchers(data, topic_key_val, link_key_val)
	new_topics = add_new_topics(new_topics, researcher_topics)
	new_links = add_new_links(new_links, researcher_links)

	print("Converting publications")
	publication_runner = Convert_Publications()
	publication_topics, publication_links, topic_key_val, link_key_val = publication_runner.convert_publications(data, topic_key_val, link_key_val)
	new_topics = add_new_topics(new_topics, publication_topics)
	new_links = add_new_links(new_links, publication_links)

	print("Outputting to files")
	# Output topics to file
	output_to_file(new_topics, 'output/combined_topics.json')
	output_to_file(new_links, 'output/combined_links.json')

if __name__ == '__main__':
	main()