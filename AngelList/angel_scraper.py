# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import sys
import codecs
import csv
import json
import time
from selenium import webdriver

reload(sys)
sys.setdefaultencoding('utf8')
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

list_of_urls = ['https://angel.co/companies?locations[]=1776-Montreal', 'https://angel.co/companies?locations[]=1776-Montreal&company_types[]=Startup','https://angel.co/companies?locations[]=1776-Montreal&company_types[]=VC+Firm&company_types[]=Private+Company&company_types[]=Incubator&company_types[]=SaaS&company_types[]=Mobile+App','https://angel.co/companies?locations[]=1776-Montreal&markets[]=E-Commerce','https://angel.co/companies?locations[]=1776-Montreal&markets[]=Education&markets[]=Games&markets[]=Healthcare','https://angel.co/companies?locations[]=1776-Montreal&markets[]=Enterprise+Software','https://angel.co/companies?locations[]=1776-Montreal&markets[]=Mobile','https://angel.co/companies?locations[]=1776-Montreal&stage[]=Seed&stage[]=Series+A&stage[]=Series+B&stage[]=Series+C&stage[]=Acquired',
'https://angel.co/companies?locations[]=1702-Toronto,+Ontario&company_types[]=Mobile+App&company_types[]=SaaS&company_types[]=Incubator&company_types[]=VC+Firm','https://angel.co/companies?locations[]=1702-Toronto,+Ontario&company_types[]=Startup','https://angel.co/companies?locations[]=1702-Toronto,+Ontario&company_types[]=Private+Company','https://angel.co/companies?locations[]=1702-Toronto,+Ontario&markets[]=E-Commerce','https://angel.co/companies?locations[]=1702-Toronto,+Ontario&markets[]=Education&markets[]=Games','https://angel.co/companies?locations[]=1702-Toronto,+Ontario&markets[]=Enterprise+Software','https://angel.co/companies?locations[]=1702-Toronto,+Ontario&markets[]=Enterprise+Software&company_types[]=Startup','https://angel.co/companies?locations[]=1702-Toronto,+Ontario&markets[]=Enterprise+Software&stage[]=Seed&stage[]=Series+A&stage[]=Series+B&stage[]=Series+C&stage[]=Acquired','https://angel.co/companies?locations[]=1702-Toronto,+Ontario&markets[]=Enterprise+Software&teches[]=Javascript&teches[]=HTML5&teches[]=Python&teches[]=Java&teches[]=CSS','https://angel.co/companies?locations[]=1702-Toronto,+Ontario&markets[]=Healthcare','https://angel.co/companies?locations[]=1702-Toronto,+Ontario&markets[]=Mobile','https://angel.co/companies?locations[]=1702-Toronto,+Ontario&markets[]=Mobile&raised[min]=10000&raised[max]=100000000','https://angel.co/companies?locations[]=1702-Toronto,+Ontario&markets[]=Mobile&markets[]=Enterprise+Software&stage[]=Seed&stage[]=Series+A&stage[]=Series+B&stage[]=Series+C&stage[]=Acquired']
database_file = 'database_json.json'
old_scrape_file = 'angel_output_old.csv'
created_tags_file = 'created_tags.csv'

output_file = "angel_output.csv"
additional_info_output_file = 'angel_additional.csv'

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

def load_angel_startup_urls(filename):
	soup = BeautifulSoup(open(filename), "html.parser")
	count = 0
	urls = list()
	for startup in soup.findAll('a',{'class': 'startup-link'}):
		if(startup.get('title') != None):
			urls.append(startup.get('href'))
			count = count + 1
	return urls

def load_already_done(filename):
	companies = list()
	with open(filename,'r+') as f:
		reader = csv.reader(f)
		for row in reader:
			if(len(row) >= 1):
				companies.append(row[0])
				#0 = angel url
				#1 = company name
				#2 = employees
	return companies

def already_done(angel_url, companies):
	return angel_url in companies

def load_previous_scrape(filename):
	idCount = 0
	with open(filename,'r+') as f:
		reader = csv.reader(f)
		for row in reader:
			if(len(row) >= 1 and row[0] == 'CN'):
				idCount = int(row[1])
	return idCount + 1
def load_created_tags(filename):
	tags = dict()
	with open(filename,'r+') as f:
		reader = csv.reader(f)
		for row in reader:
			if(len(row) == 2):
				tags[str(row[0])] = str(row[1])

	return tags

def main():
	#with open(additional_info_output_file, 'w+') as csvfile1:
	#	writer1 = csv.writer(csvfile1,lineterminator = '\n')	
	database_nodes = load_nodes(database_file)
	already_done_companies = load_already_done(additional_info_output_file)
	idCount = load_previous_scrape(old_scrape_file)
	createdTags = load_created_tags(created_tags_file)

	startup_urls = list()
	browser = webdriver.Chrome()	
	#start_url = 'https://angel.co/companies?locations[]=1776-Montreal&markets[]=E-Commerce'
	start_url = list_of_urls[8]
	browser.get(start_url)
	try:
		while(True):
			time.sleep(3)
			button = browser.find_element_by_class_name('more')
			button.click()
	except Exception as e:
		pass
	time.sleep(3)
	table = browser.find_element_by_class_name('results')
	first = True
	for row in table.find_elements_by_class_name('dc59'):
		if(first):
			first = False
			continue
		startup_name =  row.find_element_by_class_name('name').text#.text#, row.find_element_by_class_name('startup-link').href 
		startup_url =  row.find_element_by_class_name('startup-link').get_attribute('href')
		startup_urls.append(startup_url)
		#print row.find_element_by_class_name('company_size').find_element_by_tag_name('div').text#.find_element_by_class_name('h_desc').text
		#print row.find_element_by_class_name('stage').text#.find_element_by_class_name('value').text
		#print row.find_element_by_class_name('raised').text#find_element_by_class_name('value').text

	#Create file
	with open(output_file,'w+') as csvfile1:
		writer1 = csv.writer(csvfile1,lineterminator = '\n')
	
	#startup_urls = load_angel_startup_urls(montreal_html_file)
	#toronto_urls = load_angel_startup_urls(toronto_html_file)
	#for url in toronto_urls:
	#	startup_urls.append(url)

	for angel_url in startup_urls:
		if(already_done(angel_url,already_done_companies)):
			print("skip: " + angel_url)
			continue
		response = requests.get(angel_url)
		#soup = BeautifulSoup(response.text,'html.parser')
		browser.get(angel_url)
		failed = 0
		while(browser.title == "AngelList"):
			failed = failed + 1
			if(failed == 5):
				print ("Failed 5 times, crashing")
				break
			print("Sleeping due to captcha. You have 90 seconds to solve the captcha")
			time.sleep(90)
			browser.get(angel_url)
		print ("Loaded: " + browser.title)
		time.sleep(5)

		company_name = browser.find_element_by_tag_name('h1').text
		try:
			more_description_button = browser.find_element_by_class_name('hidden_more')
			more_description_button.click()
		except Exception as e:
			pass
		try:
			description = browser.find_element_by_class_name('product_desc').text
		except Exception as e:
			description = ""
		try:
			startup_url = browser.find_element_by_class_name('company_url').text
		except Exception as e:
			startup_url = ""
		startup_id = idCount
		idCount = idCount + 1
		with open(output_file,'a+') as csvfile1:
			writer1 = csv.writer(csvfile1,lineterminator = '\n')
			if(description != "" and startup_url != ""):
				writer1.writerow(['CN',str(startup_id),company_name,'description',description,'reference',startup_url])
			elif(description != "" and startup_url == ""):
				writer1.writerow(['CN',str(startup_id),company_name,'description',description,'reference',angel_url])
			elif(description == "" and startup_url != ""):
				writer1.writerow(['CN',str(startup_id),company_name,'reference',startup_url])
			else:
				writer1.writerow(['CN',str(startup_id),company_name,'reference',angel_url])

		try:
			locations_tag = browser.find_element_by_class_name('js-location_tags')
			locations = locations_tag.find_elements_by_class_name('tag')
			with open(output_file,'a+') as csvfile1:
				writer1 = csv.writer(csvfile1,lineterminator = '\n')
				for location in locations:
					city = location.text
					location_id = database_nodes.get(city)

					if(location_id != None):
						writer1.writerow(['CL',str(location_id),str(startup_id),'is located in', 'is the location of'])
					elif(city == 'Montreal'):
						writer1.writerow(['CL','85246113',str(startup_id),'is located in', 'is the location of'])
					elif(city == 'Toronto'):
						writer1.writerow(['CL','85246323',str(startup_id),'is located in', 'is the location of'])
					elif(city == 'Washington DC'):
						writer1.writerow(['CL','85244878',str(startup_id),'is located in', 'is the location of'])	
					elif(database_nodes.get(city + " (United States)") != None):
						writer1.writerow(['CL',database_nodes.get(city + " (United States)"),str(startup_id),'is located in', 'is the location of'])
					elif(database_nodes.get(city + " (Canada)") != None):
						writer1.writerow(['CL',database_nodes.get(city + " (Canada)"),str(startup_id),'is located in', 'is the location of'])			
					else:
						print city + " not found"
		except Exception as e:
			print("City broken for " + angel_url)
		try:
			full_tags = browser.find_element_by_class_name('js-market_tags')
			tags = full_tags.find_elements_by_class_name('tag')
			with open(output_file,'a+') as csvfile1:
				writer1 = csv.writer(csvfile1,lineterminator = '\n')
				for tag in tags:
					this_tag = tag.text
					tag_id = createdTags.get(this_tag)
					if(tag_id == None):
						tag_id = database_nodes.get(this_tag)
						if(tag_id == None):
							tag_id = idCount
							idCount = idCount + 1
							writer1.writerow(['CN',str(tag_id),this_tag])
							writer1.writerow(['CL',str(tag_id)])
							createdTags[this_tag] = tag_id
							with open(created_tags_file, 'a+') as csvfile2:
								writer2 = csv.writer(csvfile2,lineterminator = '\n')
								writer2.writerow([this_tag,str(tag_id)])
					writer1.writerow(['CL',str(startup_id),str(tag_id),'is specialized in by','specializes in'])
		except Exception as e:
			print("No tags for " + angel_url)
		try:
			employees = browser.find_element_by_class_name('js-company_size').text
		except Exception as e:
			employees = '-'
		try:
			stage = browser.find_element_by_class_name('dsr49').find_element_by_class_name('type').text
			raised = browser.find_element_by_class_name('dsr49').find_element_by_class_name('raised').text
		except Exception as e:
			stage = ''
			raised = ''

		with open(additional_info_output_file, 'a+') as csvfile1:
			writer1 = csv.writer(csvfile1,lineterminator = '\n')
			writer1.writerow([str(angel_url),company_name,employees,stage,raised])
			already_done_companies.append(angel_url)

	browser.close()

if __name__ == '__main__':
	main()
'''from selenium import webdriver


browser = webdriver.Chrome() #replace with .Firefox(), or with the browser of your choice
url = "https://angel.co/companies?locations[]=1776-Montreal&locations[]=1702-Toronto,+Ontario&company_types[]=Startup"
browser.get(url) #navigate to the page

delay = 3 # seconds
try:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
    print "Page is ready!"
    myElem.click()
except TimeoutException:
    print "Loading took too much time!"

more_button = browser.find_element_by_class_name('more')
more_button.click()'''