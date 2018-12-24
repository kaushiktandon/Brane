# -*- coding: utf-8 -*-

import sys
import codecs
import csv

reload(sys)
sys.setdefaultencoding('utf8')
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

plants_file = 'global_power_plant_database.csv'
output_file = "output.csv"

countries_name_to_id = {
	"Afghanistan": "85168849",
	"Albania": "85168850",
	"Algeria": "85168851",
	"Angola": "85168854",
	"Argentina": "85168857",
	"Armenia": "85168858",
	"Australia": "85166437",
	"Austria": "85168860",
	"Azerbaijan": "85168861",
	"Bahrain": "85168863",
	"Bangladesh": "85168864",
	"Belarus": "85168866",
	"Belgium": "85168867",
	"Benin": "85168869",
	"Bhutan": "85168871",
	"Bolivia": "85168872",
	"Bosnia and Herzegovina": "85168873",
	"Botswana": "85168874",
	"Brazil": "85168875",
	"Brunei Darussalam": "85168877",
	"Bulgaria": "85168878",
	"Burkina Faso": "85168879",
	"Burundi": "85168881",
	"Cambodia": "85168882",
	"Cameroon": "85168883",
	"Canada": "85166378",
	"Cape Verde": "85168884",
	"Central African Republic": "85168886",
	"Chile": "85168888",
	"China": "85168889",
	"Colombia": "85168890",
	"Congo": "85168892",
	"Costa Rica": "85168895",
	"Cote DIvoire": "85168896",
	"Croatia": "85168897",
	"Cuba": "85168898",
	"Cyprus": "85168899",
	"Czech Republic": "85168900",
	"Democratic Republic of the Congo": "85168892",
	"Denmark": "85168901",
	"Djibouti": "85168902",
	"Dominican Republic": "85168904",
	"Ecuador": "85168906",
	"Egypt": "85168907",
	"El Salvador": "85168908",
	"Equatorial Guinea": "85168909",
	"Eritrea": "85168910",
	"Estonia": "85168911",
	"Ethiopia": "85168912",
	"Fiji": "85168914",
	"Finland": "85168915",
	"France": "85168916",
	"French Guiana": "85168917",
	"Gabon": "85168919",
	"Gambia": "85168920",
	"Georgia": "85168922",
	"Germany": "85168923",
	"Ghana": "85168924",
	"Greece": "85168926",
	"Guatemala": "85168931",
	"Guinea": "85168933",
	"Guinea-Bissau": "85168934",
	"Guyana": "85168935",
	"Honduras": "85168937",
	"Hungary": "85168939",
	"Iceland": "85168940",
	"India": "85168941",
	"Indonesia": "85168942",
	"Iran": "85168943",
	"Iraq": "85168944",
	"Ireland": "85168945",
	"Israel": "85168947",
	"Italy": "85168948",
	"Jamaica": "85168949",
	"Japan": "85168950",
	"Jordan": "85168952",
	"Kazakhstan": "85168953",
	"Kenya": "85168954",
	"Kuwait": "85168958",
	"Kyrgyzstan": "85168959",
	"Laos": "85168960",
	"Latvia": "85168961",
	"Lebanon": "85168962",
	"Lesotho": "85168963",
	"Liberia": "85168964",
	"Libya": "85168965",
	"Lithuania": "85168967",
	"Luxembourg": "85168968",
	"Macedonia": "85168970",
	"Madagascar": "85168971",
	"Malawi": "85168972",
	"Malaysia": "85168973",
	"Mali": "85168975",
	"Mauritania": "85168979",
	"Mauritius": "85168980",
	"Mexico": "85168982",
	"Moldova": "85168984",
	"Mongolia": "85168986",
	"Morocco": "85168988",
	"Mozambique": "85168989",
	"Myanmar": "85168880",
	"Namibia": "85168990",
	"Nepal": "85168992",
	"Netherlands": "85168993",
	"New Zealand": "85168996",
	"Nicaragua": "85168997",
	"Niger": "85168998",
	"Nigeria": "85168999",
	"North Korea": "85168956",
	"Norway": "85169001",
	"Oman": "85169002",
	"Pakistan": "85169003",
	"Panama": "85169005",
	"Papua New Guinea": "85169006",
	"Paraguay": "85169007",
	"Peru": "85169008",
	"Philippines": "85169009",
	"Poland": "85169010",
	"Portugal": "85169011",
	"Qatar": "85169013",
	"Romania": "85169015",
	"Russia": "85169016",
	"Rwanda": "85169017",
	"Saudi Arabia": "85169026",
	"Senegal": "85169027",
	"Serbia": "85169028",
	"Sierra Leone": "85169030",
	"Singapore": "85169031",
	"Slovakia": "85169032",
	"Slovenia": "85169033",
	"South Africa": "85169036",
	"South Korea": "85168957",
	"Spain": "85169037",
	"Sri Lanka": "85169038",
	"Sudan": "85169039",
	"Swaziland": "85169041",
	"Sweden": "85169042",
	"Switzerland": "85169043",
	"Syrian Arab Republic": "85169044",
	"Taiwan": "85169045",
	"Tajikistan": "85169046",
	"Tanzania": "85169047",
	"Thailand": "85169048",
	"Togo": "85169049",
	"Trinidad and Tobago": "85169051",
	"Tunisia": "85169052",
	"Turkey": "85169053",
	"Turkmenistan": "85169054",
	"Uganda": "85169057",
	"Ukraine": "85169058",
	"United Arab Emirates": "85169059",
	"United Kingdom": "85169060",
	"United States of America": "85169061",
	"Uruguay": "85169062",
	"Uzbekistan": "85169063",
	"Venezuela": "85169065",
	"Vietnam": "85169066",
	"Western Sahara": "85169070",
	"Yemen": "85169071",
	"Zambia": "85169072",
	"Zimbabwe": "85169073"
}
fuel_to_id_dict = {
	"Oil": "85299115",	
	"Hydro": "84871826",	
	"Wind": "84871718",	
	"Biomass": "84871222",	
	"Nuclear": "84871694",	
	"Gas": "84870361",	
	"Solar": "84871724",	
	"Geothermal": "84871751",	
	"Cogeneration": "85297277",	
	"Storage": "84871757",	
	"Wave and Tidal": "84871820"
}


def main():
	#Create nodes for 3 countries
	idCount = 1
	with open(output_file, 'w+') as csvfile:
		writer = csv.writer(csvfile,lineterminator='\n')
		writer.writerow(['CN',str(idCount),'Antarctica'])
		writer.writerow(['CL','84865696',str(idCount),'is a kind of', 'contains'])
		countries_name_to_id['Antarctica'] = idCount
		idCount = idCount + 1

		writer.writerow(['CN',str(idCount),'Kosovo'])
		writer.writerow(['CL','85165571',str(idCount),'is a kind of', 'contains'])
		countries_name_to_id['Kosovo'] = idCount
		idCount = idCount + 1
		
		writer.writerow(['CN',str(idCount),'Montenegro'])
		writer.writerow(['CL','85165571',str(idCount),'is a kind of', 'contains'])
		countries_name_to_id['Montenegro'] = idCount
		idCount = idCount + 1
	#Create nodes for 3 fuels
	with open(output_file, 'a+') as csvfile:
		writer = csv.writer(csvfile,lineterminator='\n')
		writer.writerow(['CN',str(idCount),'Coal'])
		writer.writerow(['CL','85165481',str(idCount),'is a kind of', 'contains'])
		fuel_to_id_dict['Coal'] = idCount
		idCount = idCount + 1

		writer.writerow(['CN',str(idCount),'Biogas'])
		writer.writerow(['CL','84870361',str(idCount),'is a kind of', 'contains'])
		fuel_to_id_dict['Waste'] = idCount
		fuel_to_id_dict['Biogas'] = idCount
		idCount = idCount + 1
		
		writer.writerow(['CN',str(idCount),'Petcoke'])
		writer.writerow(['CL','85165481',str(idCount),'is a kind of', 'contains'])
		fuel_to_id_dict['Petcoke'] = idCount
		idCount = idCount + 1

	owners = set()
	with open(plants_file,'r+') as f:
		reader = csv.reader(f)

		#Create nodes for power plants

		counter = 0
		length = sum(1 for row in reader)
		f.seek(0)

		headers = next(reader)
		print headers

		with open(output_file, 'a+') as csvfile:
			writer = csv.writer(csvfile,lineterminator = '\n')
			for row in reader:
				name = row[2].title()

				fuel1 = row[7]
				fuel2 = row[8]
				fuel3 = row[9]
				fuel4 = row[10]

				owner = row[12]
				country = row[1]
				gppd_idnr = row[3]

				if(owner != ""):

					if(fuel4 != "" and fuel4 != "Other"):
						description = name + " is a " + fuel1 + ", " + fuel2 + ", " + fuel3 + " and " + fuel4 + " plant owned by " + owner + " in " + country
					elif(fuel3 != "" and fuel3 != "Other"):
						description = name + " is a " + fuel1 + ", " + fuel2 + " and " + fuel3 + " plant owned by " + owner + " in " + country
					elif(fuel2 != "" and fuel2 != "Other"):
						description = name + " is a " + fuel1 + " and " + fuel2 + " plant owned by " + owner + " in " + country
					elif(fuel1 != "" and fuel1 != "Other"):
						description = name + " is a " + fuel1 + " plant owned by " + owner + " in " + country
					else:
						continue

				else:
					if(fuel4 != "" and fuel4 != "Other"):
						description = name + " is a " + fuel1 + ", " + fuel2 + ", " + fuel3 + " and " + fuel4 + " plant in " + country
					elif(fuel3 != "" and fuel3 != "Other"):
						description = name + " is a " + fuel1 + ", " + fuel2 + " and " + fuel3 + " plant in " + country
					elif(fuel2 != "" and fuel2 != "Other"):
						description = name + " is a " + fuel1 + " and " + fuel2 + " plant in " + country
					elif(fuel1 != "" and fuel1 != "Other"):
						description = name + " is a " + fuel1 + " plant in " + country
					else:
						continue

				writer.writerow(['CN',str(idCount),name,'description',description,'gppd_idnr',gppd_idnr])
				writer.writerow(['CL','84873253',str(idCount),'is a kind of', 'contains'])

				country_id = countries_name_to_id[country]
				if(country_id != None):
					writer.writerow(['CL',str(country_id),str(idCount),"is located in", "is the location of"])

				if fuel_to_id_dict.get(fuel1) != None:
					writer.writerow(['CL',str(idCount),str(fuel_to_id_dict.get(fuel1)),'is produced by','produces'])
				if fuel_to_id_dict.get(fuel2) != None:
					writer.writerow(['CL',str(idCount),str(fuel_to_id_dict.get(fuel2)),'is produced by','produces'])
				if fuel_to_id_dict.get(fuel3) != None:
					writer.writerow(['CL',str(idCount),str(fuel_to_id_dict.get(fuel3)),'is produced by','produces'])
				if fuel_to_id_dict.get(fuel4) != None:
					writer.writerow(['CL',str(idCount),str(fuel_to_id_dict.get(fuel4)),'is produced by','produces'])

				owners.add(owner.title())
				idCount = idCount + 1

				if(counter % 50 == 0):
					print("Progress: ",counter * 100.0 / length, " %")
				counter = counter + 1
		#Create nodes for owners
		with open(output_file, 'a+') as csvfile:
			writer = csv.writer(csvfile,lineterminator='\n')
			for owner in owners:
				writer.writerow(['CN',str(idCount),owner])
				writer.writerow(['CL','85165554',str(idCount),'is a kind of', 'contains'])
				idCount = idCount + 1


if __name__ == '__main__':
	main()