# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import sys
import codecs
import csv
import time
import json

reload(sys)
sys.setdefaultencoding('utf8')
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

mitacs_url = 'https://www.mitacs.ca/en/projects'

nodes_file = 'nodes_ca15fd43dfaeb80eb8c125735e0479b0.data.json'
output_file = 'mitacs_output.csv'
partner_file = 'unlinked_partners.csv'

canadaProvinces = {
	'Ontario (Canada)': '85244892',
	'British Columbia (Canada)':'85244926',
	'Alberta (Canada)': '85246328',
	'Manitoba (Canada)': '85246508',
	'Newfoundland and Labrador (Canada)': '85246618',
	'Saskatchewan (Canada)': '85246622',
	'Nova Scotia (Canada)': '85247137',
	'Prince Edward Island (Canada)': '85247471',
	'New Brunswick (Canada)': '85248683',
	'Yukon Territory (Canada)': '85263563',
	'Northwest Territories (Canada)': '85271674',
	'Quebec (Canada)': '85178447'
}
categoryList = {
	'Engineering': '84866671',
	'Life science': '84863609',
	'Mathematics': '84874452',
	'Natural science': '84863609',
	'Social science': '84866695'
}

def createOutputFile(output_file):
	with open(output_file, 'w+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')	
def linkToNonProfit(output_file):
	with open(output_file, 'a+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		writer.writerow(['CL','85165562','85294980','is a kind of', 'contains'])
def linkToCanadaProvinces(output_file,canadaProvinces):
	with open(output_file, 'a+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		for province, provinceID in canadaProvinces.iteritems():
			writer.writerow(['CL','85294980',str(provinceID), 'is related to', 'is related to'])
def createNodeForProgram(output_file,idCount):
	with open(output_file, 'a+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		writer.writerow(['CN',str(idCount),'Program'])
		writer.writerow(['CL','84863710',str(idCount),'is a kind of', 'contains'])	
		writer.writerow(['SC',str(idCount)])
		idCount = idCount + 1

	return idCount

def createIndividualProgramNodes(output_file,idCount,programID):
	with open(output_file, 'a+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		writer.writerow(['CN',str(idCount),'Accelerate (Mitacs)', 'reference', 'https://www.mitacs.ca/en/programs/accelerate'])
		writer.writerow(['CL',str(programID),str(idCount), 'is a kind of', 'contains'])
		writer.writerow(['CL','85294980',str(programID),'is conducted by', 'conducts'])
		idCount = idCount + 1

		writer.writerow(['CN',str(idCount),'Elevate (Mitacs)', 'reference', 'https://www.mitacs.ca/en/programs/elevate'])
		writer.writerow(['CL',str(programID),str(idCount), 'is a kind of', 'contains'])
		writer.writerow(['CL','85294980',str(programID),'is conducted by', 'conducts'])
		idCount = idCount + 1

		writer.writerow(['CN',str(idCount),'Globalink (Mitacs)', 'reference', 'https://www.mitacs.ca/en/programs/globalink'])
		writer.writerow(['CL',str(programID),str(idCount), 'is a kind of', 'contains'])
		writer.writerow(['CL','85294980',str(programID),'is conducted by', 'conducts'])
		globalID = idCount
		idCount = idCount + 1

		writer.writerow(['CN',str(idCount),'Globalink - Come to Canada (Mitacs)', 'reference', 'https://www.mitacs.ca/en/programs/globalink/come-to-canada'])
		writer.writerow(['CL',str(globalID),str(idCount), 'is categorised as', 'categorises'])
		writer.writerow(['CL','85294980',str(programID),'is conducted by', 'conducts'])
		idCount = idCount + 1

		writer.writerow(['CN',str(idCount),'Globalink - Travel from Canada (Mitacs)', 'reference', 'https://www.mitacs.ca/en/programs/globalink/travel-from-canada'])
		writer.writerow(['CL',str(globalID),str(idCount), 'is categorised as', 'categorises'])
		writer.writerow(['CL','85294980',str(programID),'is conducted by', 'conducts'])
		idCount = idCount + 1

		writer.writerow(['CN',str(idCount),'Training (Mitacs)', 'reference', 'https://www.mitacs.ca/en/programs/training/about-training'])
		writer.writerow(['CL',str(programID),str(idCount), 'is a kind of', 'contains'])
		writer.writerow(['CL','85294980',str(programID),'is conducted by', 'conducts'])
		idCount = idCount + 1

		writer.writerow(['CN',str(idCount),'Canadian Science Policy Fellowship (Mitacs)', 'reference', 'https://www.mitacs.ca/en/programs/canadian-science-policy-fellowship'])
		writer.writerow(['CL',str(programID),str(idCount), 'is a kind of', 'contains'])
		writer.writerow(['CL','85294980',str(programID),'is conducted by', 'conducts'])
		idCount = idCount + 1

		writer.writerow(['CN',str(idCount),'Career Connect (Mitacs)', 'reference', 'https://www.mitacs.ca/en/career-connect'])
		writer.writerow(['CL',str(programID),str(idCount), 'is a kind of', 'contains'])
		writer.writerow(['CL','85294980',str(programID),'is conducted by', 'conducts'])
		idCount = idCount + 1

	return idCount

def loadProjectURLS(maxPageNumber):
	project_urls = list()
	for pageNumber in range(1,maxPageNumber):
		page_url = mitacs_url + "?page=" + str(pageNumber)
		print page_url
		response = requests.get(page_url)
		soup = BeautifulSoup(response.text,'html.parser')

		for project in soup.findAll('div',{'class': 'projects-details'}):
			project_url = 'https://www.mitacs.ca' +  project.find('a').get('href')
			project_urls.append(project_url)
	print (len(project_urls)) 
	return project_urls

def load_nodesJSON(nodes_file, everything):
	nodes = dict()
	print ("Loading nodes")
	with open(nodes_file) as f:
		for line in f:
			data = json.loads(line)
			a_id = str(data['data']['_key'])
			name = str(data['data']['t'])
			if(name == ' '):
				continue
			if(everything):
				nodes[name] = a_id
			else:
				if('(' in name and ')' in name):
					name = name[0:name.find('(')-1].strip()
					nodes[name] = a_id
	print ("Loaded nodes")
	return nodes

def createPartnerNode(output_file,idCount):
	with open(output_file, 'a+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		writer.writerow(['CN',str(idCount),'Partner'])
		writer.writerow(['CL','85839968',str(idCount), 'is a kind of', 'contains'])
		writer.writerow(['SC',str(idCount)])
		idCount = idCount + 1

	return idCount

def createSupervisorNode(output_file,idCount):
	with open(output_file, 'a+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		writer.writerow(['CN',str(idCount),'Faculty Supervisor'])
		writer.writerow(['CL','85165565',str(idCount), 'is a kind of', 'contains'])
		writer.writerow(['SC',str(idCount)])
		idCount = idCount + 1

	return idCount

def main():
	nodes = load_nodesJSON(nodes_file,True)
	partial_nodes = load_nodesJSON(nodes_file,False)

	createOutputFile(output_file)
	createOutputFile(partner_file)
	linkToNonProfit(output_file)
	linkToCanadaProvinces(output_file,canadaProvinces)

	idCount = 1
	idCount = createNodeForProgram(output_file,idCount)
	idCount = createIndividualProgramNodes(output_file,idCount,idCount-1)
	idCount = createSupervisorNode(output_file,idCount)
	supervisorClusterID = idCount - 1
	idCount = createPartnerNode(output_file,idCount)
	partnerClusterID = idCount - 1

	maxPageNumber = 491
	project_urls = loadProjectURLS(maxPageNumber)

	createdSectors = dict()
	createdUniversities = dict()
	createdSupervisors = dict()
	createdStudents = dict()
	createdPartners = dict()

	count = 0.0
	length = len(project_urls)
	with open(output_file, 'a+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		for project_url in project_urls:
			count = count + 1
			if (count % 16 == 0):
				print (count * 100 / length, '%')
			#print project_url
			response = requests.get(project_url)
			soup = BeautifulSoup(response.text,'html.parser')
			project_name = soup.find('h1',{'id': 'node-title'}).text
			project_description = soup.find('div',{'class':'field-item even'}).text
			province = soup.find('div',{'class': 'field-name-field-province'})
			project_language = 'english'
			if(province != None):
				province = province.find('div',{'class': 'field-item even'}).text
				provinceID = canadaProvinces.get(province + " (Canada)")
				if(provinceID == None):
					if(province == "NL"):
						provinceID = '85246618'
					else:
						print province + " not found "

			project_id = idCount
			idCount = idCount + 1
			writer.writerow(['CN',str(project_id),project_name + ' (Project)', 'description', project_description, 'reference', project_url])
			writer.writerow(['CL','84871641', str(project_id), 'is a kind of', 'contains'])
			writer.writerow(['CL','85294980', str(project_id), 'is conducted by', 'conducts'])
			if(provinceID != None):
				writer.writerow(['CL',str(provinceID),str(project_id),'is located in', 'is the location of'])

			disciplineFULL = soup.find('div',{'class':'field-name-field-discipline-taxonomy'})
			if(disciplineFULL != None):
				discipline = str(disciplineFULL.find('div',{'class':'field-item'}).text)
				disciplineID = None
				disciplineURL = str(disciplineFULL.find('div',{'class':'field-item'}).find('a',href=True)['href'])
				if(disciplineURL[0:4] == '/fr/'):
					disciplineURL = 'en/' + disciplineURL[4:]
					disciplineURL = 'https://www.mitacs.ca/' + disciplineURL
					response2 = requests.get(disciplineURL)
					soup2 = BeautifulSoup(response2.text,'html.parser')
					discipline = str(soup2.find('h1',{'id': 'page-title'}).text)
					project_language = 'french'
				try:
					if(nodes.get(discipline) != None):
						disciplineID = nodes.get(discipline)
					elif('-' in discipline and '/' not in discipline):
						discipline = discipline.split('-')[1].title() + " " + discipline.split('-')[0].lower()
						discipline = discipline.strip()
						if(nodes.get(discipline) != None):
							disciplineID = nodes.get(discipline)
					elif('-' not in discipline and '/' in discipline):
						discipline = discipline.split('/')[0].strip()
						if(nodes.get(discipline) != None):
							disciplineID = nodes.get(discipline)
					elif('-' in discipline and '/' in discipline):
						discipline = discipline.split('/')[0]
						discipline = discipline.split('-')[1].title()  + discipline.split('-')[0].lower()
						discipline = discipline.strip()
						if(nodes.get(discipline) != None):
							disciplineID = nodes.get(discipline)
					elif(',' in discipline):
						discipline = discipline.split(',')[0]
						if(nodes.get(discipline) != None):
							disciplineID = nodes.get(discipline)
					elif(discipline[-1] == 's'):
						discipline = discipline[:-1]
						if(nodes.get(discipline) != None):
							disciplineID = nodes.get(discipline)
				except Exception as e:
					pass
				if(disciplineID == None):
					discipline = discipline.title()
					disciplineID = nodes.get(discipline)
				if(disciplineID != None):
					writer.writerow(['CL',str(project_id),str(disciplineID),'is related to', 'is related to'])
				else:
					print discipline + " not found "


			sectorFULL = soup.find('div',{'class':'field-name-field-sector-taxonomy'})
			if(sectorFULL != None):
				sector = str(sectorFULL.find('div',{'class': 'field-item'}).text)
				sectorID = None

				sectorURL = str(sectorFULL.find('div',{'class':'field-item'}).find('a',href=True)['href'])
				if(sectorURL[0:4] == '/fr/'):
					sectorURL = 'en/' + sectorURL[4:]
					sectorURL = 'https://www.mitacs.ca/' + sectorURL
					response2 = requests.get(sectorURL)
					soup2 = BeautifulSoup(response2.text,'html.parser')
					sector = str(soup2.find('h1',{'id': 'page-title'}).text)
					project_language = 'french'

				if(createdSectors.get(sector + " (Sector)") != None):
					sectorID = nodes.get(sector)
				elif(nodes.get(sector) != None):
					sectorID = nodes.get(sector)
				elif(nodes.get(sector + " (Sector)") != None):
					sectorID = nodes.get(sector + " (Sector)")
					print(sector + " (Sector)")
				elif(nodes.get(sector[:-1]) != None):
					sectorID = nodes.get(sector[:-1])
				elif('and' in sector and nodes.get(sector.split('and')[0].strip()) != None):
					sectorID = nodes.get(sector.split('and')[0].strip())
				else:
					sectorID = idCount
					idCount = idCount + 1

					writer.writerow(['CN',str(sectorID),sector + " (Sector)"])
					writer.writerow(['CL','85165971',str(sectorID),'is a kind of','contains'])
					print("Created: " + sector)
					createdSectors[sector + " (Sector)"] = str(sectorID)

				if(sectorID != None):
					writer.writerow(['CL',str(sectorID),str(project_id),'is categorised as', 'categorises'])

			university = soup.find('div',{'class':'field-name-field-university-taxonomy'})
			if(university != None):
				university = str(university.find('div',{'class':'field-item'}).text)
				universityID = None
				if(createdUniversities.get(university) != None):
					universityID = createdUniversities.get(university)
				elif(nodes.get(university) != None):
					universityID = nodes.get(university)
				elif(partial_nodes.get(university) != None):
					universityID = partial_nodes.get(university)
				else:
					universityID = idCount
					idCount = idCount + 1

					writer.writerow(['CN',str(universityID),university])
					writer.writerow(['CL','85165550',str(universityID),'is a kind of', 'contains'])
					print ("Created: " + university)
					createdUniversities[university] = str(universityID)
				if(universityID != None):
					writer.writerow(['CL',str(universityID),str(project_id),'is affiliated with','is affiliated with'])


			if(project_language == 'french'):
				writer.writerow(['CL',str(project_id),'85191241','is related to', 'is related to'])
			else:
				writer.writerow(['CL',str(project_id),'85191235','is related to', 'is related to'])

			supervisor = soup.find('div',{'class':'field-name-field-faculty-supervisor'})
			supervisorID = None
			if(supervisor != None):
				supervisor = str(supervisor.find('div',{'class':'field-item'}).text)
				if(createdSupervisors.get(supervisor) != None):
					supervisorID = createdSupervisors.get(supervisor)
				elif(nodes.get(supervisor) != None):
					supervisorID = nodes.get(supervisor)
				elif(partial_nodes.get(supervisor) != None):
					supervisorID = partial_nodes.get(supervisor)
				else:
					supervisorID = idCount
					idCount = idCount + 1

					writer.writerow(['CN',str(supervisorID),supervisor])
					writer.writerow(['CL',str(supervisorClusterID),str(supervisorID),'is a kind of','contains'])
					writer.writerow(['CL',str(supervisorID),str(project_id),'is conducted by', 'conducts'])
					createdSupervisors[supervisor] = str(supervisorID)

			student = soup.find('div',{'class':'field-name-field-student-name'})
			if(student != None):
				studentID = None
				student = str(student.find('div',{'class':'field-item'}).text)
				if(createdStudents.get(student) != None):
					studentID = createdStudents.get(student)
				elif(nodes.get(student) != None):
					studentID = nodes.get(student)
				elif(partial_nodes.get(student) != None):
					studentID = partial_nodes.get(student)
				else:
					studentID = idCount
					idCount = idCount + 1

					writer.writerow(['CN',str(studentID),student])
					writer.writerow(['CL','85166882',str(studentID),'is a kind of','contains'])
					if(supervisorID != None):
						writer.writerow(['CL',str(supervisorID),str(studentID),'is supervised by','supervises'])
					writer.writerow(['CL',str(studentID),str(project_id),'is conducted by', 'conducts'])
					createdStudents[student] = str(studentID)

			partner = soup.find('div',{'class':'field-name-field-partner-taxonomy'})
			if(partner != None):
				partnerID = None
				partners = str(partner.find('div',{'class':'field-item'}).text)
				list_of_partners = list()
				if(',' in partners):
					for a in partners.split(','):
						list_of_partners.append(a.strip())
				else:
					list_of_partners.append(partners)
				for partner in list_of_partners:
					if(createdPartners.get(partner) != None):
						studentID = createdPartners.get(partner)
					elif(nodes.get(partner) != None):
						partnerID = nodes.get(partner)
					elif(partial_nodes.get(partner) != None):
						partnerID = partial_nodes.get(partner)
					else:
						partnerID = idCount
						idCount = idCount + 1

						writer.writerow(['CN',str(partnerID),partner])
						writer.writerow(['CL',str(partnerClusterID),str(partnerID),'is categorised as','categorises'])
						writer.writerow(['CL',str(partnerID),str(project_id),'is related to', 'is related to'])
						createdPartners[partner] = str(partnerID)

						if(' Inc' in partner or ' inc' in partner or ' inc.' in partner or ' ltd' in partner or ' Ltd' in partner or ' ltd.' in partner or ' corp' in partner or ' Corp' in partner or ' Corportation' in partner or ' Corp.' in partner):
							writer.writerow(['CL','85165554',str(partnerID),'is a kind of', 'contains'])
						elif('Government' in partner or 'gov.' in partner or ' gov' in partner or 'gouvernement' in partner or 'government' in partner):
							writer.writerow(['CL','85165556',str(partnerID),'is a kind of', 'contains'])
						else:
							with open(partner_file, 'a+') as csvfile2:
								writer2 = csv.writer(csvfile2,lineterminator = '\n')
								writer2.writerow([str(partnerID),partner])

if __name__ == '__main__':
	main()