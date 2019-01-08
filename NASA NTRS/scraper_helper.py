# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import sys
import codecs
import csv
from xml.etree import ElementTree
from xml.dom import minidom

import time

reload(sys)
sys.setdefaultencoding('utf8')
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

input_file = 'nasa_65_scrape.csv'
output_file = "NASA_FULL.csv"

NASA_Centers = {
	'NASA Ames Research Center': '85235773',
	'NASA Armstrong Flight Research Center': '85235774',
	'NASA Glenn Research Center': '85235778',
	'NASA Goddard Space Flight Center': '85179138',
	'NASA Jet Propulsion Laboratory': '84873324',
	'NASA Johnson Space Center': '85235779',
	'NASA Kennedy Space Center': '85166441',
	'NASA Langley Research Center': '85235777',
	'NASA Marshall Space Flight Center': '85235780',
	'NASA Stennis Space Center': '85235775'
}
subjects = {
	'ACOUSTICS' : ['84865254'],					
	'ADMINISTRATION AND MANAGEMENT' : ['85188415'],					
	'AERODYNAMICS' : ['84865314'],					
	'AERONAUTICS (GENERAL)' : ['84863939'],					
	'AEROSPACE MEDICINE' : ['84868161'],					
	'AIRCRAFT PROPULSION AND POWER' : ['84871685'],					
	'AIRCRAFT STABILITY AND CONTROL' : ['84865326'],					
	'ASTRONAUTICS (GENERAL)' : ['84865782'],					
	'ASTRONOMY' : ['84864446'],					
	'ASTROPHYSICS' : ['84863694'],					
	'ATOMIC AND MOLECULAR PHYSICS' : ['84865491','84864584'],					
	'AVIONICS AND AIRCRAFT INSTRUMENTATION' : ['84866963'],					
	'BEHAVIORAL SCIENCES' : ['85166914'],					
	'BIOSCIENCES' : ['84873160'],					
	'BIOTECHNOLOGY' : ['84873160'],					
	'CHEMISTRY' : ['84864455'],					
	'CHEMISTRY AND MATERIALS (GENERAL)' : ['84864955','84864455'],					
	'COMMUNICATIONS AND RADAR' : ['84872006'],					
	'COMPOSITE MATERIALS' : ['84878857'],					
	'COMPUTER OPERATIONS AND HARDWARE' : ['84872041'],					
	'COMPUTER PROGRAMMING AND SOFTWARE' : ['84868756'],					
	'COMPUTER SYSTEMS' : ['84872041'],					
	'COMPUTERS' : ['84872041'],					
	'CYBERNETICS' : ['84867334'],					
	'CYBERNETICS, ARTIFICIAL INTELLIGENCE AND ROBOTICS' : ['84868714','84866969','84867334'],					
	'DOCUMENTATION AND INFORMATION SCIENCE' : ['84868286'],					
	'EARTH RESOURCES AND REMOTE SENSING' : ['85172632'],					
	'ECONOMICS AND COST ANALYSIS' : ['85166947'],					
	'ELECTRONIC COMPONENTS AND CIRCUITS' : ['84868547'],					
	'ELECTRONIC EQUIPMENT' : ['84868547'],					
	'ELECTRONIC SYSTEMS' : ['84868547'],					
	'ELECTRONICS' : ['84868547'],					
	'ELECTRONICS AND ELECTRICAL ENGINEERING' : ['84868547','84866951'],					
	'ENERGY PRODUCTION AND CONVERSION' : ['84870316'],					
	'ENGINEERING (GENERAL)' : ['84866671'],					
	'ENVIRONMENT POLLUTION' : ['84870439','85191308'],					
	'FACILITIES, RESEARCH, AND SUPPORT' : ['85165552'],					
	'FLUID MECHANICS' : ['84865109'],					
	'FLUID MECHANICS AND HEAT TRANSFER' : ['84865109','84870346'],					
	'FLUID MECHANICS AND THERMODYNAMICS' : ['84865109','84865402'],					
	'GEOPHYSICS' : ['84864158'],					
	'GEOSCIENCES (GENERAL)' : ['84864095'],					
	'INORGANIC AND PHYSICAL CHEMISTRY' : ['84864482','84865532'],					
	'INORGANIC, ORGANIC AND PHYSICAL CHEMISTRY' : ['84864482','84865532','84864506'],					
	'INSTRUMENTATION AND PHOTOGRAPHY' : ['84876444'],					
	'LASERS AND MASERS' : ['84872452'],					
	'LAUNCH VEHICLES AND LAUNCH OPERATIONS' : ['84872238'],					
	'LAUNCH VEHICLES AND SPACE VEHICLES' : ['84872238','84872091'],					
	'LAW, POLITICAL SCIENCE AND SPACE POLICY' : ['85167019'],					
	'LIFE SCIENCES' : ['84863609'],					
	'LIFE SCIENCES (GENERAL)' : ['84863609'],					
	'LUNAR AND PLANETARY EXPLORATION' : ['84872091'],					
	'LUNAR AND PLANETARY SCIENCE AND EXPLORATION' : ['84868639','84863826'],					
	'MATERIALS' : ['84864955'],					
	'MATERIALS, METALLIC' : ['85165525'],					
	'MATHEMATICAL AND COMPUTER SCIENCES (GENERAL)' : ['84874452','84866563'],					
	'MATHEMATICS' : ['84874452'],					
	'MATHEMATICS AND INFORMATION SCIENCES' : ['84874452','84868286'],					
	'MECHANICAL ENGINEERING' : ['84867148'],					
	'MECHANICS' : ['84865901'],					
	'METALLIC MATERIALS' : ['85165525'],					
	'METALS AND METALLIC MATERIALS' : ['85165525'],					
	'METEOROLOGY' : ['84863936'],					
	'METEOROLOGY AND CLIMATOLOGY' : ['84863936','84863901'],					
	'NAVIGATION' : ['84868981'],					
	'NUCLEAR AND HIGH-ENERGY PHYSICS' : ['84864612','84864618'],					
	'NUCLEAR ENGINEERING' : ['84867160'],					
	'NUCLEAR PHYSICS' : ['84864612'],					
	'NUMERICAL ANALYSIS' : ['84868822'],					
	'OCEANOGRAPHY' : ['85166735'],					
	'OPTICS' : ['84865562'],					
	'PHYSICAL SCIENCES' : ['84863580'],					
	'PHYSICS (GENERAL)' : ['84865805'],					
	'PHYSICS OF ELEMENTARY PARTICLES AND FIELDS' : ['84866010'],					
	'PHYSICS, ATOMIC, MOLECULAR, AND NUCLEAR' : ['84864584','84865491','84864612'],					
	'PHYSICS, GENERAL' : ['84865805'],					
	'PHYSICS, PLASMA' : ['84868792'],					
	'PLASMA PHYSICS' : ['84868792'],					
	'PROPELLANTS' : ['84873130'],					
	'PROPELLANTS AND FUELS' : ['84873130'],					
	'PROPULSION SYSTEMS' : ['84871685'],					
	'RESEARCH AND SUPPORT FACILITIES' : ['85165552'],					
	'SOCIAL AND INFORMATION SCIENCES (GENERAL)' : ['84866695','84868286'],					
	'SOCIAL SCIENCES (GENERAL)' : ['84866695'],					
	'SOLAR PHYSICS' : ['84863667'],					
	'SPACE SCIENCES' : ['84868499'],					
	'SPACE SCIENCES (GENERAL)' : ['84868499'],					
	'SPACE VEHICLES' : ['84872091','84872091'],					
	'SPACECRAFT DESIGN, TESTING AND PERFORMANCE' : ['84869086','84872091'],					
	'SPACECRAFT INSTRUMENTATION' : ['84872091'],					
	'SPACECRAFT INSTRUMENTATION AND ASTRIONICS' : ['84872091'],					
	'SPACECRAFT PROPULSION AND POWER' : ['84871895','84872091'],					
	'STATISTICS AND PROBABILITY' : ['84868397','85167876'],					
	'STRUCTURAL MECHANICS' : ['84865350'],					
	'THEORETICAL MATHEMATICS' : ['84874452'],					
	'THERMODYNAMICS AND COMBUSTION' : ['84865402'],					
	'THERMODYNAMICS AND STATISTICAL PHYSICS' : ['84865402','84866004'],					
	'URBAN TECHNOLOGY AND TRANSPORTATION' : ['85166035']			

}


def createNodeWithLink(name,id,parentCluster,output_file,url=None):
	return id + 1

def createDocumentTypeNodes(output_file,id):
	#Step 2.2
	id = createNodeWithLink('Accepted manuscript',id,'84878834',output_file)
	id = createNodeWithLink('Bibliography',id,'84878834',output_file)
	id = createNodeWithLink('Conference paper',id,'84878834',output_file)
	id = createNodeWithLink('Tech brief',id,'84878834',output_file)
	id = createNodeWithLink('News release',id,'84878834',output_file)
	id = createNodeWithLink('Presentation',id,'84878834',output_file)
	id = createNodeWithLink('PhD dissertation',id,'84878834',output_file)
	return id

def createNASACenterNodes(output_file,id):
	NASA_Centers['NASA Wallops Flight Facility'] = id
	id = createNodeWithLink('NASA Wallops Flight Facility',id,'84878896',output_file,'https://www.nasa.gov/centers/wallops/home')
	NASA_Centers['NASA White Sands Test Facility'] = id
	id = createNodeWithLink('NASA White Sands Test Facility',id,'84878896',output_file,'https://www.nasa.gov/centers/wstf/home/index.html')
	NASA_Centers['NASA Unspecified Center'] = id
	id = createNodeWithLink('NASA Unspecified Center',id,'84878896',output_file)

	return id
def createSubjectCategoryNodes(output_file,id):
	id = createNodeWithLink('Air Transportation And Safety',id,'85170354',output_file)
	temp = list()
	temp.append(str(id-1))
	subjects['AIR TRANSPORTATION AND SAFETY'] = temp

	id = createNodeWithLink('Aircraft',id,'84872050',output_file)
	temp = list()
	temp.append(str(id-1))
	subjects['AIRCRAFT'] = temp

	id = createNodeWithLink('Aircraft Communications',id,'85170354',output_file)
	temp = list()
	temp.append(str(id-1))
	subjects['AIRCRAFT COMMUNICATIONS AND NAVIGATION'] = temp

	id = createNodeWithLink('Aircraft Design',id,'85165499',output_file)
	temp = list()
	temp.append(str(id-1))
	subjects['AIRCRAFT DESIGN, TESTING AND PERFORMANCE'] = temp

	id = createNodeWithLink('Aircraft Instrumentation',id,'85170354',output_file)
	temp = list()
	temp.append(str(id-1))
	subjects['AIRCRAFT INSTRUMENTATION'] = temp

	id = createNodeWithLink('Astrodynamics',id,'84863653',output_file)
	temp = list()
	temp.append(str(id-1))
	subjects['ASTRODYNAMICS'] = temp

	id = createNodeWithLink('Auxiliary Systems',id,'84866174',output_file)
	temp = list()
	temp.append(str(id-1))
	subjects['AUXILIARY SYSTEMS'] = temp

	id = createNodeWithLink('Exobiology',id,'84863609',output_file)
	temp = list()
	temp.append(str(id-1))
	subjects['EXOBIOLOGY'] = temp

	id = createNodeWithLink('Fabrication Technology',id,'84863718',output_file)
	temp = list()
	temp.append(str(id-1))
	subjects['FABRICATION TECHNOLOGY'] = temp

	id = createNodeWithLink('Ground Support Systems',id,'84866174',output_file)
	temp = list()
	temp.append(str(id-1))
	subjects['GROUND SUPPORT SYSTEMS AND FACILITIES (SPACE)'] = temp

	id = createNodeWithLink('Instrumentation',id,'84864688',output_file)
	subjects['INSTRUMENTATION AND PHOTOGRAPHY'].append(str(id-1))

	id = createNodeWithLink('Maser',id,'84864688',output_file)
	subjects['LASERS AND MASERS'].append(str(id-1))
	temp = list()
	temp.append(str(id-1))
	subjects['MASERS'] = temp

	id = createNodeWithLink('Launch Operations',id,'85170354',output_file)
	subjects['LAUNCH VEHICLES AND LAUNCH OPERATIONS'].append(str(id-1))

	id = createNodeWithLink('Lunar exploration',id,'85170354',output_file)
	subjects['LUNAR AND PLANETARY EXPLORATION'].append(str(id-1))

	id = createNodeWithLink('Planetary exploration',id,'85170354',output_file)
	subjects['LUNAR AND PLANETARY SCIENCE AND EXPLORATION'].append(str(id-1))

	id = createNodeWithLink('Machinery',id,'84864688',output_file)
	temp = list()
	temp.append(str(id-1))
	subjects['MACHINE ELEMENTS AND PROCESSES'] = temp
	subjects['MACHINERY'] = temp


	id = createNodeWithLink('System Technology',id,'84863718',output_file)
	temp = list()
	temp.append(str(id-1))
	subjects['MAN/SYSTEM TECHNOLOGY AND LIFE SUPPORT'] = temp

	id = createNodeWithLink('Life Support',id,'84866174',output_file)
	subjects['MAN/SYSTEM TECHNOLOGY AND LIFE SUPPORT'].append(str(id-1))

	id = createNodeWithLink('Materials Processing',id,'84871418',output_file)
	temp = list()
	temp.append(str(id-1))
	subjects['MATERIALS PROCESSING'] = temp

	id = createNodeWithLink('Nonmetallic material',id,'85165586',output_file)
	temp = list()
	temp.append(str(id-1))
	subjects['MATERIALS, NONMETALLIC'] = temp
	subjects['NONMETALLIC MATERIALS'] = temp

	id = createNodeWithLink('Solid-state physics',id,'84863580',output_file)
	temp = list()
	temp.append(str(id-1))
	subjects['PHYSICS, SOLID-STATE'] = temp
	subjects['SOLID-STATE PHYSICS'] = temp

	id = createNodeWithLink('Quality Assurance And Reliability',id,'85170354',output_file)
	temp = list()
	temp.append(str(id-1))
	subjects['QUALITY ASSURANCE AND RELIABILITY'] = temp

	id = createNodeWithLink('Space Biology',id,'84863609',output_file)
	temp = list()
	temp.append(str(id-1))
	subjects['SPACE BIOLOGY'] = temp

	id = createNodeWithLink('Space Communications',id,'84863653',output_file)
	temp = list()
	temp.append(str(id-1))
	subjects['SPACE COMMUNICATIONS, SPACECRAFT COMMUNICATIONS, COMMAND AND TRACKING'] = temp

	id = createNodeWithLink('Spacecraft Communications',id,'84863718',output_file)
	subjects['SPACE COMMUNICATIONS, SPACECRAFT COMMUNICATIONS, COMMAND AND TRACKING'].append(str(id-1))

	id = createNodeWithLink('Command And Tracking',id,'84863718',output_file)
	subjects['SPACE COMMUNICATIONS, SPACECRAFT COMMUNICATIONS, COMMAND AND TRACKING'].append(str(id-1))

	id = createNodeWithLink('Space Processing',id,'84871418',output_file)
	temp = list()
	temp.append(str(id-1))
	subjects['SPACE PROCESSING'] = temp

	id = createNodeWithLink('Space Radiation',id,'84876989',output_file)
	temp = list()
	temp.append(str(id-1))
	subjects['SPACE RADIATION'] = temp

	id = createNodeWithLink('Space Transportation',id,'84863653',output_file)
	temp = list()
	temp.append(str(id-1))
	subjects['SPACE TRANSPORTATION'] = temp
	subjects['SPACE TRANSPORTATION AND SAFETY'] = temp

	id = createNodeWithLink('Space Safety',id,'84865981',output_file)
	subjects['SPACE TRANSPORTATION AND SAFETY'].append(str(id-1))

	id = createNodeWithLink('Spacecraft Testing',id,'84871418',output_file)
	subjects['SPACECRAFT DESIGN, TESTING AND PERFORMANCE'].append(str(id-1))

	id = createNodeWithLink('Spacecraft Instrumentation',id,'84864688',output_file)
	subjects['SPACECRAFT INSTRUMENTATION'].append(str(id-1))
	subjects['SPACECRAFT INSTRUMENTATION AND ASTRIONICS'].append(str(id-1))

	id = createNodeWithLink('Astrionics',id,'84863653',output_file)
	subjects['SPACECRAFT INSTRUMENTATION AND ASTRIONICS'].append(str(id-1))

	id = createNodeWithLink('Systems Analysis',id,'84863653',output_file)
	temp = list()
	temp.append(str(id-1))
	subjects['SYSTEMS ANALYSIS'] = temp
	subjects['SYSTEMS ANALYSIS AND OPERATIONS RESEARCH'] = temp

	id = createNodeWithLink('Operations Research',id,'84865981',output_file)
	subjects['SYSTEMS ANALYSIS AND OPERATIONS RESEARCH'].append(str(id-1))

	id = createNodeWithLink('Technology Utilization',id,'85170354',output_file)
	temp = list()
	temp.append(str(id-1))
	subjects['TECHNOLOGY UTILIZATION AND SURFACE TRANSPORTATION'] = temp

	id = createNodeWithLink('Surface Transportation',id,'85170354',output_file)
	subjects['TECHNOLOGY UTILIZATION AND SURFACE TRANSPORTATION'].append(str(id-1))

	id = createNodeWithLink('Combustion',id,'84876989',output_file)
	subjects['THERMODYNAMICS AND COMBUSTION'].append(str(id-1))

	id = createNodeWithLink('Urban Technology',id,'84863718',output_file)
	subjects['URBAN TECHNOLOGY AND TRANSPORTATION'].append(str(id-1))
	return id

def createTechnicalReportNodes(output_file,id,all_authors,startToken):
	startTime =  time.time()
	print startTime
	#all_authors = dict()
	resumptionTokenStart = startToken
	lastValid = resumptionTokenStart
	timesFailed = 0

	while(resumptionTokenStart <= 597801):
		print "Resumption Token: " + str(resumptionTokenStart) + " / 597801 " + str(resumptionTokenStart * 100.0 / 597801)
		if(resumptionTokenStart > 1):
			url = 'https://ntrs.nasa.gov/oai?verb=ListRecords&metadataPrefix=casi_dc&resumptionToken=casi_dc!all_sti!' + str(resumptionTokenStart)
		else:
			url = 'https://ntrs.nasa.gov/oai?verb=ListRecords&metadataPrefix=casi_dc' 
		requestTime = time.time()
		try:
			response = requests.get(url)
			soup = BeautifulSoup(response.text,'xml')
			numRecords = len(soup.findAll('record'))
		except:
			print("Couldn't get response for: " + url + ". Trying again in 120 seconds")
			timesFailed = timesFailed + 1
			time.sleep(120)
			if(timesFailed == 10):
				timesFailed = 0
				resumptionTokenStart = resumptionTokenStart + 100
				print("Failed 10 times. Continuing")
			continue
		responseTime = time.time()
		print(str(responseTime) + ": " + str(responseTime - requestTime) + " seconds to get response. There are " + str(numRecords) + " records. ")
		if(numRecords == 0):
			print("Invalid. Last valid was " + str(lastValid))
			resumptionTokenStart = resumptionTokenStart + 100
			continue
		else:
			lastValid = float(resumptionTokenStart)
			timesFailed = 0

		records = soup.findAll('record')
		with open(output_file, 'a+') as csvfile:
			writer = csv.writer(csvfile,lineterminator = '\n')	
			for record in records:
				doc_type = record.find('dc:type')
				if(doc_type == None):
					continue
				doc_type = doc_type.text
				if doc_type != 'Technical Report':
					continue
				title = record.find('dc:title')
				if(title == None):
					continue
				title = title.text

				description = record.find('dc:description')
				if(description == None):
					description = ""
				else:
					description = description.text
				identifier = record.find('casiterms:identifier.casi_id')
				if(identifier == None):
					continue
				identifier = identifier.text
				doc_url = 'https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/' + str(identifier) +'.pdf'
				report_id = id
				id = id + 1
				#Step 0
				writer.writerow(['CN',str(report_id),title,'description',description,'reference',doc_url])
				#0.1, 2.3
				writer.writerow(['CL','85235955',str(report_id),'is a kind of','contains'])
				research_center = record.find('casiterms:contributor.originator')
				if(research_center != None):
					research_center = research_center.text
					if(NASA_Centers.get(research_center) != None):
						research_id = NASA_Centers[research_center]
						writer.writerow(['CL',str(research_id),str(report_id),'is produced by', 'produces'])
					else:
						print "Research center not found: " + research_center
				authors = record.findAll('dc:creator')
				for author in authors:
					reversed_name = author.text
					if(len(reversed_name.split(",")) != 2):
						continue
					firstname = reversed_name.split(",")[1].strip()
					lastname = reversed_name.split(",")[0].strip()
					author_name = firstname + " " + lastname
					if(all_authors.get(author_name) != None):
						author_id = all_authors[author_name]
					else:
						author_id = id
						all_authors[author_name] = id
						id = id + 1
						#1.0
						writer.writerow(['CN',str(author_id),author_name])
						#1.1
						writer.writerow(['CL','85165565',str(author_id),'is a kind of', 'contains'])
					#1.2
					writer.writerow(['CL',str(author_id),str(report_id),'is authored by', 'is the author of'])
				subjects_in_doc = record.findAll('dc:subject')
				for subject in subjects_in_doc:
					if(subject == None):
						continue
					subject = subject.text.upper()
					if(subjects.get(subject) == None):
						print "Subject not found: " + subject
					else:
						subject_ids = subjects.get(subject)
						for subject_id in subject_ids:
							writer.writerow(['CL',str(subject_id),str(report_id),'is related to', 'is related to'])

		resumptionTokenStart = resumptionTokenStart + 100
	print str(time.time() - startTime) + " seconds to run "
def getAlreadyCreatedNodes(input_file,idCount):
	start_id = 1
	all_authors = dict()
	with open(input_file,'r+') as f:
		reader = csv.reader(f)
		for row in reader:
			if len(row) >=3:
				if row[0] == 'CN' and row[1] >= idCount:
					all_authors[row[2]] = str(row[1])
					start_id = row[1]
	return float(start_id)+1,all_authors


def main():
	#Create file
	#with open(output_file, 'w+') as csvfile:
	#	writer = csv.writer(csvfile,lineterminator = '\n')
	#idCount = createDocumentTypeNodes(output_file,1)
	#idCount = createNASACenterNodes(output_file,idCount)
	#idCount = createSubjectCategoryNodes(output_file,idCount)

	#start_id, all_authors = getAlreadyCreatedNodes(input_file,idCount)

	#startToken = 390901
	#startToken = 393401
	#startToken = 416901
	#createTechnicalReportNodes(output_file,start_id,all_authors,startToken)

	#file1 = "Book1.csv"
	#file2 = "Book2.csv"
	#with open(file1, 'a+') as csvfile:
	#	writer = csv.writer(csvfile,lineterminator = '\n')	
	#	with open(file2,'r+') as f:
	#		reader = csv.reader(f)
	#		for row in reader:
	#			writer.writerow(row)
	pubs_file = "publications.csv"
	authors_file = "authors.csv"
	links_file = 'links.csv'
	fullFile = "NASA_FULL_SCRAPE.csv"


	with open(pubs_file, 'w+') as csvfile1:
		writer1 = csv.writer(csvfile1,lineterminator = '\n')
		with open(authors_file, 'w+') as csvfile2:
			writer2 = csv.writer(csvfile2,lineterminator = '\n')
			with open(links_file, 'w+') as csvfile3:
				writer3 = csv.writer(csvfile3,lineterminator = '\n')
				with open(fullFile,'r+') as f:
					reader = csv.reader(f)
					for row in reader:
						if len(row) > 0:
							if(row[0] == 'CL'):
								writer3.writerow(row)
							elif(row[0] == 'CN' and row[1] >= 50 and row[3] == 'description'):
								writer1.writerow(row)
							elif(row[0] == 'CN' and row[1] >= 50):
								writer2.writerow(row)




if __name__ == '__main__':
	main()