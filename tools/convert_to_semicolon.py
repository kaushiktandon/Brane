# -*- coding: utf-8 -*-

import sys
import codecs
import csv
import time
import json

reload(sys)
sys.setdefaultencoding('utf8')
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

input_file = "../Mitacs/new_links.csv"
output_file = "../Mitacs/new_output_converted.txt"

with open(output_file, 'w+') as csvfile1:
	#writer1 = csv.writer(csvfile1,lineterminator = '\n',delimiter=";")
	with open(input_file,'r+') as f:
		reader = csv.reader(f)
		for row in reader:
			output_string = "";
			for column in row:
				if('\n' in column):
					column = column.replace('\n','')

				output_string = output_string + column + ';'
			#print output_string, len(output_string)
			output_string = output_string.replace("  ", " ")
			csvfile1.write(output_string + '\n')
