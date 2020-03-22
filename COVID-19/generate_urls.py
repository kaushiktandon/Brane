# -*- coding: utf-8 -*-

import requests
from selenium import webdriver
import time

def get_urls(browser, start_url):
	browser.get(start_url+'1')
	time.sleep(2)
	last_page_num = int(browser.find_element_by_class_name('paginator__last').get_attribute('data-page'))
	print(last_page_num)

	urls = list()
	for page_num in range(1, last_page_num + 1):
		url = start_url + str(page_num)
		browser.get(url)
		time.sleep(2)

		article_elements = browser.find_elements_by_class_name('search-result__title')
		for article_element in article_elements:
			article_url = article_element.find_element_by_tag_name('a').get_attribute('href')
			urls.append(article_url)
	return urls

def main():
	output_file = 'covid_urls.txt'
	options = webdriver.ChromeOptions()
	options.add_argument('--headless')
	options.add_argument('--no-sandbox')
	options.add_argument('--disable-dev-shm-usage')
	browser = webdriver.Chrome(chrome_options=options)
	article_urls_to_do = set()

	start_url = 'https://coronavirus.1science.com/search?query=language%3Aeng&sort=yeardesc&size=50&page='
	urls = get_urls(browser, start_url)
	print(len(urls))
	for url in urls:
		article_urls_to_do.add(url)

	start_url = 'https://coronavirus.1science.com/search?query=language%3Aeng%20journalcountry%3AUSA&sort=yeardesc&size=50&page='
	urls = get_urls(browser, start_url)
	print(len(urls))
	for url in urls:
		article_urls_to_do.add(url)

	start_url = 'https://coronavirus.1science.com/search?query=language%3Aeng%20journalcountry%3A%28GBR%20OR%20NLD%20OR%20DEU%20OR%20CHE%29&sort=yeardesc&size=50&page='
	urls = get_urls(browser, start_url)
	print(len(urls))
	for url in urls:
		article_urls_to_do.add(url)

	start_url = 'https://coronavirus.1science.com/search?query=language%3Aeng%20journal-exact%3A%28%22Journal%20of%20Virology%22%20OR%20Virology%20OR%20%22Avian%20Diseases%22%20OR%20%22Emerging%20Infectious%20Diseases%22%20OR%20%22The%20Journal%20of%20General%20Virology%22%20OR%20%22Archives%20of%20Virology%22%20OR%20%22PloS%20One%22%20OR%20%22Journal%20of%20Medical%20Virology%22%20OR%20%22Virus%20Research%22%20OR%20%22Veterinary%20Microbiology%22%29&sort=yeardesc&size=50&page='
	urls = get_urls(browser, start_url)
	print(len(urls))
	for url in urls:
		article_urls_to_do.add(url)

	start_url = 'https://coronavirus.1science.com/search?query=language%3Aeng%20domain%3A%22Health%20Sciences%22&sort=yeardesc&size=50&page='
	urls = get_urls(browser, start_url)
	print(len(urls))
	for url in urls:
		article_urls_to_do.add(url)

	start_url = 'https://coronavirus.1science.com/search?query=language%3Aeng%20org-exact%3A%28%22University%20of%20Hong%20Kong%22%20OR%20%22Chinese%20University%20of%20Hong%20Kong%22%20OR%20%22Chinese%20Academy%20of%20Sciences%22%20OR%20%22Universiteit%20Utrecht%22%20OR%20%22Centers%20for%20Disease%20Control%20and%20Prevention%20-%20CDC%22%20OR%20%22NIH%20-%20National%20Institutes%20of%20Health%22%20OR%20%22University%20of%20Toronto%22%20OR%20%22Prince%20of%20Wales%20Hospital%40Chinese%20University%20of%20Hong%20Kong%22%20OR%20%22University%20of%20North%20Carolina%20at%20Chapel%20Hill%22%20OR%20%22Chinese%20Academy%20of%20Agricultural%20Sciences%22%20OR%20%22University%20of%20Southern%20California%22%20OR%20%22National%20University%20of%20Singapore%20%28NUS%29%22%20OR%20%22Johns%20Hopkins%20University%22%20OR%20%22University%20of%20Pennsylvania%22%20OR%20%22Queen%20Mary%20Hospital%40University%20of%20Hong%20Kong%22%20OR%20%22CNRS%20-%20Centre%20national%20de%20la%20recherche%20scientifique%22%20OR%20%22University%20of%20Iowa%22%20OR%20%22National%20Taiwan%20University%22%20OR%20%22Ohio%20State%20University%22%20OR%20%22CSIC%20-%20Consejo%20Superior%20de%20Investigaciones%20Cient%C3%ADficas%22%20OR%20%22Harvard%20University%22%20OR%20%22University%20of%20Minnesota-Twin%20Cities%22%20OR%20%22Seoul%20National%20University%22%20OR%20%22University%20of%20Georgia%22%20OR%20%22Cornell%20University%22%20OR%20%22Chinese%20Academy%20of%20Medical%20Sciences%22%20OR%20%22A-STAR%20Agency%20for%20Science%2C%20Technology%20and%20Research%22%20OR%20%22USDA%20-%20US%20Department%20of%20Agriculture%22%20OR%20%22Academia%20Sinica%22%20OR%20%22University%20of%20California%2C%20Davis%22%29&sort=yeardesc&size=50+page='
	urls = get_urls(browser, start_url)
	print(len(urls))
	for url in urls:
		article_urls_to_do.add(url)

	file_output = open(output_file, 'w+')
	for article in article_urls_to_do:
		file_output.write(article+'\n')
	file_output.close()

if __name__ == '__main__':
	main()