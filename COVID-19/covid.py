# -*- coding: utf-8 -*-

import requests
from selenium import webdriver
import time
import csv

def modified_find_element_by_class_name(browser, class_name):
	try:
		val = browser.find_element_by_class_name(class_name).text
		return val
	except Exception as e:
		pass
	return None
def modified_find_element_by_class_name_elem(browser, class_name):
	try:
		val = browser.find_element_by_class_name(class_name)
		return val
	except Exception as e:
		pass
	return None
def load_urls(urls_file):
	urls = list()
	with open(urls_file) as f:
		for line in f:
			urls.append(line)
	return urls
def main():
	urls_file = 'covid_urls.txt'
	output_file = 'covid3.csv'
	#Create file
	with open(output_file,'w+') as csvfile1:
		writer1 = csv.writer(csvfile1,lineterminator = '\n')
		writer1.writerow(['TI', 'AF', 'SO', 'PY', 'VL', 'IS', 'BP', 'EP', 'OA', 'DI', 'NR', 'URL', 'AB', 'RO', 'DE', 'URL2'])

	article_urls_to_do = load_urls(urls_file)

	options = webdriver.ChromeOptions()
	options.add_argument('--headless')
	options.add_argument('--no-sandbox')
	options.add_argument('--disable-dev-shm-usage')
	browser = webdriver.Chrome(chrome_options=options)

	for article_url in article_urls_to_do[13000:]:
		article_url = article_url.strip()
		print(article_url)
		browser.get(article_url)
		time.sleep(0.75)
		article_title = modified_find_element_by_class_name(browser,'itemdetail__title')
		if(article_title == None):
			print(article_url + " has no article title")
			continue
		# Are there more authors?
		try:
			authors_button = modified_find_element_by_class_name_elem(browser, 'btn-link-inline')
			authors_button.click()
			time.sleep(0.25)
		except Exception as e:
			pass
		# Are there more keywords
		try:
			keywords_button = modified_find_element_by_class_name_elem(browser, 'btn-link-inline')
			keywords_button.click()
			time.sleep(0.25)
		except Exception as e:
			pass

		# Attributes to set per article
		authors = ''
		journal = ''
		year_published = ''
		volume = ''
		issue = ''
		start_page = ''
		end_page = ''
		open_access = ''
		doi = ''
		num_citations = ''
		full_url = ''
		abstract = ''
		organizations = ''
		keywords = ''

		authors_elem = modified_find_element_by_class_name(browser, 'search-result__authors')
		if (authors_elem != None):
			if ('by ' in authors_elem):
				authors_elem = authors_elem[3:]
			if (' & ' in authors_elem):
				authors_elem = authors_elem.replace(' & ', ', ')
			for author in authors_elem.split(','):
				author = author.strip()
				if (len(author.split(" ")) > 1):
					last_name = author.split(' ')[-1]
					first_name_elems = author.split(' ')[:-1]
					first_name = ''
					for elem in first_name_elems:
						first_name += elem + " "
					first_name = first_name.strip()
					authors += (last_name + ", " + first_name + "; ")
				else:
					authors += author + '; '
			# Remove extra semicolon
			authors = authors[:-2]
		
		doi = modified_find_element_by_class_name(browser,'itemdetail__doi')
		if (doi != None):
			doi = doi[16:]
		journal = modified_find_element_by_class_name(browser,'itemdetail__journaltitle')
		open_access = modified_find_element_by_class_name(browser,'itemdetail__oa')

		metadata = modified_find_element_by_class_name_elem(browser,'inline-bulleted-list')
		try:
			for elem in metadata.find_elements_by_tag_name('li'):
				if (elem.text == journal and journal != None):
					continue
				elif (elem.text == open_access and open_access != None):
					continue

				volume_exists = elem.text.find('Volume')
				issue_exists = elem.text.find('issue')
				issue_exists2 = elem.text.find("Issue")
				pages_exists = elem.text.find('pages')
				pages_exists2 = elem.text.find('Pages')
				page_exists = elem.text.find('page ')
				page_exists2 = elem.text.find('Page ')
				if (volume_exists != -1):
					end = elem.text.find(',', volume_exists)
					if (end == -1):
						end = len(elem.text)
					volume = elem.text[volume_exists + len('Volume') + 1: end]
				if (issue_exists != -1):
					end = elem.text.find(',', issue_exists)
					if (end == -1):
						end = len(elem.text)
					issue = elem.text[issue_exists + len('issue') + 1: end]
				if (issue_exists2 != -1):
					end = elem.text.find(',', issue_exists2)
					if end == -1:
						end = len(elem.text)
					issue = elem.text[issue_exists2 + len('issue') + 1: end]
				if (pages_exists != -1):
					pages = elem.text[pages_exists + len('pages') + 1:]
					start_page = pages[:pages.find('-')]
					end_page = pages[pages.find('-') + 1:]
				if (page_exists != -1):
					start_page = elem.text[page_exists + len('page') + 1 :]
				if (pages_exists2 != -1):
					pages = elem.text[pages_exists2 + len('Pages') + 1:]
					start_page = pages[:pages.find('-')]
					end_page = pages[pages.find('-') + 1:]
				if (page_exists2 != -1):
					start_page = elem.text[page_exists2 + len('Page') + 1 :]
				if (volume_exists == -1 and issue_exists == -1 and pages_exists == -1 and pages_exists == -1 and pages_exists2 == -1 and page_exists2 == -1 and issue_exists2 == -1):
					year_published = elem.text
		except Exception as e:
			pass

		num_citations = modified_find_element_by_class_name(browser,'search-result__metrics-line__citations')
		if (num_citations != None):
			num_citations = num_citations[: num_citations.find(' ')]
		else:
			num_citations = ''

		full_text_url_elem = modified_find_element_by_class_name_elem(browser, 'search-result__full-text-link')
		if (full_text_url_elem != None):
			full_url = full_text_url_elem.get_attribute('href')

		abstract = modified_find_element_by_class_name(browser, 'itemdetail__abstract')

		keyword_elems = modified_find_element_by_class_name_elem(browser, 'itemdetail__keywords')
		try:
			for elem in keyword_elems.find_elements_by_tag_name('li'):
				keywords += elem.text + '; '
			keywords = keywords[:-2]
		except Exception as e:
			pass

		try:
			organization_headers = browser.find_elements_by_class_name('itemdetail__heading')
			real_elem = None
			for elem in organization_headers:
				if elem.text == 'ORGANIZATION':
					real_elem = elem
					break
			if real_elem != None:
				xpath = "//h2[@class='itemdetail__heading']/following-sibling::ul"
				organization_elem = browser.find_element_by_xpath(xpath)

				for val in organization_elem.find_elements_by_tag_name('li'):
					if (val.text != ''):
						organizations += val.text + '; '
				organizations = organizations[:-2]
		except Exception as e:
			pass
		with open(output_file, 'a+', encoding='utf8') as csvfile1:
			writer1 = csv.writer(csvfile1,lineterminator = '\n')
			writer1.writerow([article_title, str(authors),journal,year_published,volume,issue, str(start_page), str(end_page), open_access, doi, str(num_citations), full_url, abstract, organizations, keywords, article_url])

		#print(
		#	"\n-----------\ntile={article_title}\nauthors = {authors}\njournal = {journal}\nyear_published = {year_published}\nvolume = {volume}\nissue = {issue}\nstart_page = {start_page}\nend_page = {end_page}\nopen_access = {open_access}\ndoi = {doi}\nnum_citations = {num_citations}\nfull_url = {full_url}\nabstract = {abstract}\norganizations = {organizations}\nkeywords = {keywords}".format
		#	(article_title=article_title, authors=authors, journal=journal, year_published=year_published, volume=volume, issue=issue, start_page=start_page, end_page=end_page, open_access=open_access, doi=doi, num_citations=num_citations, full_url=full_url, abstract=abstract , organizations=organizations, keywords=keywords))
	browser.close()
if __name__ == '__main__':
	main()