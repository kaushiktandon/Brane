# -*- coding: utf-8 -*-

import requests
from BeautifulSoup import *
import sys
import codecs
import csv

reload(sys)
sys.setdefaultencoding('utf8')
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

output_file = "new_MIT_scrape.csv"

class Group:
	def __init__(self,title,url,ID):
		self.title = title
		self.url = url
		self.ID = ID
class Project:
	def __init__(self,title,url,ID):
		self.title = title
		self.url = url
		self.ID = ID
class Person:
	def __init__(self,name,url,ID):
		self.name = name
		self.url = url
		self.ID = ID
class Publication:
	def __init__(self,title,url,ID):
		self.title = title
		self.url = url
		self.ID = ID

research_topics_dict = {
	'robotics': '84866969',
	'design': '85165499',
	'bioengineering': '85188614',
	'construction': '85235845',
	'economy': '85173581',
	'extended intelligence': '84868723',
	'food': '85170358',
	'health': '85166036',
	'music': '85167115',
	'pharmaceuticals': '84876354',
	'privacy': '85235846',
	'storytelling':	'85170800',
	'imaging':	'84868861',
	'nonverbal behavior': '85235847',
	'ethics': '85166522',
	'computer science': '84866563',
	'cartography': '84868624',
	'academia': '85165549',
	'natural language processing': '85170908',
	'voice': '85171524',
	'autism research': '85235851',
	'ocean': '84871518',
	'climate change': '84870828',
	'bionics': '84867361',
	'marginalized communities': '85235848',
	'human-computer interaction': '84868723',
	'human-machine interaction': '84868723',
	'architecture': '85167796',
	'civic technology': '85235850'
}

startURL = "https://www.media.mit.edu/search/?extra_filter=all&start_year=1979&end_year=2018" #+ "&filter="

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

def createMITNode(output_file):
	print("Creating MIT Node")
	with open(output_file, 'w+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		writer.writerow(['CN',"1","MIT Media Lab","description",'The MIT Media Lab transcends known boundaries and disciplines by actively promoting a unique, antidisciplinary culture that emboldens unconventional mixing and matching of seemingly disparate research areas.','reference','https://www.media.mit.edu/about/mission-history/'])
		writer.writerow(['CL','85165552','1','is a kind of', 'contains'])
		writer.writerow(['CL','85169301','1','is owned by','owns'])
	print("Done creating MIT Node")

def getMaxPageNum(filter):
	print("Finding max page number for " + filter)
	pageNum = 1
	URL = startURL + "&filter=" + filter + "&page=" + str(pageNum)
	soup = getHTML(URL)


	while(soup != None and soup.find('title') != None and '404 Not Found' not in str(soup.find('title'))):
		pageNum = pageNum + 1
		URL = startURL + "&filter=" + filter + "&page=" + str(pageNum)
		print URL
		soup = getHTML(URL)

	print("Max page number for " + filter + " is " + str(pageNum - 1))
	return pageNum - 1
	

def parseGroups():
	maxPageNum = getMaxPageNum("group")
	currentPageNum = 1

	groups = list()
	groupStartURL = "https://www.media.mit.edu"
	while(currentPageNum <= maxPageNum):
		URL = startURL + "&filter=group&page=" + str(currentPageNum)
		soup = getHTML(URL)

		if(soup == None):
			print("Invalid Soup")
			continue

		titles = soup.findAll('h2',{'class': 'module-title'})
		links = soup.findAll('div',{'class': 'container-item listing-layout-item '})

		for i in range(len(links)):
			groups.append(Group(titles[i].text.replace("&#39;","'"),groupStartURL + links[i].get('data-href'),-1))
		currentPageNum = currentPageNum + 1
	#print soup.findAll('div',{'class': 'container-item listing-layout-item '})
	return groups


def createNodesFromGroupLinks(listOfGroups, currentID):
	print("Creating Group Nodes")
	length = len(listOfGroups)
	counter = 0
	with open(output_file, 'a+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')

		for group in listOfGroups:
			if group.url == 'https://www.media.mit.edu/groups/terrestrial-sensing/overview/' or group.url == 'https://www.media.mit.edu/groups/hundred-dollar-laptop/overview/' or group.url == 'https://www.media.mit.edu/groups/changing-places-consortium/overview/' or group.url == 'https://www.media.mit.edu/groups/digital-life/overview/': #Weird URL, doesn't work
				counter = counter + 1
				continue
			group.ID = currentID
			groupURL = group.url
			soup = getHTML(groupURL)

			description = str(soup.find('div',{'class' : 'more-text-full'}).text)
			description = description.replace("&nbsp;"," ").replace('ΓÇö','-').replace('ΓÇö','-').replace('ΓÇÖ',"'").replace("&amp;",'&').replace('ΓÇ£','"').replace('ΓÇ¥','"')

			writer.writerow(['CN',str(group.ID),str(group.title),'description',description,'reference',groupURL])
			writer.writerow(['CL','1',str(group.ID),'is researched by','researches'])
			currentID = currentID + 1

			try:
				topics =  str(soup.find('div',{'class': 'primary-block-meta'}).text)[16:].split("#")
				for topic in topics:
					if research_topics_dict.get(topic) == None:
						continue
					db_id = research_topics_dict.get(topic)
					writer.writerow(['CL',str(group.ID),str(db_id),'is related to','is related to'])
			except:
				print "No topics for: " + group.url

			if(counter % 5 == 0):
				print("Progress: ",counter * 100.0 / length, " %")
			counter = counter + 1
	print("Done creating group nodes")
	return currentID

def parseProjects():
	print("Parsing projects")
	maxPageNum = getMaxPageNum("project")
	currentPageNum = 1

	projects = list()
	dictOfPeopleInProjects = dict()

	projectStartURL = "https://www.media.mit.edu"
	while(currentPageNum <= maxPageNum):
		print("Getting projects from page " + str(currentPageNum))
		URL = startURL + "&filter=project&page=" + str(currentPageNum)
		soup = getHTML(URL)

		if(soup == None):
			print("Invalid Soup")
			continue

		titles = soup.findAll('h2',{'class': 'module-title'})
		links = soup.findAll('div',{'class': 'container-item listing-layout-item '})

		for i in range(len(links)):
			thisLink = projectStartURL + links[i].get('data-href')
			peopleLink = thisLink.replace('overview','people')
			projectTitle = titles[i].text.replace("&#39;","'")
			try:
				soup = getHTML(peopleLink)
				people = soup.findAll('div',{'class':'module-title'})
			except:
				continue


			for person in people:
				name = str(person.text).replace("&#39;","'")
				if(dictOfPeopleInProjects.get(name) == None):
					tempList = list()
					tempList.append(projectTitle)
					dictOfPeopleInProjects[name] = tempList
				else:
					dictOfPeopleInProjects[name].append(projectTitle)

			projects.append(Project(projectTitle,thisLink,-1))

		currentPageNum = currentPageNum + 1

	return projects,dictOfPeopleInProjects

def createNodesFromProjectLinks(listOfProjects,listOfGroups,currentID):
	print("Creating Project Nodes")
	length = len(listOfProjects)
	counter = 0

	projectID_dict = dict()

	with open(output_file, 'a+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')

		for project in listOfProjects:
			soup = getHTML(project.url)
			try:
				description = str(soup.find('div',{'class' : 'more-text-full'}).text)
				description = description.replace("&nbsp;"," ").replace('ΓÇö','-').replace('ΓÇö','-').replace('ΓÇÖ',"'").replace("&amp;",'&').replace('ΓÇ£','"').replace('ΓÇ¥','"')
			except:
				print("Description error for: " + project.url)
				description = ""
			project.ID = currentID
			currentID = currentID + 1

			writer.writerow(['CN',str(project.ID), str(project.title),'description',description,'reference',project.url])
			writer.writerow(['CL','84871641',str(project.ID),'is a kind of', 'contains'])
			projectID_dict[project.title] = project.ID

			#Link projects to group
			potentialGroups = soup.findAll('a',href=True)
			groups = list()
			for group in potentialGroups:
				if '/groups/' not in group['href']:
					continue
				if group['href'] not in groups:
					groups.append(group['href'])

			for group in groups:
				for fullGroup in listOfGroups:
					if group == fullGroup.url:
						ID = fullGroup.ID
						writer.writerow(['CL',str(ID),str(project.ID),'is reasearched by','researches'])
						break
			#Link projects to database node ID
			try:
				topics =  str(soup.find('div',{'class': 'primary-block-meta'}).text)[16:].split("#")
				for topic in topics:
					if research_topics_dict.get(topic) == None:
						continue
					db_id = research_topics_dict.get(topic)
					writer.writerow(['CL',str(project.ID),str(db_id),'is related to','is related to'])
			except:
				print "No topics for: " + project.url

			if(counter % 5 == 0):
				print("Progress: ",counter * 100.0 / length, " %")
			counter = counter + 1
	print("Done creating project nodes")
	return currentID, projectID_dict

def parsePeople():
	print("Parsing people")
	maxPageNum = getMaxPageNum("person")
	currentPageNum = 1

	people = list()
	peopleStartURL = "https://www.media.mit.edu"
	while(currentPageNum <= maxPageNum):
		print("Getting people from page " + str(currentPageNum))
		URL = startURL + "&filter=person&page=" + str(currentPageNum)
		soup = getHTML(URL)

		if(soup == None):
			print("Invalid Soup")
			continue

		titles = soup.findAll('h2',{'class': 'module-title'})
		links = soup.findAll('div',{'class': 'container-item listing-layout-item '})

		for i in range(len(links)):
			people.append(Person(titles[i].text.replace("&#39;","'"),peopleStartURL + links[i].get('data-href'),-1))
		currentPageNum = currentPageNum + 1
	return people

def createNodesFromPeopleLinks(listOfPeople,projectID_dict,listOfPeopleInProjects,currentID):
	print("Creating People Nodes")
	length = len(listOfPeople)
	peopleID_dict = dict()
	counter = 0
	with open(output_file, 'a+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')

		for person in listOfPeople:
			soup = getHTML(person.url)
			try:
				description = str(soup.find('div',{'class' : 'more-text-full'}).text)
				description = description.replace("&nbsp;"," ").replace('ΓÇö','-').replace('ΓÇö','-').replace('ΓÇÖ',"'").replace("&amp;",'&').replace('ΓÇ£','"').replace('ΓÇ¥','"')
			except:
				print("Description error for: " + person.url)
				description = ""
			person.ID = currentID
			currentID = currentID + 1

			writer.writerow(['CN',str(person.ID), str(person.name),'description',description,'reference',person.url])
			writer.writerow(['CL','85165565',str(person.ID),'is a kind of', 'contains'])
			peopleID_dict[person.name] = person.ID

			if(listOfPeopleInProjects.get(person.name) != None):
				for projectName in listOfPeopleInProjects.get(person.name):
					projectID = projectID_dict.get(projectName)
					writer.writerow(['CL',str(person.ID),str(projectID),'is conducted by','conducts'])


			if(counter % 5 == 0):
				print("Progress: ",counter * 100.0 / length, " %")
			counter = counter + 1
	print("Done creating people nodes")
	return currentID, peopleID_dict

def parsePublications():
	print("Parsing publications")
	maxPageNum = getMaxPageNum("publication")
	currentPageNum = 1

	publications = list()
	publicationStartURL = "https://www.media.mit.edu"
	while(currentPageNum <= maxPageNum):
		print("Getting publications from page " + str(currentPageNum))
		URL = startURL + "&filter=publication&page=" + str(currentPageNum)
		soup = getHTML(URL)

		if(soup == None):
			print("Invalid Soup")
			continue

		titles = soup.findAll('h2',{'class': 'module-title'})
		links = soup.findAll('div',{'class': 'container-item listing-layout-item '})

		for i in range(len(links)):
			publications.append(Publication(titles[i].text.replace("&#39;","'"),publicationStartURL + links[i].get('data-href'),-1))
		currentPageNum = currentPageNum + 1
	return publications

def createNodesFromPublicationsLinks(listOfPublications,projectID_dict,peopleID_dict,currentID):
	print("Creating Publication Nodes")
	length = len(listOfPublications)
	counter = 0
	with open(output_file, 'a+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')

		for publication in listOfPublications:
			soup = getHTML(publication.url)
			try:
				description = str(soup.findAll('div',{'class' : 'main-copy'})[1].text)[8:]
				description = description.replace("&nbsp;"," ").replace('ΓÇö','-').replace('ΓÇö','-').replace('ΓÇÖ',"'").replace("&amp;",'&').replace('ΓÇ£','"').replace('ΓÇ¥','"')
				if 'Technical publication summary:' in description:
					description = description[30:]
			except:
				print("Description error for: " + publication.url)
				description = ""
			publication.ID = currentID
			currentID = currentID + 1

			writer.writerow(['CN',str(publication.ID), str(publication.title),'description',description,'reference',publication.url])
			writer.writerow(['CL','84878840',str(publication.ID),'is a kind of', 'contains'])

			try:
				project_titles = soup.findAll('a',href=True)
				for potential_title in project_titles:
					if '/projects/' not in str(potential_title['href']):
						continue
					project = potential_title.text
					project_id = projectID_dict.get(project)
					if(project_id != None):
						writer.writerow(['CL',str(project_id),str(publication.ID),'is related to', 'is related to'])
			except:
				print("Error in getting project titles for " + publication.url)
				
			try:
				people_names = soup.findAll('a',href=True)
				for potential_person in people_names:
					if '/people/' not in str(potential_person['href']):
						continue
					person = str(potential_person.text).replace("&#39;","'")

					person_id = peopleID_dict.get(person)
					if(person_id != None):
						writer.writerow(['CL',str(person_id),str(publication.ID),'is authored by','is the author of'])
			except:
				print("Error in getting people in " + publication.url)
				

			if(counter % 5 == 0):
				print("Progress: ",counter * 100.0 / length, " %")
			counter = counter + 1
	print("Done creating people nodes")
	return currentID

def main():
	createMITNode(output_file)
	currentID = 2

	listOfGroups = parseGroups()	
	currentID = createNodesFromGroupLinks(listOfGroups,currentID)

	listOfProjects, listOfPeopleInProjects = parseProjects()
	currentID, projectID_dict = createNodesFromProjectLinks(listOfProjects,listOfGroups,currentID)

	listOfPeople = parsePeople()
	currentID, peopleID_dict = createNodesFromPeopleLinks(listOfPeople,projectID_dict,listOfPeopleInProjects,currentID)

	listOfPublications = parsePublications()
	currentID = createNodesFromPublicationsLinks(listOfPublications,projectID_dict,peopleID_dict,currentID)
if __name__ == '__main__':
	main()