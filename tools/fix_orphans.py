import csv

old_backup = 'old_backup.csv'
august_backup = 'august_backup.csv'
old_to_new = 'old_to_new.csv'
august_clusters_file = 'august_clusters.csv' 
links_file = 'links.csv'
created_CSV_file = 'fixed.csv'

class Link:
	def __init__(self, id1, id2):
		self.id1 = id1
		self.id2 = id2

def load_august_backup():
	nodes = dict()
	with open(august_backup,'r+') as f:
		reader = csv.reader(f)
		for row in reader:
			a_id = str(row[0])
			name = str(row[1])
			nodes[name] = a_id
	return nodes

def load_old_backup():
	nodes = dict()
	with open(old_backup,'r+') as f:
		reader = csv.reader(f)
		for row in reader:
			title = str(row[0])
			old_cluster = str(row[1])
			nodes[title] = old_cluster
	return nodes

def load_august_clusters():
	nodes = dict()
	with open(august_clusters_file,'r+') as f:
		reader = csv.reader(f)
		for row in reader:
			title = str(row[0])
			ID = str(row[1])
			nodes[title] = ID
	return nodes

def load_old_to_new():
	nodes = dict()
	with open(old_to_new,'r+') as f:
		reader = csv.reader(f)
		for row in reader:
			title = str(row[0])
			ID = str(row[1])
			nodes[title] = ID
	return nodes

def load_links():
	links = list()
	with open(links_file,'r+') as f:
		reader = csv.reader(f)
		for row in reader:
			id_1 = str(row[0])[6:]
			id_2 = str(row[1])[6:]
			links.append(Link(id_1,id_2))
	return links


def title_in_august(title,august_titles):
	if title in august_titles:
		return august_titles[title]
	return "-1"

def link_exists(c_id,id,links):
	for link in links:
		if link.id1 == c_id:
			if link.id2 == id:
				return True
		elif link.id1 == id:
			if link.id2 == c_id:
				return True
	return False

def linked_to_cluster(id,clusters,links):
	for key,c_id in clusters.iteritems():
		if link_exists(c_id,id,links):
			return True
	return False
def linked_to_cluster_csv(id,clusters):
	with open(created_CSV_file,'r+') as f:
		reader = csv.reader(f)
		for row in reader:
			if(len(row) > 3):
				c = str(row[2])
				if c == id:
					return True#return str(row[1]) in clusters
	return False

def main():
	august_titles = load_august_backup()
	backup_titles = load_old_backup()
	old_to_new_conversion = load_old_to_new()
	august_clusters = load_august_clusters()
	links = load_links()

	lent = len(backup_titles) + len(august_titles)
	count = 0.0
	with open(created_CSV_file, 'a+') as csvfile:
		writer = csv.writer(csvfile,lineterminator = '\n')
		
		for b_title,b_cluster in backup_titles.iteritems():
			count = count + 1
			if (count % 20 == 0):
				print (count * 100 / lent, '%')
			#is the title in august_titles
			a_ID = title_in_august(b_title,august_titles)
			if(a_ID == '-1'):
				continue
			still_valid = linked_to_cluster(a_ID,august_clusters,links)
			if(still_valid):
				continue
			#print a_ID,b_title,b_cluster
			new_id = old_to_new_conversion.get(b_cluster)
			if(new_id == None):
				continue
			
			writer.writerow(['CL',str(new_id),str(a_ID),'is categorised as','categorises'])
			#print("CL,"+str(new_id)+","+str(a_ID)+ ",is categorized as,categories")

		for name, a_id in august_titles.iteritems():
			count = count + 1
			if(linked_to_cluster_csv(a_id, august_clusters)):
				continue
			if(linked_to_cluster(a_id,august_clusters,links)):
				continue
			if (count % 10 == 0):
				print (count * 100 / lent, '%')	
			writer.writerow(['CL','85166420',str(a_id),'is categorised as','categorises'])
			#print("CL,"+'85166420'+","+str(a_id)+ ",is categorized as,categories")

if __name__ == '__main__':
	main()