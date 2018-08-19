import csv
terms_to_collect_file = 'database_terms.csv' #Terms to gather table

def loadGatherTerms():
	''' Load the terms to gather table from a predefined csv file
		Returns:
			dictionary with key being lower case word (and plural versions) and value being the database ID
	'''	
	terms = dict()
	with open(terms_to_collect_file) as f:
		for line in f.readlines():
			words = line.split(',')
			temp_id = str(words[0])
			for word in words:
				word = word.strip().lower()
				word2 = word + 's'
				word3 = word + 'es'
				if(len(word) > 0 and (word[0] < '0' or word[0] > '9')):
					terms[word] = temp_id
					terms[word2] = temp_id
					terms[word3] = temp_id
	return terms


nouns = ['information','field','extraction','vocabulary','corpus','translation','programming','software','tree','system','data','technology','framework','language','device','network','actvity','branch','approaches','business','way','area','domain','robot','study','studies']

gather_terms = loadGatherTerms()
for key, value in gather_terms.iteritems():
	if key in nouns or key[-1] == 's':
		continue
	print key
