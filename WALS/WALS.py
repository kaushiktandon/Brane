# -*- coding: utf-8 -*-

import sys
import codecs
import csv
import time
from bs4 import BeautifulSoup
import requests
import json

reload(sys)
sys.setdefaultencoding('utf8')
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

input_file = 'Languages.csv'
database_file = 'database_json.json'
output_file = "WALS_output.csv"

start_url = 'https://wals.info/languoid/genealogy'

existing_languages = {
	'Sign language':  '85167029',
	'Esperanto':  '85167369',
	'Metalanguage':  '85168005',
	'Latin':  '85166942',
	'Greek language':  '85167147',
	'Azeri (Latin)':  '85191237',
	'Belarusian':  '85191240',
	'Indonesian':  '85191265',
	'Faroese':  '85191254',
	'Pashto':  '85191230',
	'Albanian':  '85191231',
	'Armenian':  '85191234',
	'German':  '85191236',
	'French':  '85191241',
	'Khmer':  '85191246',
	'Croatian':  '85191249',
	'Swedish':  '85191255',
	'Greek':  '85191259',
	'Chinese (Traditional) legacy':  '85191261',
	'Icelandic':  '85191263',
	'Irish':  '85191267',
	'Hebrew':  '85191268',
	'Nepali':  '85191282',
	'Maori':  '85191284',
	'Urdu':  '85191287',
	'Polish':  '85191288',
	'Romanian':  '85191289',
	'Kinyarwanda':  '85191291',
	'Slovak':  '85191293',
	'Setswana':  '85191295',
	'Syriac':  '85191299',
	'Tajik (Cyrillic)':  '85191300',
	'Turkmen':  '85191303',
	'Welsh':  '85191304',
	'Ukrainian':  '85191305',
	'Uzbek (Latin)':  '85191306',
	'Slovenian':  '85191294',
	'Romansh':  '85191298',
	'Mohawk':  '85191247',
	'Yakut':  '85191290',
	'Greenlandic':  '85191260',
	'Latvian':  '85191275',
	'Turkish':  '85191302',
	'Georgian':  '85191257',
	'Vietnamese':  '85191307',
	'Sinhala':  '85191297',
	'Luxembourgish':  '85191277',
	'Hungarian':  '85191262',
	'Thai':  '85191301',
	'Wolof':  '85191292',
	'Japanese':  '85191270',
	'Frisian':  '85191283',
	'Kyrgyz':  '85191273',
	'Czech':  '85191250',
	'Persian':  '85191266',
	'Spanish':  '85191233',
	'Portuguese':  '85191243',
	'Lao':  '85191274',
	'Italian':  '85191269',
	'Macedonian (fyrom)':  '85191278',
	'Lithuanian':  '85191276',
	'Malay':  '85191244',
	'Yoruba':  '85191285',
	'Maltese':  '85191280',
	'Bulgarian':  '85191245',
	'Danish':  '85191251',
	'Upper sorbian':  '85191258',
	'Telugu':  '85191264',
	'Kiswahili':  '85191272',
	'Yi':  '85191248',
	'Bengali':  '85191239',
	'Korean':  '85191296',
	'English':  '85191235',
	'Arabic':  '85191238',
	'Sami (Southern)':  '85191286',
	'Tamazight (Latin)':  '85191232',
	'Amharic':  '85191253',
	'Kazakh':  '85191271',
	'Occitan':  '85191256',
	'Estonian':  '85191252',
	'Mongolian (Cyrillic)':  '85191281',
	'Divehi':  '85191279',
	'Serbian (Latin)':  '85191242'
}

class Language:
	def __init__(self, WALS_ID, ISO_ID, macroarea):
		self.WALS_ID = WALS_ID
		self.ISO_ID = ISO_ID
		self.macroarea = macroarea
def load_nodes(nodes_file):
	print("Loading nodes")
	nodes = dict()
	with open(nodes_file) as f:
		data = json.load(f)
		for i in range(len(data)):
			a_id = str(data[i][0])
			name = str(data[i][1])
			nodes[name] = a_id;
	return nodes

def loadLanguageCSV(input_file):
	languages = dict()
	with open(input_file,'r+') as f:
		reader = csv.reader(f)
		firstRow = True
		for row in reader:
			if firstRow:
				firstRow = False
				continue
			wals_id = row[3]
			iso_id = row[4]
			macroarea = row[8]
			languages[wals_id] = Language(wals_id,iso_id,macroarea)
	return languages

def createNodeForWALS(output_file,idCount):
	with open(output_file, 'w+') as csvfile1:
		writer1 = csv.writer(csvfile1,lineterminator = '\n')
		writer1.writerow(['CN',str(idCount),'World Atlas of Language Structures','description','The World Atlas of Language Structures (WALS) is a database of structural (phonological, grammatical, lexical) properties of languages gathered from descriptive materials.[1] It was first published by Oxford University Press as a book with CD-ROM in 2005, and was released as the second edition on the Internet in April 2008. It is maintained by the Max Planck Institute for Evolutionary Anthropology and by the Max Planck Digital Library. The editors are Martin Haspelmath, Matthew S. Dryer, David Gil and Bernard Comrie.','reference','https://wals.info/'])
		writer1.writerow(['CL','84872675',str(idCount),'is a kind of', 'contains'])
	return idCount + 1
def createNodeForLanguageFamilyAndGenus(output_file,idCount):
	with open(output_file,'a+') as csvfile1:
		writer1 = csv.writer(csvfile1,lineterminator = '\n')
		writer1.writerow(['CN',str(idCount),'Language Family'])
		writer1.writerow(['CL','85169301',str(idCount),'is related to', 'is related to'])
		writer1.writerow(['CL','85569520',str(idCount),'is a kind of', 'contains'])
		writer1.writerow(['SC',str(idCount)])
		idCount = idCount + 1

		writer1.writerow(['CN',str(idCount),'Language Genus'])
		writer1.writerow(['CL','85169301',str(idCount),'is related to', 'is related to'])
		writer1.writerow(['CL','85569520',str(idCount),'is a kind of', 'contains'])
		writer1.writerow(['SC',str(idCount)])
		idCount = idCount + 1

	return idCount		

def createNodesForFamilies(output_file,idCount,soup):
	print("Creating nodes for families")
	families = dict()
	with open(output_file,'a+') as csvfile1:
		writer1 = csv.writer(csvfile1,lineterminator = '\n')

		for family in soup.findAll('a',{'class':'Family'}):
			family_name = family['title']
			family_reference = family['href']

			writer1.writerow(['CN',str(idCount),family_name,'reference',family_reference])
			writer1.writerow(['CL','2',str(idCount),'is a kind of', 'contains'])
			families[family_name] = idCount

			idCount = idCount + 1
	return families,idCount

def createNodesForGenuses(output_file,idCount,soup,families):
	print("Creating nodes for genuses")
	genuses = dict()
	with open(output_file,'a+') as csvfile1:
		writer1 = csv.writer(csvfile1,lineterminator = '\n')
		counter = 0
		length = len(soup.findAll('a',{'class': 'Genus'}))

		for genus in soup.findAll('a',{'class': 'Genus'}):
			if(counter % 10 == 0):
				print str(counter * 100.0 / length) + "%"
			genus_name = genus['title']
			genus_reference = genus['href']

			writer1.writerow(['CN',str(idCount),genus_name,'reference',genus_reference])
			writer1.writerow(['CL','3',str(idCount),'is a kind of', 'contains'])

			response = requests.get(genus_reference)
			new_soup = BeautifulSoup(response.text,'html.parser')
			try:
				if(new_soup.find('a',{'class': 'Family'}) != None):
					family_name = str(new_soup.find('a',{'class': 'Family'})['title'])
					family_id = families.get(family_name)
					if(family_id != None):
						writer1.writerow(['CL',str(family_id),str(idCount),'is related to', 'is related to'])
			except:
				print("error on " + genus_reference)
			genuses[genus_name] = idCount

			idCount = idCount + 1
			counter = counter + 1
	return genuses,idCount

def createCertainCountryNodes(output_file,idCount):
	countries = dict()
	with open(output_file,'a+') as csvfile1:
		writer1 = csv.writer(csvfile1,lineterminator = '\n')	
		writer1.writerow(['CN',str(idCount),'South Sudan'])
		writer1.writerow(['CL','84865696',str(idCount),'is a kind of', 'contains'])
		countries['South Sudan'] = idCount
		idCount = idCount + 1

		writer1.writerow(['CN',str(idCount),'Serbia and Montenegro'])
		writer1.writerow(['CL','84865696',str(idCount),'is a kind of', 'contains'])
		countries['Serbia and Montenegro'] = idCount
		idCount = idCount + 1

		writer1.writerow(['CN',str(idCount),'Bosnia-Herzegovina'])
		writer1.writerow(['CL','84865696',str(idCount),'is a kind of', 'contains'])
		countries['Bosnia-Herzegovina'] = idCount
		idCount = idCount + 1

		writer1.writerow(['CN',str(idCount),'Democratic Republic of Congo'])
		writer1.writerow(['CL','84865696',str(idCount),'is a kind of', 'contains'])
		countries['Democratic Republic of Congo'] = idCount
		idCount = idCount + 1

		writer1.writerow(['CN',str(idCount),'Myanmar'])
		writer1.writerow(['CL','84865696',str(idCount),'is a kind of', 'contains'])
		countries['Myanmar'] = idCount
		idCount = idCount + 1
		
		writer1.writerow(['CN',str(idCount),'Palestinian West Bank and Gaza'])
		writer1.writerow(['CL','84865696',str(idCount),'is a kind of', 'contains'])
		countries['Palestinian West Bank and Gaza'] = idCount
		idCount = idCount + 1

	return idCount, countries

def createNodesForLanguages(output_file,idCount,soup,genuses,families,created_countries,list_of_languages,database_nodes):
	print("Creating language nodes")
	languages = dict()
	families_macroarea_links = list()
	genuses_macroarea_links = list()
	with open(output_file,'a+') as csvfile1:
		writer1 = csv.writer(csvfile1,lineterminator = '\n')
		counter = 0
		length = len(soup.findAll('a',{'class': 'Language'}))
		for language in soup.findAll('a',{'class': 'Language'}):
			if(counter % 10 == 0):
				print str(counter * 100.0 / length) + "%"
			language_url = language['href']
			language_name = language['title']
			wals_id = str(language_url)[-3:]
			iso_id = ""
			macroarea = ""
			this_genus = ""
			if(list_of_languages.get(wals_id) != None):
				iso_id =  list_of_languages.get(wals_id).ISO_ID
				#macroarea = list_of_languages.get(wals_id).macroarea
			response = requests.get(language_url)
			new_soup = BeautifulSoup(response.text,'html.parser')
			
			if(iso_id == ''):
				try:
					iso_id = str(new_soup.find('span',{'class': 'language_identifier iso639-3'}).find('a',href=True).get('title'))
				except:
					iso_id = ''

			if(existing_languages.get(language_name) != None):
				language_id = existing_languages.get(language_name)
				#print language_name, existing_languages.get(language_name)
			else:
				language_id = idCount
				if(iso_id != ""):
					writer1.writerow(['CN',str(language_id),language_name,'WALS_ID',wals_id,'ISO 639-3',str(iso_id),'reference',language_url])
				else:
					writer1.writerow(['CN',str(language_id),language_name,'WALS_ID',wals_id,'reference',language_url])

			if(this_genus == ''):
				try:
					this_genus = str(new_soup.find('a',{'class': 'Genus'}).get('title'))
					this_genus_id = genuses.get(this_genus)
					if(this_genus_id != None):
						writer1.writerow(['CL',str(this_genus_id),str(language_id),'belongs to', 'contains'])
					else:
						print this_genus
				except Exception as e:
					print e, language_url
					this_genus = ""
			writer1.writerow(['CL','85169301',str(language_id),'is a kind of', 'contains'])

			if(macroarea == ''):
				try:
					macroarea  = str(new_soup.find('a',{'class': 'Country'}).get('title'))
					macroarea_id = database_nodes.get(macroarea)
					if(macroarea_id != None):
						writer1.writerow(['CL',str(macroarea_id),str(language_id),'is the location of', 'is located in'])
					elif(created_countries.get(macroarea) != None):
						macroarea_id = created_countries.get(macroarea)
						writer1.writerow(['CL',str(macroarea_id),str(language_id),'is the location of', 'is located in'])						
					else:
						print(macroarea)

					language_family  = str(new_soup.find('a',{'class': 'Family'}).get('title'))
					if(language_family != None):
						language_family_id = families.get(language_family)
						if(language_family_id != None):
							if(language_family_id not in families_macroarea_links):
								families_macroarea_links.append(language_family_id)
								writer1.writerow(['CL',str(macroarea_id),str(language_family_id),'is the location of', 'is located in'])
						else:
							print language_family

					this_genus_id = genuses.get(this_genus)
					if(this_genus_id != None):
						if(this_genus_id not in genuses_macroarea_links):
							genuses_macroarea_links.append(this_genus_id)
							writer1.writerow(['CL',str(macroarea_id),str(this_genus_id),'is the location of', 'is located in'])
				except Exception as e:
					print e, language_url
					macroarea = ''


			idCount = idCount + 1
			counter = counter + 1
	return languages,idCount

def main():
	database_nodes = load_nodes(database_file)
	partial_languages = loadLanguageCSV(input_file)

	idCount = 1
	idCount = createNodeForWALS(output_file,idCount)
	idCount = createNodeForLanguageFamilyAndGenus(output_file,idCount)

	response = requests.get(start_url)
	soup = BeautifulSoup(response.text,'html.parser')

	families, idCount = createNodesForFamilies(output_file,idCount,soup)
	genuses, idCount = createNodesForGenuses(output_file,idCount,soup,families)

	#genuses = dict()
	idCount, countries = createCertainCountryNodes(output_file,idCount)
	languages, idCount = createNodesForLanguages(output_file,idCount,soup,genuses,families, countries, partial_languages,database_nodes)


if __name__ == '__main__':
	main()