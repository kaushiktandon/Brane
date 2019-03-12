import csv
import sys
import json
import codecs

reload(sys)
sys.setdefaultencoding('utf8')
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

input_file = 'merged.csv'
output_file = 'merged_minus_grid.csv'

with open(output_file, 'w+') as csvfile:
	writer = csv.writer(csvfile,lineterminator = '\n')
	with open(input_file, 'r+') as f:
		reader = csv.reader(f)
		for row in reader:
			if(len(row) >= 1):
				id1 = int(row[1])
				id2 = int(row[2])
				#id1 = int(row[0].split(';')[1])
				#id2 = int(row[0].split(';')[2])
				if((id1 <= 85345579 and id1 >= 85244819) or (id2 >= 85244819 and id2 <= 85345579)):
					continue
				else:
					writer.writerow(row)


