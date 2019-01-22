import csv
import requests
import sys
import json
import codecs
import fileinput


reload(sys)
sys.setdefaultencoding('utf8')
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

plants_file = "plants.csv"
database_file = "ALL NODES - Dec 5 2018.json"
output_file = "outputPlants.csv"

class Plant:
	def __init__(self,scientific,common,family,group,status,ID):
		self.scientific = scientific
		self.common = common
		self.family = family
		self.group = group
		self.status = status
		self.ID = ID

def loadDatabaseNodesToIdDict(database_file):
	nodes = dict()
	with open(database_file) as f:
		data = json.load(f)
		for i in range(len(data)):
			a_id = str(data[i]['_key'])
			name = str(data[i]['t']).strip()
			nodes[name] = a_id
	return nodes

def loadPlants(plants_file,database_nodes):
	plants = list()
	scientificNames = list()
	idCount = 1

	with open(plants_file,'r+') as f:
		reader = csv.reader(f)
		headers = next(reader)
		print headers
		for row in reader:
			scientificName = row[0].strip()
			commonName = row[1].strip()
			if("no common name" in commonName.lower()):
				print row
			family = row[2].strip()
			group = row[3].strip()
			status = row[4].strip()
			if scientificName.lower().strip() not in scientificNames:
				scientificNames.append(scientificName.lower().strip())
				ID = database_nodes.get(commonName)
				if ID == None:
					ID = idCount
					idCount = idCount + 1
				plants.append(Plant(scientificName,commonName,family,group,status,ID))
	return plants,idCount
def createNodesForPlants(plants,output_file):
	with open(output_file, 'w+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		for plant in plants:
			if plant.ID < 10000:
				if("no common name" in plant.common.lower() or 'haha' in plant.common.lower()):
					writer.writerow(['CN',str(plant.ID),plant.scientific])
				else:
					writer.writerow(['CN',str(plant.ID),plant.common,'t2',plant.scientific])

def createEndangeredAndThreatened(endangeredID,threatenedID,output_file):
	with open(output_file, 'a+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		#Create nodes for federal listing status
		writer.writerow(['CN',str(endangeredID),"Endangered species"])
		writer.writerow(['CN',str(threatenedID),"Threatened species"])
		#Set as cluster
		writer.writerow(['SC',str(endangeredID)])
		writer.writerow(['SC',str(threatenedID)])
		#Categorize linking status
		writer.writerow(['CL','85166321',str(endangeredID),'is a kind of', 'contains'])
		writer.writerow(['CL','85166321',str(threatenedID),'is a kind of', 'contains'])

def determinePlantGroups(plants,startID,database_nodes):
	groups = dict()
	for plant in plants:
		if plant.group not in groups:
			#check if ID exists
			if database_nodes.get(plant.group) != None:
				ID = database_nodes.get(plant.group)
			else:
				ID = startID
				startID = startID + 1
			groups[plant.group] = ID
	return groups,startID

def createNodesForPlantGroups(plantGroups,output_file):
	with open(output_file, 'a+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		for group, ID in plantGroups.iteritems():
			writer.writerow(['CN',str(ID),group])
			writer.writerow(['SC',str(ID)])
			writer.writerow(['CL','84870867',str(ID),'is a kind of', 'contains'])

def determinePlantFamilies(plants,startID,database_nodes):
	families = dict()
	for plant in plants:
		if plant.family not in families:
			#check if ID exists
			if database_nodes.get(plant.family) != None:
				ID = database_nodes.get(plant.family)
			else:
				ID = startID
				startID = startID + 1
			families[plant.family] = ID
	return families, startID

def createNodesForPlantFamilies(plantFamilies,output_file):
	with open(output_file, 'a+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		for family, ID in plantFamilies.iteritems():
			writer.writerow(['CN',str(ID),family])
			#writer.writerow(['SC',str(ID)])
			writer.writerow(['CL','85235424',str(ID),'is a kind of', 'contains'])


def categorizePlantNamesByGroup(plants, groups):
	with open(output_file, 'a+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		for plant in plants:
			thisGroup = plant.group
			thisID = plant.ID
			groupID = groups.get(thisGroup)
			writer.writerow(['CL',str(groupID),str(thisID),'is a kind of', 'contains'])

def categorizePlantNamesByFamily(plants, groups):
	with open(output_file, 'a+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		for plant in plants:
			thisFamily = plant.family
			thisID = plant.ID
			familyID = groups.get(thisFamily)
			writer.writerow(['CL',str(familyID),str(thisID),'is a kind of', 'contains'])


def categorizePlantStatus(plants, endangeredID, threatenedID):
	with open(output_file, 'a+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		for plant in plants:
			thisID = plant.ID
			if("Endangered" in plant.status):
				writer.writerow(['CL',str(thisID),str(endangeredID),'is a property of', 'has'])
			elif("Threatened" in plant.status):
				writer.writerow(['CL',str(thisID),str(threatenedID),'is a property of', 'has'])


def removeDuplicates(output_file):
	seen = set() # set for fast O(1) amortized lookup
	for line in fileinput.FileInput(output_file, inplace=1):
		if line in seen: continue # skip duplicate
		
		seen.add(line)
		print line, # standard output is now redirected to the file

def main():
	#Loads and removes duplicates
	database_nodes = loadDatabaseNodesToIdDict(database_file)
	plants,idCount = loadPlants(plants_file,database_nodes)
	createNodesForPlants(plants,output_file)

	endangeredID = idCount
	threatenedID = idCount + 1
	idCount = idCount + 2

	createEndangeredAndThreatened(endangeredID,threatenedID,output_file)

	plantGroups, idCount = determinePlantGroups(plants,idCount,database_nodes)
	createNodesForPlantGroups(plantGroups,output_file)
	categorizePlantNamesByGroup(plants,plantGroups)

	plantFamilies, idCount = determinePlantFamilies(plants,idCount,database_nodes)
	createNodesForPlantFamilies(plantFamilies,output_file)
	categorizePlantNamesByFamily(plants,plantFamilies)


	categorizePlantStatus(plants,endangeredID,threatenedID)
	removeDuplicates(output_file)


if __name__ == '__main__':
	main()
