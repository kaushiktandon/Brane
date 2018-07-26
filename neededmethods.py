import requests
from BeautifulSoup import *

def getHTML(url):
	try:
		r = requests.get(url)
		return BeautifulSoup(r.text)
	except:
		print("Couldn't get HTML for: " + url)
def extractCategories(soup_html):
	categories = []
	a = soup_html.find('div',{'class': 'mw-normal-catlinks'})
	if a != None:
		for litag in a.findAll('li'):
			categories.append(str(litag.text))
	return categories

#def extractReferences(soup_html):
	#references = []
	#return references

#def extractSeeAlso(soup_html):
	#seeAlso = []
	#return seeAlso


url  = 'https://en.wikipedia.org/wiki/BINA48'
soup = getHTML(url)

categories = extractCategories(soup)
#references = extractReferences(soup)
#seeAlso = extractSeeAlso(soup)