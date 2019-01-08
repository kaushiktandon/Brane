# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import sys
import codecs
import csv
import time

reload(sys)
sys.setdefaultencoding('utf8')
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.setrecursionlimit(1000000)

output_file = "scrape.csv"

ranks = {
	'domain': '1',
	'superkingdom': '1',
	'kingdom': '2',
	'phylum': '3',
	'class':'4',
	'order': '5',
	'family': '6',
	'genus': '7',
	'species': '85166321'
}

def updateSpeciesNode(output_file):
	with open(output_file, 'w+') as csvfile1:
		writer1 = csv.writer(csvfile1,lineterminator = '\n')
		writer1.writerow(['UN','85166321','Species (taxonomy)'])

def createRankNodes(output_file):
	with open(output_file, 'w+') as csvfile1:
		writer1 = csv.writer(csvfile1,lineterminator = '\n')

		writer1.writerow(['CN','1','Domain (taxonomy)','t2','Superkingdom'])
		writer1.writerow(['CL','85166482','1','is a kind of', 'contains'])

		writer1.writerow(['CN','2','Kingdom (taxonomy)'])
		writer1.writerow(['CL','85166482','2','is a kind of', 'contains'])

		writer1.writerow(['CN','3','Phylum (taxonomy)'])
		writer1.writerow(['CL','85166482','3','is a kind of', 'contains'])

		writer1.writerow(['CN','4','Class (taxonomy)'])
		writer1.writerow(['CL','85166482','4','is a kind of', 'contains'])

		writer1.writerow(['CN','5','Order (taxonomy)'])
		writer1.writerow(['CL','85166482','5','is a kind of', 'contains'])

		writer1.writerow(['CN','6','Family (taxonomy)'])
		writer1.writerow(['CL','85166482','6','is a kind of', 'contains'])

		writer1.writerow(['CN','7','Genus (taxonomy)'])
		writer1.writerow(['CL','85166482','7','is a kind of', 'contains'])

	return 8
def getHTML(url):
	''' Uses BeautifulSoup to get the HTML for a page
		Args:
			url: URL of page to get HTML for
		Returns:
			Beautiful Soup object with HTML
	'''
	try:
		r = requests.get(url)
		return BeautifulSoup(r.text,'html.parser')
	except Exception as e:
		print(e)
		print("Couldn't get HTML for: " + url)

def load_urls_from_file(filename):
	file_urls = list()
	with open(filename,'r+') as f:
		for line in f:
			temp_url = line[:line.find(">")].strip()
			file_urls.append(temp_url)
	return file_urls


def createEntityNodes(output_file,start_id):
	allEntities = dict()

	topLevels = ['https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Undef&name=Archaea&lvl=3&srchmode=1&keep=1&unlock','https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Tree&id=2&lvl=3&srchmode=1&keep=1&unlock',
	'https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Undef&name=Eukaryota&lvl=3&srchmode=1&keep=1&unlock','https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Undef&name=Viroids&lvl=3&srchmode=1&keep=1&unlock',
	'https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Undef&name=Viroids&lvl=3&srchmode=1&keep=1&unlock','https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Tree&id=28384&lvl=3&srchmode=1&keep=1&unlock','https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Tree&id=12908&lvl=3&srchmode=1&keep=1&unlock']

	urls = list()
	start_time = time.time()
	for start_url in topLevels:
		numUrls = len(urls)
		print("Getting URLs from " + start_url)
		if(start_url == 'https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Tree&id=2&lvl=3&srchmode=1&keep=1&unlock'):
			page_urls = load_urls_from_file("large_page.html")
			print("URLs gotten")
			for page_url in page_urls:
				new_url = 'https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/' + page_url
				if('mode=Tree' in new_url):
					new_url = new_url.replace('mode=Tree','mode=Info')
				urls.append(new_url)
		elif start_url == 'https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Tree&id=28384&lvl=3&srchmode=1&keep=1&unlock':
			page_urls = load_urls_from_file("large_page_2.html")
			print("URLs gotten")
			for page_url in page_urls:
				new_url = 'https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/' + page_url
				if('mode=Tree' in new_url):
					new_url = new_url.replace('mode=Tree','mode=Info')
				urls.append(new_url)
			#soup = BeautifulSoup(open("large_page.html"), "html.parser")
		else:
			soup = getHTML(start_url)
			print("URLs gotten")
			for link in soup.findAll('a',href=True):
				if 'wwwtax' in link['href'] and 'mode=Undef' not in link['href']:
					new_url = 'https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/' + link['href']
					if('mode=Tree' in new_url):
						new_url = new_url.replace('mode=Tree','mode=Info')
					urls.append(new_url)
		print(str(len(urls) - numUrls) + " URLs added")
	length = len(urls)
	myCounter = 0.0
	print length
	for url in urls:
		if(myCounter % 25 == 0):
			print("Progress: ",myCounter * 100.0 / length, " %")
		myCounter = myCounter + 1
		print url
		soup = getHTML(url)
		if(soup == None):
			continue
		#soup = getHTML('https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=2026736&lvl=3&lin=f&keep=1&srchmode=1&unlock')
		tables = soup.findAll('td',{'valign':'top'})
		if(len(tables) == 0):
			continue
		table = tables[0]

		entityName = ""
		rank = ""
		parent = ""
		txid = -1
		row1 = True
		row2 = True
		rankRow = False

		synonymRow = True
		synonyms = list()

		for row in table:
			if row1:
				entityName = row.text.replace('┬á1','')
				row1 = False
			elif row2:
				row_text = str(row)
				txid = int(row[13:].strip())
				row2 = False
			elif rankRow:
				rank = row.text
				rankRow = False
			elif('Rank' in row and rank == ""):
				rankRow = True
			else:
				try:
					if 'synonym' in row.text:
						row_text = str(row.text)
						counter = 0
						while(row_text.find('synonym:',counter) != -1):
							synonym =  row_text[row_text.find('synonym',counter):row_text.find('\n',counter+10)]
							if('"' in synonym):
								ind = synonym.find('"')
								synonym = synonym[ind+1:synonym.find('"',ind+1)].strip()
							else:
								synonym = synonym[9:].strip()
							synonyms.append(synonym)
							counter = row_text.find('synonym',counter+1)
						#print row_text.rfind('synonym')
					elif 'Lineage' in row.text:
						lineage = row.text
						parent = lineage[16:].split(';')[-1].strip()
				except Exception as e:
					#print(e)
					continue

		reference = 'https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=' + str(txid) + '&lvl=3&lin=f&keep=1&srchmode=1&unlock'
		#print rank, ranks.get(rank), entityName.replace('Â 1)',"").replace('┬á1)',"") #Fix unicode issue
		#Check if parent still works once replace works

		#print entityName, txid,reference, rank, ranks.get(rank), synonyms, parent
		with open(output_file, 'a+') as csvfile1:
			writer1 = csv.writer(csvfile1,lineterminator = '\n')
			if(len(synonyms) == 0):
				writer1.writerow(['CN',str(start_id),entityName,'reference',reference,'NBCI:txid',str(txid)])
			elif(len(synonyms) == 1):
				writer1.writerow(['CN',str(start_id),entityName,'t2',synonyms[0],'reference',reference,'NBCI:txid',str(txid)])
			elif(len(synonyms) == 2):
				writer1.writerow(['CN',str(start_id),entityName,'t2',synonyms[0],'t3',synonyms[1],'reference',reference,'NBCI:txid',str(txid)])
			elif(len(synonyms) == 3):
				writer1.writerow(['CN',str(start_id),entityName,'t2',synonyms[0],'t3',synonyms[1],'t4',synonyms[2],'reference',reference,'NBCI:txid',str(txid)])
			else:
				writer1.writerow(['CN',str(start_id),entityName,'t2',synonyms[0],'t3',synonyms[1],'t4',synonyms[2],'t5',synonyms[3],'reference',reference,'NBCI:txid',str(txid)])
			allEntities[entityName] = str(start_id)

			if(ranks.get(rank) != None):
				writer1.writerow(['CL',str(ranks.get(rank)),str(start_id),'is a kind of', 'contains'])
			else:
				writer1.writerow(['CL','84871345',str(start_id),'is a kind of', 'contains'])

			if(allEntities.get(parent) != None):
				writer1.writerow(['CL',str(allEntities.get(parent)),str(start_id),'is contained in','contains'])
			else:
				print parent + " not found"

			start_id = start_id + 1
	endTime = time.time()
	print(str(endTime-startTime) + " seconds to run")
	return start_id

def main():
	updateSpeciesNode(output_file)
	start_id = createRankNodes(output_file)
	start_id = createEntityNodes(output_file,start_id)


if __name__ == '__main__':
	main()
