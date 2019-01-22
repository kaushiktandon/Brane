import csv
import requests
import sys
import json
import codecs
import fileinput


reload(sys)
sys.setdefaultencoding('utf8')
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

species_file = "species.csv"
plants_file = "plants.csv"
database_file = "ALL NODES - Dec 5 2018.json"
output_file = "output.csv"

states_dict = us_state_abbrev = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NY': 'New York',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming',
}

class Specie:
	def __init__(self,scientific,common,group,status,whereListed,ID):
		self.scientific = scientific
		self.common = common
		self.group = group
		self.status = status
		self.whereListed = whereListed
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


def loadSpecies(species_file,database_nodes):
	species = list()
	scientificNames = list()
	idCount = 1

	with open(species_file,'r+') as f:
		reader = csv.reader(f)
		headers = next(reader)
		print headers
		for row in reader:
			scientificName = row[0].strip()
			commonName = row[1].strip()
			if("no common name" in commonName.lower()):
				print row
			group = row[2].strip()
			status = row[3].strip()
			whereListed = row[4].strip()
			if scientificName.lower().strip() not in scientificNames:
				scientificNames.append(scientificName.lower().strip())
				ID = database_nodes.get(commonName)
				if ID == None:
					ID = idCount
					idCount = idCount + 1
				species.append(Specie(scientificName,commonName,group,status,whereListed,ID))
	return species,idCount
def createNodesForSpecies(species,output_file):
	with open(output_file, 'w+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		for specie in species:
			if specie.ID < 10000:
				if("no common name" in specie.common.lower()):
					writer.writerow(['CN',str(specie.ID),specie.scientific])
				else:
					writer.writerow(['CN',str(specie.ID),specie.common,'t2',specie.scientific])

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

def determineSpeciesGroups(species,startID,database_nodes):
	groups = dict()
	for specie in species:
		if specie.group not in groups:
			#check if ID exists
			if database_nodes.get(specie.group) != None:
				ID = database_nodes.get(specie.group)
			else:
				ID = startID
				startID = startID + 1
			groups[specie.group] = ID
	return groups,startID

def createNodesForSpeciesGroups(speciesGroups,output_file):
	with open(output_file, 'a+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		for group, ID in speciesGroups.iteritems():
			writer.writerow(['CN',str(ID),group])
			writer.writerow(['SC',str(ID)])
			writer.writerow(['CL','84870867',str(ID),'is a kind of', 'contains'])

def categorizeSpecieNames(species, groups):
	with open(output_file, 'a+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		for specie in species:
			thisGroup = specie.group
			thisID = specie.ID
			groupID = groups.get(thisGroup)
			writer.writerow(['CL',str(groupID),str(thisID),'is a kind of', 'contains'])

def categorizeSpecieStatus(species, endangeredID, threatenedID):
	with open(output_file, 'a+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		for specie in species:
			thisID = specie.ID
			if("Endangered" in specie.status):
				writer.writerow(['CL',str(thisID),str(endangeredID),'is a property of', 'has'])
			elif("Threatened" in specie.status):
				writer.writerow(['CL',str(thisID),str(threatenedID),'is a property of', 'has'])

def categorizeLocations(species,startID,database_nodes,output_file):
	with open(output_file, 'a+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		for specie in species:
			fullLocation = specie.whereListed
			if(len(fullLocation) == 0):
				continue
			#print fullLocation
			thisID = specie.ID
			commaSplit = fullLocation.split(",")
			if(len(commaSplit) > 1):
				#print commaSplit
				hasUSA = False
				for america in commaSplit:
					#print america
					if 'U.S.' in america:
						hasUSA = True
					if hasUSA:
						for i in range(len(america)-1):
							if(america[i].isupper() and america[i+1].isupper()):
								key = america[i] + america[i+1]
								if(states_dict.get(key) != None):
									fullState =  states_dict[key]
									stateID = database_nodes.get(fullState)
									#print "GOT", fullState
									writer.writerow(['CL',str(stateID),str(thisID),'is located in', 'is the location of'])

					if(database_nodes.get(america.strip()) != None):
						databaseID = database_nodes[america.strip()]
						#print "GOT: ",america.strip()
						writer.writerow(['CL',str(databaseID),str(thisID),'is located in', 'is the location of'])
			hyphenSplit = fullLocation.split('-')
			if(len(hyphenSplit) > 1):
				for val in hyphenSplit:
					if database_nodes.get(val.replace(")",'').strip())	!= None:
						databaseID = database_nodes.get(val.replace(")",'').strip())	
						writer.writerow(['CL',str(databaseID),str(thisID),'is located in', 'is the location of'])
					elif "County" in val:
						state = fullLocation[fullLocation.find('(') + 1 : fullLocation.find(val) - 1]
						if(state != None):
							fullState = states_dict[state.strip()]
							county =  val.replace(")","").strip()
							writer.writerow(['CN',str(startID),county])
							writer.writerow(['CL','85165572',str(startID),'is a kind of', 'contains'])
							writer.writerow(['CL',str(startID),str(thisID),'is located in', 'is the location of'])
							writer.writerow(['CL','85165571',str(startID),'is located in', 'is the location of'])
							startID = startID + 1

			parenSplit = fullLocation.split("(")
			if(len(parenSplit) > 1):
				for val in parenSplit:
					if database_nodes.get(val.replace(")",'').strip())	!= None:
						databaseID = database_nodes.get(val.replace(")",'').strip())
						writer.writerow(['CL',str(databaseID),str(thisID),'is located in', 'is the location of'])



	return startID

def removeDuplicates(output_file):
	seen = set() # set for fast O(1) amortized lookup
	for line in fileinput.FileInput(output_file, inplace=1):
		if line in seen: continue # skip duplicate
		
		seen.add(line)
		print line, # standard output is now redirected to the file

def main():
	#Loads and removes duplicates
	database_nodes = loadDatabaseNodesToIdDict(database_file)
	species,idCount = loadSpecies(species_file,database_nodes)
	createNodesForSpecies(species,output_file)

	endangeredID = idCount
	threatenedID = idCount + 1
	idCount = idCount + 2

	createEndangeredAndThreatened(endangeredID,threatenedID,output_file)

	speciesGroups, idCount = determineSpeciesGroups(species,idCount,database_nodes)
	createNodesForSpeciesGroups(speciesGroups,output_file)
	categorizeSpecieNames(species,speciesGroups)
	categorizeSpecieStatus(species,endangeredID,threatenedID)

	idCount = categorizeLocations(species,idCount,database_nodes,output_file)
	removeDuplicates(output_file)


if __name__ == '__main__':
	main()
