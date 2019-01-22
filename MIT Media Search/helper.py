# -*- coding: utf-8 -*-

import requests
from BeautifulSoup import *
import sys
import codecs
import csv

reload(sys)
sys.setdefaultencoding('utf8')
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

input_file = "scrape.csv"
output_file = "scrape_with_links.csv"

def loadPublications():
	print("Loading publications")
	publications = list()
	publication_ids = list()
	with open(input_file,'r+') as f:
		reader = csv.reader(f)
		for row in reader:
			if len(row) < 6 or row[0] != 'CN' or 'publications' not in row[6]:
				continue
			ID = row[1]
			URL = row[6]
			publications.append(URL)
			publication_ids.append(ID)
	print("Loaded publications")
	return publications, publication_ids

def loadPeople():
	print("Loading people")
	people = dict()
	with open(input_file,'r+') as f:
		reader = csv.reader(f)
		for row in reader:
			if len(row) < 6 or row[0] != 'CN' or 'people' not in row[6]:
				continue
			ID = row[1]
			URL = row[6]
			people[URL] = ID
	print("Loaded people")
	return people

def getHTML(url):
	''' Uses BeautifulSoup to get the HTML for a page
		Args:
			url: URL of page to get HTML for
		Returns:
			Beautiful Soup object with HTML
	'''
	try:
		r = requests.get(url)
		return BeautifulSoup(r.text)
	except:
		print("Couldn't get HTML for: " + url)

def main():
	publications, publication_ids = loadPublications()
	people = loadPeople()
	with open(output_file, 'w+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')

		length = len(publications)
		for i in range(len(publications)):
			publication = publications[i]
			publication_id = publication_ids[i]

			soup = getHTML(publication)
			
			try:
				people_names = soup.findAll('a',href=True)
			except:
				print("OOPS")
				continue
			for potential_person in people_names:
				if '/people/' not in str(potential_person['href']):
					continue

				person = "https://www.media.mit.edu" + potential_person['href']

				person_id = people.get(person)
				if(person_id != None):
					writer.writerow(['CL',str(person_id),str(publication_id),'is authored by','is the author of'])

			if(i % 10 == 0):
				print("Progress: ",i * 100.0 / length, " %")


if __name__ == '__main__':
	main()


