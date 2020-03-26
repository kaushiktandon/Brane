# -*- coding: utf-8 -*-

import json
import requests
import csv

class Convert_Clusters():
	def __init__(self):
		print("Create clusters")
	def convert_clusters(self):
		cluster_topics = list()
		cluster_links = list()

		final_topic = 0
		final_link = 0

		# Create generic properties
		properties = dict()
		properties['_key'] = ''
		properties['_type'] = ''
		properties['title'] = ''
		properties['reference'] = ''
		properties['definition'] = ''
		properties['valueType'] = ''

		# T1
		properties['_key'] = 'T1'
		properties['_type'] = 'system'
		properties['title'] = 'Global Research Information Database Ecosystem'
		properties['reference'] = 'https://grid.ac/'
		properties['definition'] = ''
		properties['valueType'] = ''
		cluster_topics.append(create_topic(properties))
		# T2
		properties['_key'] = 'T2'
		properties['_type'] = 'cluster'
		properties['title'] = 'Institution'
		properties['reference'] = ''
		properties['definition'] = 'Institutes associated with academic research'
		properties['valueType'] = ''
		cluster_topics.append(create_topic(properties))
		# T3
		properties['_key'] = 'T3'
		properties['_type'] = 'cluster'
		properties['title'] = 'Education institution'
		properties['reference'] = ''
		properties['definition'] = 'An educational institution where research takes place. Can grant degrees and includes faculties, departments and schools.'
		properties['valueType'] = ''
		cluster_topics.append(create_topic(properties))
		# T4
		properties['_key'] = 'T4'
		properties['_type'] = 'cluster'
		properties['title'] = 'Healthcare institution'
		properties['reference'] = ''
		properties['definition'] = 'A health related facility where patients are treated. Includes hospitals, medical centres, health centres, treatment center. Includes trusts and healthcare systems.'
		properties['valueType'] = ''
		cluster_topics.append(create_topic(properties))
		# T5
		properties['_key'] = 'T5'
		properties['_type'] = 'cluster'
		properties['title'] = 'Company'
		properties['reference'] = ''
		properties['definition'] = 'Business entity with the aim of gaining profit.'
		properties['valueType'] = ''
		cluster_topics.append(create_topic(properties))
		# T6
		properties['_key'] = 'T6'
		properties['_type'] = 'cluster'
		properties['title'] = 'Archive institution'
		properties['reference'] = ''
		properties['definition'] = 'Repository of documents, artifacts, or specimens. Includes libraries and museums that are not part of a university.'
		properties['valueType'] = ''
		cluster_topics.append(create_topic(properties))
		# T7
		properties['_key'] = 'T7'
		properties['_type'] = 'cluster'
		properties['title'] = 'Nonprofit institution'
		properties['reference'] = ''
		properties['definition'] = 'Organisation that uses its surplus revenue to achieve its goals. Includes charities and other non-government research funding bodies.'
		properties['valueType'] = ''
		cluster_topics.append(create_topic(properties))
		# T8
		properties['_key'] = 'T8'
		properties['_type'] = 'cluster'
		properties['title'] = 'Government institution'
		properties['reference'] = ''
		properties['definition'] = 'An organisation operated mainly by the government of one or multiple countries/territories.'
		properties['valueType'] = ''
		cluster_topics.append(create_topic(properties))
		# T9
		properties['_key'] = 'T9'
		properties['_type'] = 'cluster'
		properties['title'] = 'Facility'
		properties['reference'] = ''
		properties['definition'] = 'A building or facility dedicated to research of a specific area, usually contains specialised equipment. Includes telescopes, observatories and particle accelerators.'
		properties['valueType'] = ''
		cluster_topics.append(create_topic(properties))
		# T10
		properties['_key'] = 'T10'
		properties['_type'] = 'cluster'
		properties['title'] = 'Other institution'
		properties['reference'] = ''
		properties['definition'] = 'Used in cases where none of the previously mentioned types are suitable.'
		properties['valueType'] = ''
		cluster_topics.append(create_topic(properties))
		# T11
		properties['_key'] = 'T11'
		properties['_type'] = 'property'
		properties['title'] = 'Founding date'
		properties['reference'] = ''
		properties['definition'] = 'The founding date of an institution'
		properties['valueType'] = 'integer'
		cluster_topics.append(create_topic(properties))
		# T12
		properties['_key'] = 'T12'
		properties['_type'] = 'cluster'
		properties['title'] = 'Geographic location'
		properties['reference'] = ''
		properties['definition'] = ''
		properties['valueType'] = ''
		cluster_topics.append(create_topic(properties))
		# T13
		properties['_key'] = 'T13'
		properties['_type'] = 'cluster'
		properties['title'] = 'Country'
		properties['reference'] = ''
		properties['definition'] = ''
		properties['valueType'] = ''
		cluster_topics.append(create_topic(properties))
		# T14
		properties['_key'] = 'T14'
		properties['_type'] = 'cluster'
		properties['title'] = 'Region'
		properties['reference'] = ''
		properties['definition'] = ''
		properties['valueType'] = ''
		cluster_topics.append(create_topic(properties))
		# T15
		properties['_key'] = 'T15'
		properties['_type'] = 'cluster'
		properties['title'] = 'City'
		properties['reference'] = ''
		properties['definition'] = ''
		properties['valueType'] = ''
		cluster_topics.append(create_topic(properties))

		final_topic = 15

		# Create links
		properties = dict()
		properties['_key'] = ''
		properties['_type'] = ''
		properties['name'] = ''
		properties['_from'] = ''
		properties['_to'] = ''
		properties['value'] = ''

		# L1
		properties['_key'] = 'L1'
		properties['_type'] = 'encompasses'
		properties['name'] = ''
		properties['_from'] = 'T1'
		properties['_to'] = 'T2'
		properties['value'] = ''
		cluster_links.append(create_link(properties))
		# L3
		properties['_key'] = 'L3'
		properties['_type'] = 'encompasses'
		properties['name'] = ''
		properties['_from'] = 'T1'
		properties['_to'] = 'T12'
		properties['value'] = ''
		cluster_links.append(create_link(properties))
		# L4
		properties['_key'] = 'L4'
		properties['_type'] = 'hasSubclass'
		properties['name'] = ''
		properties['_from'] = 'T2'
		properties['_to'] = 'T3'
		properties['value'] = ''
		cluster_links.append(create_link(properties))
		# L5
		properties['_key'] = 'L5'
		properties['_type'] = 'hasSubclass'
		properties['name'] = ''
		properties['_from'] = 'T2'
		properties['_to'] = 'T4'
		properties['value'] = ''
		cluster_links.append(create_link(properties))
		# L6
		properties['_key'] = 'L6'
		properties['_type'] = 'hasSubclass'
		properties['name'] = ''
		properties['_from'] = 'T2'
		properties['_to'] = 'T5'
		properties['value'] = ''
		cluster_links.append(create_link(properties))
		# L7
		properties['_key'] = 'L7'
		properties['_type'] = 'hasSubclass'
		properties['name'] = ''
		properties['_from'] = 'T2'
		properties['_to'] = 'T6'
		properties['value'] = ''
		cluster_links.append(create_link(properties))
		# L8
		properties['_key'] = 'L8'
		properties['_type'] = 'hasSubclass'
		properties['name'] = ''
		properties['_from'] = 'T2'
		properties['_to'] = 'T7'
		properties['value'] = ''
		cluster_links.append(create_link(properties))
		# L9
		properties['_key'] = 'L9'
		properties['_type'] = 'hasSubclass'
		properties['name'] = ''
		properties['_from'] = 'T2'
		properties['_to'] = 'T8'
		properties['value'] = ''
		cluster_links.append(create_link(properties))
		# L10
		properties['_key'] = 'L10'
		properties['_type'] = 'hasSubclass'
		properties['name'] = ''
		properties['_from'] = 'T2'
		properties['_to'] = 'T9'
		properties['value'] = ''
		cluster_links.append(create_link(properties))
		# L11
		properties['_key'] = 'L11'
		properties['_type'] = 'hasSubclass'
		properties['name'] = ''
		properties['_from'] = 'T12'
		properties['_to'] = 'T13'
		properties['value'] = ''
		cluster_links.append(create_link(properties))
		# L12
		properties['_key'] = 'L12'
		properties['_type'] = 'hasSubclass'
		properties['name'] = ''
		properties['_from'] = 'T12'
		properties['_to'] = 'T14'
		properties['value'] = ''
		cluster_links.append(create_link(properties))
		# L13
		properties['_key'] = 'L13'
		properties['_type'] = 'hasSubclass'
		properties['name'] = ''
		properties['_from'] = 'T12'
		properties['_to'] = 'T15'
		properties['value'] = ''
		cluster_links.append(create_link(properties))

		final_link = 13

		return cluster_topics, cluster_links, final_topic + 1, final_link + 1
def create_topic(properties):
	topic_json_struct = {}
	for prop, value in properties.items():
		if value != None:
			topic_json_struct[prop] = value
	return topic_json_struct
def create_link(properties):
	return create_topic(properties)
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
# General helper function
def output_to_file(info, file):
	with open(file, 'w', encoding='utf-8') as f:
		# There's probably a better way to output as a list of JSON objects
		f.write('[')
		i = 0
		for topic in info:
			f.write(json.dumps(topic, ensure_ascii=False))
			if i != len(info) - 1:
				f.write(",\n")
			else:
				f.write('\n')
			i = i + 1
		f.write(']')
def new_topic_key(topic_key_val):
	return 'T' + str(topic_key_val), topic_key_val + 1

def new_link_key(link_key_val):
	return 'L' + str(link_key_val), link_key_val + 1

def update_ids(grid_name, row):
	if (len(row['external_ids'][grid_name]['all']) > 1):
		return row['external_ids'][grid_name]['all']
	else:
		return row['external_ids'][grid_name]['all'][0]

def extract_terms(aliases, name):
	terms = []
	for alias in aliases:
		if alias != name:
			terms.append(alias)
	return terms

def working_link(url):
	if url == None:
		return False
	url = url.strip()
	if url == '':
		return False
	return True
	# try:
	#	request = requests.get(url)
	#	if request.status_code == 200:
	#		return True
	# except Exception as e:
	#	print(url)
	#	return False
	# print("A: " + url)
	# return False

def extract_references(insitute_links, wikipedia_url):
	new_refs = ""
	for link in insitute_links:
		if working_link(link):
			new_refs += link + ';'
	if (working_link(wikipedia_url)):
		new_refs += wikipedia_url + ';'

	if new_refs != '':
		new_refs = new_refs[:-1]

	refs = [new_refs]
	return refs

def main():
	data_file = 'grid_data.json'
	with open(data_file, encoding='utf-8') as f:
		data = json.load(f)

	# Create list of topics
	new_topics = list()
	new_links = list()

	print("Creating clusters")
	cluster_runner = Convert_Clusters()
	cluster_topics, cluster_links, topic_key_val, link_key_val = cluster_runner.convert_clusters()
	new_topics = add_new_topics(new_topics, cluster_topics)
	new_links = add_new_links(new_links, cluster_links)

	grid_id_to_topic_key = dict()
	city_id_to_topic_key = dict()
	region_code_to_topic_key = dict()
	country_code_to_topic_key = dict()

	# Create institutes
	for row in data['institutes']:
		if row.get('types') != None:
			if (len(row['types']) == 0):
				pass
			else:
				type_ = row['types'][0]
				if (type_ == 'Education'):
					my_type = 'education_institution'
					cluster = 'T3'
				elif (type_ == 'Healthcare'):
					my_type = 'healthcare_institution'
					cluster = 'T4'
				elif (type_ == 'Company'):
					my_type = 'company'
					cluster = 'T5'
				elif (type_ == 'Archive'):
					my_type = 'archive_institution'
					cluster = 'T6'
				elif (type_ == 'Nonprofit'):
					my_type = 'nonprofit_institution'
					cluster = 'T7'
				elif (type_ == 'Government'):
					my_type = 'government_institution'
					cluster = 'T8'
				elif (type_ == 'Facility'):
					my_type = 'facility'
					cluster = 'T9'
				elif (type_ == 'Other'):
					my_type = 'other_institution'
					cluster = 'T10'
				topic_key, topic_key_val = new_topic_key(topic_key_val)
				topic_params = {'_key': topic_key, '_type': my_type, 'title': row['name'], 'definition': '', 'Grid ID': row['id']}
				topic_params['terms'] = extract_terms(row['aliases'], row['name'])
				topic_params['reference'] = extract_references(row['links'], row['wikipedia_url'])
				if (row.get('external_ids') != None):
					# ISNI ID
					if (row['external_ids'].get("ISNI") != None):
						topic_params['ISNI ID'] = row['external_ids']['ISNI']['all'][0].replace(' ','')
					# Crossref ID
					if (row['external_ids'].get('FundRef') != None):
						topic_params['Crossref ID'] = update_ids('FundRef', row)
					# Higher education
					if (row['external_ids'].get('HESA') != None):
						topic_params['Higher education'] = update_ids('HESA', row)
					# UCAS ID
					if (row['external_ids'].get('UCAS') != None):
							topic_params['UCAS ID'] = update_ids('UCAS',row )
					# UKPRN ID
					if (row['external_ids'].get('UKPRN') != None):
						topic_params['UKPRN ID'] = update_ids('UKPRN', row)
					# OrgRef ID
					if (row['external_ids'].get('OrgRef') != None):
						topic_params['OrgRef'] = update_ids('OrgRef', row)
					#Wikidata ID
					if (row['external_ids'].get('Wikidata') != None):
						topic_params['Wikidata ID'] = update_ids('Wikidata', row)
					#ROR ID
					if (row['external_ids'].get('ROR') != None):
						topic_params['ROR ID'] = update_ids('ROR', row)
				if (row.get('addresses') != None and len(row['addresses']) != 0):
					address = row['addresses'][0]
					if (address.get('geonames_city') != None):
						# GeoNames City Name
						topic_params['Geonames City Name'] = address['geonames_city']['city']
						# GeoNames City ID
						topic_params['Geonames City ID'] = address['geonames_city']['id']
						if (address['geonames_city'].get('geonames_admin2') != None):
							# Geonames Admin 2 Region Name
							topic_params['Geonames Admin 2 Region Name'] = address['geonames_city']['geonames_admin2']['name']
							# Geonames Admin 2 Region Code
							topic_params['Geonames Admin 2 Region Code'] = address['geonames_city']['geonames_admin2']['code']
							# Geonames Admin 2 Region ID
							topic_params['Geonames Admin 2 Region ID'] = address['geonames_city']['geonames_admin2'].get('id')
						if (address['geonames_city'].get('geonames_admin1') != None):
							# Geonames Admin 1 Region Name
							topic_params['Geonames Admin 1 Region Name'] = address['geonames_city']['geonames_admin1']['name']
							# Geonames Admin 1 Region Code
							topic_params['Geonames Admin 1 Region Code'] = address['geonames_city']['geonames_admin1']['code']
							# Geonames Admin 1 Region ID
							topic_params['Geonames Admin 1 Region ID'] = address['geonames_city']['geonames_admin1'].get('id')
						if (address['geonames_city'].get('nuts_level3') != None):
							# NUTS 3 Name
							topic_params['NUTS 3 Name'] = address['geonames_city']['nuts_level3']['name']
							# NUTS 3 Code
							topic_params['NUTS 3 Code'] = address['geonames_city']['nuts_level3']['code']
						if (address['geonames_city'].get('nuts_level2') != None):
							# NUTS 2 Name
							topic_params['NUTS 2 Name'] = address['geonames_city']['nuts_level2']['name']
							# NUTS 2 Code
							topic_params['NUTS 2 Code'] = address['geonames_city']['nuts_level2']['code']
						if (address['geonames_city'].get('nuts_level1') != None):
							# NUTS 1 Name
							topic_params['NUTS 1 Name'] = address['geonames_city']['nuts_level1']['name']
							# NUTS 1 Code
							topic_params['NUTS 1 Code'] = address['geonames_city']['nuts_level1']['code']
					# GeoNames Country/Territory Name
					topic_params['Geonames Country/Territory Name'] = address['country']
					# GeoNames Country/Territory Code
					topic_params['Geonames Country/Territory Code'] = address['country_code']
					# GeoNames Country/Territory ID
					topic_params['Geonames Country/Territory ID'] = address.get('country_id')

				new_topics.append(create_topic(topic_params))
				grid_id_to_topic_key[row['id']] = topic_key
				# Link institute to cluster
				link_key, link_key_val = new_link_key(link_key_val)
				link_params = {'_key': link_key,'_type': 'hasInstance', '_from': cluster, '_to': topic_key}
				new_links.append(create_link(link_params))
				# Link institute to founding date
				if (row['established'] != None):
					link_key, link_key_val = new_link_key(link_key_val)
					link_params = {'_key': link_key,'_type': 'has', '_from': topic_key, '_to': 'T11', 'value': row['established']}
					new_links.append(create_link(link_params))

	# Link to affiliated insitutions
	for row in data['institutes']:
		if row.get('relationships') != None:
			my_key = grid_id_to_topic_key.get(row["id"])
			if my_key != None:
				for relationship in row.get('relationships'):
					other_key = grid_id_to_topic_key.get(relationship['id'])
					if (other_key != None):
						if (relationship['type'] == 'Parent'):
							link_key, link_key_val = new_link_key(link_key_val)
							link_params = {'_key': link_key,'_type': 'link', 'name':'contains', '_from': other_key, '_to': my_key}
							new_links.append(create_link(link_params))
						elif (relationship['type'] == 'Child'):
							link_key, link_key_val = new_link_key(link_key_val)
							link_params = {'_key': link_key,'_type': 'link', 'name':'contains', '_from': my_key, '_to': other_key}
							new_links.append(create_link(link_params))
						elif (relationship['type'] == 'Related'):
							link_key, link_key_val = new_link_key(link_key_val)
							link_params = {'_key': link_key,'_type': 'link', 'name':'is affiliated with', '_from': my_key, '_to': other_key}
							new_links.append(create_link(link_params))
	# Create countries
	for row in data['institutes']:
		if row.get('addresses') != None:
			address = row['addresses'][0]
			country_name = address.get('country')
			country_code = address.get('country_code')
			# Doe this country exist already
			if country_name != None and country_name != '' and country_code_to_topic_key.get(country_code) == None:
				topic_key, topic_key_val = new_topic_key(topic_key_val)
				definition = country_name + " is a country"
				topic_params = {'_key': topic_key, '_type': 'topic', 'title': country_name, 'definition': definition}
				topic_params['Geonames Country/Territory Name'] = country_name
				topic_params['Geonames Country/Territory Code'] = country_code
				topic_params['Geonames Country/Territory ID'] = address.get('country_id')
				if (address.get('geonames_city') != None and address['geonames_city'].get('nuts_level1') != None):
					topic_params['NUTS 1 Code'] = address['geonames_city']['nuts_level1']['code']

				new_topics.append(create_topic(topic_params))
				country_code_to_topic_key[country_code] = topic_key

				# Link country to cluster
				link_key, link_key_val = new_link_key(link_key_val)
				link_params = {'_key': link_key,'_type': 'hasInstance', '_from': 'T13', '_to': topic_key}
				new_links.append(create_link(link_params))

	# Create regions
	for row in data['institutes']:
		if row.get('addresses') != None:
			address = row['addresses'][0]
			if (address.get('geonames_city') != None):
				if (address['geonames_city'].get('geonames_admin1') != None):
					region_code = address['geonames_city']['geonames_admin1']['code']
					# Does this region exist already
					if (region_code_to_topic_key.get(region_code) == None and address['geonames_city']['geonames_admin1'].get('name') != None):
						region_name = address['geonames_city']['geonames_admin1']['name']
						definition = region_name
						country_name = address.get('country')
						if (country_name != None and country_name != ''):
							region_name += ' (' + country_name + ')'
							definition += ' is a region in ' + country_name

						topic_key, topic_key_val = new_topic_key(topic_key_val)
						topic_params = {'_key': topic_key, '_type': 'topic', 'title': region_name, 'definition': definition}
						topic_params['Geonames Admin 1 Region Name'] = address['geonames_city']['geonames_admin1']['name']
						topic_params['Geonames Admin 1 Region Code'] = address['geonames_city']['geonames_admin1']['code']
						topic_params['Geonames Admin 1 Region ID'] = address['geonames_city']['geonames_admin1'].get('id')

						if (country_name != None):
							topic_params['Geonames Country/Territory Name'] = country_name
							topic_params['Geonames Country/Territory Code'] = address['country_code']
							topic_params['Geonames Country/Territory ID'] = address.get('country_id')

						if (address['geonames_city'].get('nuts_level2') != None):
							topic_params['NUTS 2 Name'] = address['geonames_city']['nuts_level2']['name']
							topic_params['NUTS 2 Code'] = address['geonames_city']['nuts_level2']['code']
						if (address['geonames_city'].get('nuts_level1') != None):
							topic_params['NUTS 1 Name'] = address['geonames_city']['nuts_level1']['name']
							topic_params['NUTS 1 Code'] = address['geonames_city']['nuts_level1']['code']

						new_topics.append(create_topic(topic_params))
						region_code_to_topic_key[region_code] = topic_key
						# Link region to cluster
						link_key, link_key_val = new_link_key(link_key_val)
						link_params = {'_key': link_key,'_type': 'hasInstance', '_from': 'T14', '_to': topic_key}
						new_links.append(create_link(link_params))
						# Link region to country
						country_code = address['country_code']
						if (country_code != '' and country_name != ''):
							country_key = country_code_to_topic_key[country_code]
							link_key, link_key_val = new_link_key(link_key_val)
							link_params = {'_key': link_key,'_type': 'link', 'name': 'is located in', '_from': topic_key, '_to': country_key}
							new_links.append(create_link(link_params))

	# Create cities
	for row in data['institutes']:
		if row.get('addresses') != None:
			address = row['addresses'][0]
			if (address.get('geonames_city') != None):
				# Does this city already exist?
				if (city_id_to_topic_key.get(address['geonames_city']['id']) == None):
					city_name = address['city']
					definition = city_name
					country_name = address.get('country')
					if (country_name != None and country_name != ''):
						city_name += ' (' + country_name + ')'
						definition += ' is a city in ' + country_name

					topic_key, topic_key_val = new_topic_key(topic_key_val)
					topic_params = {'_key': topic_key, '_type': 'topic', 'title': city_name, 'definition': definition, 'Geonames City ID': address['geonames_city']['id']}
					if (address['geonames_city'].get('geonames_admin2') != None and address['geonames_city']['geonames_admin2']['name'] != ''):
						topic_params['Geonames Admin 2 Region Name'] = address['geonames_city']['geonames_admin2']['name']
						topic_params['Geonames Admin 2 Region Code'] = address['geonames_city']['geonames_admin2']['code']
						topic_params['Geonames Admin 2 Region ID'] = address['geonames_city']['geonames_admin2'].get('id')
					if (address['geonames_city'].get('geonames_admin1') != None and address['geonames_city']['geonames_admin1']['name'] != ''):
						topic_params['Geonames Admin 1 Region Name'] = address['geonames_city']['geonames_admin1']['name']
						topic_params['Geonames Admin 1 Region Code'] = address['geonames_city']['geonames_admin1']['code']
						topic_params['Geonames Admin 1 Region ID'] = address['geonames_city']['geonames_admin1'].get('id')

					if (country_name != None and country_name != ''):
						topic_params['Geonames Country/Territory Name'] = country_name
						topic_params['Geonames Country/Territory Code'] = address['country_code']
						topic_params['Geonames Country/Territory ID'] = address.get('country_id')

					if (address['geonames_city'].get('nuts_level3') != None):
						topic_params['NUTS 3 Name'] = address['geonames_city']['nuts_level3']['name']
						topic_params['NUTS 3 Code'] = address['geonames_city']['nuts_level3']['code']
					if (address['geonames_city'].get('nuts_level2') != None):
						topic_params['NUTS 2 Name'] = address['geonames_city']['nuts_level2']['name']
						topic_params['NUTS 2 Code'] = address['geonames_city']['nuts_level2']['code']
					if (address['geonames_city'].get('nuts_level1') != None):
						topic_params['NUTS 1 Name'] = address['geonames_city']['nuts_level1']['name']
						topic_params['NUTS 1 Code'] = address['geonames_city']['nuts_level1']['code']

					new_topics.append(create_topic(topic_params))
					city_id_to_topic_key[address['geonames_city']['id']] = topic_key
					# Link city to cluster
					link_key, link_key_val = new_link_key(link_key_val)
					link_params = {'_key': link_key,'_type': 'hasInstance', '_from': 'T15', '_to': topic_key}
					new_links.append(create_link(link_params))
					# Link city to region
					region_name = topic_params.get('Geonames Admin 1 Region Name')
					region_code = topic_params.get('Geonames Admin 1 Region Code')
					if (region_code != '' and region_name != '' and region_code_to_topic_key.get(region_code) != None):
						region_key = region_code_to_topic_key[region_code]
						link_key, link_key_val = new_link_key(link_key_val)
						link_params = {'_key': link_key,'_type': 'link', 'name': 'is located in', '_from': topic_key, '_to': region_key}
						new_links.append(create_link(link_params))
					# Link city to country
					country_code = address['country_code']
					if (country_code != '' and country_name != '' and country_code_to_topic_key.get(country_code) != None):
						country_key = country_code_to_topic_key[country_code]
						link_key, link_key_val = new_link_key(link_key_val)
						link_params = {'_key': link_key,'_type': 'link', 'name': 'is located in', '_from': topic_key, '_to': country_key}
						new_links.append(create_link(link_params))
	# Link institutes to country, region, city
	for row in data['institutes']:
		my_key = grid_id_to_topic_key.get(row["id"])
		if my_key != None:
			address = row['addresses'][0]
			# Link to country
			country_code = address.get('country_code')
			if (country_code != None):
				country_key = country_code_to_topic_key[country_code]
				link_key, link_key_val = new_link_key(link_key_val)
				link_params = {'_key': link_key,'_type': 'link', 'name': 'is located in', '_from': my_key, '_to': country_key}
				new_links.append(create_link(link_params))

			# Link to region
			if (address.get('geonames_city') != None and address['geonames_city'].get('geonames_admin1') != None and address['geonames_city']['geonames_admin1'].get('name') != None):
				region_code = address['geonames_city']['geonames_admin1']['code']
				region_key = region_code_to_topic_key[region_code]
				link_key, link_key_val = new_link_key(link_key_val)
				link_params = {'_key': link_key,'_type': 'link', 'name': 'is located in', '_from': my_key, '_to': region_key}
				new_links.append(create_link(link_params))

			# Link to city
			if (address.get('geonames_city') != None):
				city_id = address['geonames_city']['id']
				city_key = city_id_to_topic_key[city_id]
				link_key, link_key_val = new_link_key(link_key_val)
				link_params = {'_key': link_key,'_type': 'link', 'name': 'is located in', '_from': my_key, '_to': city_key}
				new_links.append(create_link(link_params))
	print("Outputting to files")
	# Output topics to file
	output_to_file(new_topics, 'output/combined_topics.json')
	output_to_file(new_links, 'output/combined_links.json')

if __name__ == '__main__':
	main()