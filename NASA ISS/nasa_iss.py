'''
	Kaushik Tandon
	January - February 2020
	NASA Web Of Science + ISS conversion for The Brane
'''

import json
import csv
import numpy as np
import pandas as pd

class Convert_Clusters():
	def __init__(self):
		print("Create clusters")
	def convert_clusters(self):
		cluster_topics = list()
		cluster_links = list()
		properties = dict()

		# Create generic properties
		properties['_key'] = ''
		properties['_type'] = ''
		properties['title'] = ""
		properties['terms'] = ''
		properties['definition'] = ''
		properties['sources'] = ''
		properties['firstName'] = ''
		properties['lastName'] = ''
		properties['initials'] = ''
		properties['email'] = ''
		properties['orcidID'] = ''
		properties['Possible_Duplicates'] = ''
		properties['Notes'] = ''
		properties['valueType'] = ''

		# T1
		properties['_key'] = 'T1'
		properties['_type'] = 'system'
		properties['title'] = "ISS investigation"
		cluster_topics.append(self.create_topic(properties))
		# T2
		properties['_key'] = 'T2'
		properties['_type'] = 'cluster'
		properties['title'] = "Individual"
		cluster_topics.append(self.create_topic(properties))
		# T3
		properties['_key'] = 'T3'
		properties['_type'] = 'cluster'
		properties['title'] = "Researcher"
		cluster_topics.append(self.create_topic(properties))
		# T4
		properties['_key'] = 'T4'
		properties['_type'] = 'cluster'
		properties['title'] = "Event"
		cluster_topics.append(self.create_topic(properties))
		# T5
		properties['_key'] = 'T5'
		properties['_type'] = 'cluster'
		properties['title'] = "Conference"
		cluster_topics.append(self.create_topic(properties))
		# T6
		properties['_key'] = 'T6'
		properties['_type'] = 'cluster'
		properties['title'] = "Workshop"
		cluster_topics.append(self.create_topic(properties))
		# T7
		properties['_key'] = 'T7'
		properties['_type'] = 'cluster'
		properties['title'] = "Symposium"
		cluster_topics.append(self.create_topic(properties))
		# T8
		properties['_key'] = 'T8'
		properties['_type'] = 'cluster'
		properties['title'] = "Congress"
		cluster_topics.append(self.create_topic(properties))
		# T9
		properties['_key'] = 'T9'
		properties['_type'] = 'cluster'
		properties['title'] = "Meeting"
		cluster_topics.append(self.create_topic(properties))
		# T10
		properties['_key'] = 'T10'
		properties['_type'] = 'cluster'
		properties['title'] = "Publication"
		cluster_topics.append(self.create_topic(properties))
		# T11
		properties['_key'] = 'T11'
		properties['_type'] = 'cluster'
		properties['title'] = "Journal"
		cluster_topics.append(self.create_topic(properties))
		# T12
		properties['_key'] = 'T12'
		properties['_type'] = 'cluster'
		properties['title'] = "Conference Proceeding"
		cluster_topics.append(self.create_topic(properties))
		# T13
		properties['_key'] = 'T13'
		properties['_type'] = 'cluster'
		properties['title'] = "Article"
		cluster_topics.append(self.create_topic(properties))
		# T14
		properties['_key'] = 'T14'
		properties['_type'] = 'property'
		properties['title'] = "Access type"
		properties['valueType'] = 'String'		
		cluster_topics.append(self.create_topic(properties))
		# T15
		properties['_key'] = 'T15'
		properties['_type'] = 'property'
		properties['title'] = "Download date"
		properties['valueType'] = 'Date'		
		cluster_topics.append(self.create_topic(properties))
		# T16
		properties['_key'] = 'T16'
		properties['_type'] = 'property'
		properties['title'] = "Publication type"
		properties['valueType'] = 'String'		
		cluster_topics.append(self.create_topic(properties))
		# T17
		properties['_key'] = 'T17'
		properties['_type'] = 'property'
		properties['title'] = "Language"
		properties['valueType'] = 'String'		
		cluster_topics.append(self.create_topic(properties))
		# T18
		properties['_key'] = 'T18'
		properties['_type'] = 'property'
		properties['title'] = "Published date"
		properties['valueType'] = 'Date'		
		cluster_topics.append(self.create_topic(properties))
		# T19
		properties['_key'] = 'T19'
		properties['_type'] = 'property'
		properties['title'] = "Document type"
		properties['valueType'] = 'String'		
		cluster_topics.append(self.create_topic(properties))
		# T20
		properties['_key'] = 'T20'
		properties['_type'] = 'property'
		properties['title'] = "Conference year"
		properties['valueType'] = 'String'		
		cluster_topics.append(self.create_topic(properties))
		# T21
		properties['_key'] = 'T21'
		properties['_type'] = 'cluster'
		properties['title'] = "Organization"
		properties['valueType'] = ''		
		cluster_topics.append(self.create_topic(properties))
		# T22
		properties['_key'] = 'T22'
		properties['_type'] = 'cluster'
		properties['title'] = "Research organization"
		cluster_topics.append(self.create_topic(properties))
		# T23
		properties['_key'] = 'T23'
		properties['_type'] = 'cluster'
		properties['title'] = "Publisher"
		cluster_topics.append(self.create_topic(properties))
		# T24
		properties['_key'] = 'T24'
		properties['_type'] = 'cluster'
		properties['title'] = "Keyword"
		cluster_topics.append(self.create_topic(properties))
		# T25
		properties['_key'] = 'T25'
		properties['_type'] = 'cluster'
		properties['title'] = 'Tagged Keyword'
		cluster_topics.append(self.create_topic(properties))
		# T26
		properties['_key'] = 'T26'
		properties['_type'] = 'cluster'
		properties['title'] = 'Untagged Keyword'
		cluster_topics.append(self.create_topic(properties))
		# T27
		properties['_key'] = 'T27'
		properties['_type'] = 'cluster'
		properties['title'] = 'Investigation'
		cluster_topics.append(self.create_topic(properties))
		# T29
		properties['_key'] = 'T29'
		properties['_type'] = 'cluster'
		properties['title'] = 'Space agency'
		cluster_topics.append(self.create_topic(properties))
		# T30
		properties['_key'] = 'T30'
		properties['_type'] = 'cluster'
		properties['title'] = 'Sponsoring organization'
		cluster_topics.append(self.create_topic(properties))
		# T31
		properties['_key'] = 'T31'
		properties['_type'] = 'cluster'
		properties['title'] = 'Principal investigator'
		cluster_topics.append(self.create_topic(properties))
		# T32
		properties['_key'] = 'T32'
		properties['_type'] = 'cluster'
		properties['title'] = 'City'
		cluster_topics.append(self.create_topic(properties))
		# T33
		properties['_key'] = 'T33'
		properties['_type'] = 'cluster'
		properties['title'] = 'State'
		cluster_topics.append(self.create_topic(properties))
		# T34
		properties['_key'] = 'T34'
		properties['_type'] = 'cluster'
		properties['title'] = 'Country'
		cluster_topics.append(self.create_topic(properties))
		# T35
		properties['_key'] = 'T35'
		properties['_type'] = 'property'
		properties['title'] = 'Operations location'
		cluster_topics.append(self.create_topic(properties))
		# T36
		properties['_key'] = 'T36'
		properties['_type'] = 'cluster'
		properties['title'] = 'Academic activity'
		cluster_topics.append(self.create_topic(properties))
		# T37
		properties['_key'] = 'T37'
		properties['_type'] = 'cluster'
		properties['title'] = 'Location'
		cluster_topics.append(self.create_topic(properties))
		# T38
		properties['_key'] = 'T38'
		properties['_type'] = 'cluster'
		properties['title'] = 'Category'
		cluster_topics.append(self.create_topic(properties))
		# T39
		properties['_key'] = 'T39'
		properties['_type'] = 'cluster'
		properties['title'] = 'Biology and Biotechnology'
		cluster_topics.append(self.create_topic(properties))
		# T40
		properties['_key'] = 'T40'
		properties['_type'] = 'cluster'
		properties['title'] = 'Animal Biology - Invertebrates'
		cluster_topics.append(self.create_topic(properties))
		# T41
		properties['_key'] = 'T41'
		properties['_type'] = 'cluster'
		properties['title'] = 'Animal Biology - Vertebrates'
		cluster_topics.append(self.create_topic(properties))
		# T42
		properties['_key'] = 'T42'
		properties['_type'] = 'cluster'
		properties['title'] = 'Cellular Biology'
		cluster_topics.append(self.create_topic(properties))
		# T43
		properties['_key'] = 'T43'
		properties['_type'] = 'cluster'
		properties['title'] = 'Macromolecular Crystal Growth'
		cluster_topics.append(self.create_topic(properties))
		# T44
		properties['_key'] = 'T44'
		properties['_type'] = 'cluster'
		properties['title'] = 'Microbiology'
		cluster_topics.append(self.create_topic(properties))
		# T45
		properties['_key'] = 'T45'
		properties['_type'] = 'cluster'
		properties['title'] = 'Microencapsulation'
		cluster_topics.append(self.create_topic(properties))
		# T46
		properties['_key'] = 'T46'
		properties['_type'] = 'cluster'
		properties['title'] = 'Plant Biology'
		cluster_topics.append(self.create_topic(properties))
		# T47
		properties['_key'] = 'T47'
		properties['_type'] = 'cluster'
		properties['title'] = 'Vaccine Development'
		cluster_topics.append(self.create_topic(properties))
		# T48
		properties['_key'] = 'T48'
		properties['_type'] = 'cluster'
		properties['title'] = 'Earth and Space Science'
		cluster_topics.append(self.create_topic(properties))
		# T49
		properties['_key'] = 'T49'
		properties['_type'] = 'cluster'
		properties['title'] = 'Astrobiology'
		cluster_topics.append(self.create_topic(properties))
		# T50
		properties['_key'] = 'T50'
		properties['_type'] = 'cluster'
		properties['title'] = 'Astrophysics'
		cluster_topics.append(self.create_topic(properties))
		# T51
		properties['_key'] = 'T51'
		properties['_type'] = 'cluster'
		properties['title'] = 'Earth Remote Sensing'
		cluster_topics.append(self.create_topic(properties))
		# T52
		properties['_key'] = 'T52'
		properties['_type'] = 'cluster'
		properties['title'] = 'Heliophysics'
		cluster_topics.append(self.create_topic(properties))
		# T53
		properties['_key'] = 'T53'
		properties['_type'] = 'cluster'
		properties['title'] = 'Educational and cultural activities'
		cluster_topics.append(self.create_topic(properties))
		# T54
		properties['_key'] = 'T54'
		properties['_type'] = 'cluster'
		properties['title'] = 'Classroom Versions of ISS Investigations'
		cluster_topics.append(self.create_topic(properties))
		# T55
		properties['_key'] = 'T55'
		properties['_type'] = 'cluster'
		properties['title'] = 'Educational Competitions'
		cluster_topics.append(self.create_topic(properties))
		# T56
		properties['_key'] = 'T56'
		properties['_type'] = 'cluster'
		properties['title'] = 'Educational Demonstrations'
		cluster_topics.append(self.create_topic(properties))
		# T57
		properties['_key'] = 'T57'
		properties['_type'] = 'cluster'
		properties['title'] = 'Student-Developed Investigations'
		cluster_topics.append(self.create_topic(properties))
		# T58
		properties['_key'] = 'T58'
		properties['_type'] = 'cluster'
		properties['title'] = 'Human Research'
		cluster_topics.append(self.create_topic(properties))
		# T59
		properties['_key'] = 'T59'
		properties['_type'] = 'cluster'
		properties['title'] = 'Bone and Muscle Physiology'
		cluster_topics.append(self.create_topic(properties))
		# T60
		properties['_key'] = 'T60'
		properties['_type'] = 'cluster'
		properties['title'] = 'Cardiovascular and Respiratory Systems'
		cluster_topics.append(self.create_topic(properties))
		# T61
		properties['_key'] = 'T61'
		properties['_type'] = 'cluster'
		properties['title'] = 'Crew Healthcare Systems'
		cluster_topics.append(self.create_topic(properties))
		# T62
		properties['_key'] = 'T62'
		properties['_type'] = 'cluster'
		properties['title'] = 'Habitability and Human Factors'
		cluster_topics.append(self.create_topic(properties))
		# T63
		properties['_key'] = 'T63'
		properties['_type'] = 'cluster'
		properties['title'] = 'Human Behavior and Performance'
		cluster_topics.append(self.create_topic(properties))
		# T64
		properties['_key'] = 'T64'
		properties['_type'] = 'cluster'
		properties['title'] = 'Human Microbiome'
		cluster_topics.append(self.create_topic(properties))
		# T65
		properties['_key'] = 'T65'
		properties['_type'] = 'cluster'
		properties['title'] = 'Immune System'
		cluster_topics.append(self.create_topic(properties))
		# T66
		properties['_key'] = 'T66'
		properties['_type'] = 'cluster'
		properties['title'] = 'Integrated Physiology and Nutrition'
		cluster_topics.append(self.create_topic(properties))
		# T67
		properties['_key'] = 'T67'
		properties['_type'] = 'cluster'
		properties['title'] = 'Nervous and Vestibular Systems'
		cluster_topics.append(self.create_topic(properties))
		# T68
		properties['_key'] = 'T68'
		properties['_type'] = 'cluster'
		properties['title'] = 'Radiation Impacts on Humans'
		cluster_topics.append(self.create_topic(properties))
		# T69
		properties['_key'] = 'T69'
		properties['_type'] = 'cluster'
		properties['title'] = 'Vision'
		cluster_topics.append(self.create_topic(properties))
		# T70
		properties['_key'] = 'T70'
		properties['_type'] = 'cluster'
		properties['title'] = 'Physical science'
		cluster_topics.append(self.create_topic(properties))
		# T71
		properties['_key'] = 'T71'
		properties['_type'] = 'cluster'
		properties['title'] = 'Combustion Science'
		cluster_topics.append(self.create_topic(properties))
		# T72
		properties['_key'] = 'T72'
		properties['_type'] = 'cluster'
		properties['title'] = 'Complex Fluids'
		cluster_topics.append(self.create_topic(properties))
		# T73
		properties['_key'] = 'T73'
		properties['_type'] = 'cluster'
		properties['title'] = 'Fluid Physics'
		cluster_topics.append(self.create_topic(properties))
		# T74
		properties['_key'] = 'T74'
		properties['_type'] = 'cluster'
		properties['title'] = 'Fundamental Physics'
		cluster_topics.append(self.create_topic(properties))
		# T75
		properties['_key'] = 'T75'
		properties['_type'] = 'cluster'
		properties['title'] = 'Materials Science'
		cluster_topics.append(self.create_topic(properties))
		# T76
		properties['_key'] = 'T76'
		properties['_type'] = 'cluster'
		properties['title'] = 'Technology Development and Demonstration'
		cluster_topics.append(self.create_topic(properties))
		# T77
		properties['_key'] = 'T77'
		properties['_type'] = 'cluster'
		properties['title'] = 'Air, Water and Surface Monitoring'
		cluster_topics.append(self.create_topic(properties))
		# T78
		properties['_key'] = 'T78'
		properties['_type'] = 'cluster'
		properties['title'] = 'Avionics and Software'
		cluster_topics.append(self.create_topic(properties))
		# T79
		properties['_key'] = 'T79'
		properties['_type'] = 'cluster'
		properties['title'] = 'Characterizing Experiment Hardware'
		cluster_topics.append(self.create_topic(properties))
		# T80
		properties['_key'] = 'T80'
		properties['_type'] = 'cluster'
		properties['title'] = 'Commercial Demonstrations'
		cluster_topics.append(self.create_topic(properties))
		# T81
		properties['_key'] = 'T81'
		properties['_type'] = 'cluster'
		properties['title'] = 'Communication and Navigation'
		cluster_topics.append(self.create_topic(properties))
		# T82
		properties['_key'] = 'T82'
		properties['_type'] = 'cluster'
		properties['title'] = 'Fire Suppression and Detection'
		cluster_topics.append(self.create_topic(properties))
		# T83
		properties['_key'] = 'T83'
		properties['_type'] = 'cluster'
		properties['title'] = 'Food and Clothing Systems'
		cluster_topics.append(self.create_topic(properties))
		# T84
		properties['_key'] = 'T84'
		properties['_type'] = 'cluster'
		properties['title'] = 'Imaging Technology'
		cluster_topics.append(self.create_topic(properties))
		# T85
		properties['_key'] = 'T85'
		properties['_type'] = 'cluster'
		properties['title'] = 'Life Support Systems and Habitation'
		cluster_topics.append(self.create_topic(properties))
		# T86
		properties['_key'] = 'T86'
		properties['_type'] = 'cluster'
		properties['title'] = 'Microbial Populations in Spacecraft'
		cluster_topics.append(self.create_topic(properties))
		# T87
		properties['_key'] = 'T87'
		properties['_type'] = 'cluster'
		properties['title'] = 'Microgravity Environment Measurement'
		cluster_topics.append(self.create_topic(properties))
		# T88
		properties['_key'] = 'T88'
		properties['_type'] = 'cluster'
		properties['title'] = 'Radiation Measurements and Shielding'
		cluster_topics.append(self.create_topic(properties))
		# T89
		properties['_key'] = 'T89'
		properties['_type'] = 'cluster'
		properties['title'] = 'Repair and Fabrication Technologies'
		cluster_topics.append(self.create_topic(properties))
		# T90
		properties['_key'] = 'T90'
		properties['_type'] = 'cluster'
		properties['title'] = 'Robotics'
		cluster_topics.append(self.create_topic(properties))
		# T91
		properties['_key'] = 'T91'
		properties['_type'] = 'cluster'
		properties['title'] = 'Small Satellites and Control Technologies'
		cluster_topics.append(self.create_topic(properties))
		# T92
		properties['_key'] = 'T92'
		properties['_type'] = 'cluster'
		properties['title'] = 'Space Structures'
		cluster_topics.append(self.create_topic(properties))
		# T93
		properties['_key'] = 'T93'
		properties['_type'] = 'cluster'
		properties['title'] = 'Spacecraft and Orbital Environments'
		cluster_topics.append(self.create_topic(properties))
		# T94
		properties['_key'] = 'T94'
		properties['_type'] = 'cluster'
		properties['title'] = 'Spacecraft Materials'
		cluster_topics.append(self.create_topic(properties))
		# T95
		properties['_key'] = 'T95'
		properties['_type'] = 'cluster'
		properties['title'] = 'Thermal Management Systems'
		cluster_topics.append(self.create_topic(properties))
		# T96
		properties['_key'] = 'T96'
		properties['_type'] = 'cluster'
		properties['title'] = 'Wordnet tag'
		cluster_topics.append(self.create_topic(properties))

		# Create Links
		properties = dict()
		properties['_key'] = ''
		properties['_type'] = ''
		properties['name'] = ''
		properties['definition'] = ''
		properties['_from'] = ''
		properties['_to'] = ''
		# L1
		properties['_key'] = 'L1'
		properties['_type'] = 'encompasses'
		properties['_from'] = 'T1'
		properties['_to'] = 'T2'
		cluster_links.append(self.create_link(properties))
		# L2
		properties['_key'] = 'L2'
		properties['_type'] = 'encompasses'
		properties['_from'] = 'T1'
		properties['_to'] = 'T27'
		cluster_links.append(self.create_link(properties))
		# L3
		properties['_key'] = 'L3'
		properties['_type'] = 'encompasses'
		properties['_from'] = 'T1'
		properties['_to'] = 'T36'
		cluster_links.append(self.create_link(properties))
		# L4
		properties['_key'] = 'L4'
		properties['_type'] = 'encompasses'
		properties['_from'] = 'T1'
		properties['_to'] = 'T21'
		cluster_links.append(self.create_link(properties))
		# L5
		properties['_key'] = 'L5'
		properties['_type'] = 'hasSubclass'
		properties['_from'] = 'T2'
		properties['_to'] = 'T3'
		cluster_links.append(self.create_link(properties))
		# L6
		properties['_key'] = 'L6'
		properties['_type'] = 'hasSubclass'
		properties['_from'] = 'T4'
		properties['_to'] = 'T5'
		cluster_links.append(self.create_link(properties))
		# L7
		properties['_key'] = 'L7'
		properties['_type'] = 'hasSubclass'
		properties['_from'] = 'T4'
		properties['_to'] = 'T6'
		cluster_links.append(self.create_link(properties))
		# L8
		properties['_key'] = 'L8'
		properties['_type'] = 'hasSubclass'
		properties['_from'] = 'T4'
		properties['_to'] = 'T7'
		cluster_links.append(self.create_link(properties))
		# L9
		properties['_key'] = 'L9'
		properties['_type'] = 'hasSubclass'
		properties['_from'] = 'T4'
		properties['_to'] = 'T8'
		cluster_links.append(self.create_link(properties))
		# L9
		properties['_key'] = 'L9'
		properties['_type'] = 'hasSubclass'
		properties['_from'] = 'T4'
		properties['_to'] = 'T9'
		cluster_links.append(self.create_link(properties))
		# L10	
		properties['_key'] = 'L10'
		properties['_type'] = 'hasSubclass'
		properties['_from'] = 'T10'
		properties['_to'] = 'T11'
		cluster_links.append(self.create_link(properties))
		# L11	
		properties['_key'] = 'L11'
		properties['_type'] = 'hasSubclass'
		properties['_from'] = 'T10'
		properties['_to'] = 'T12'
		cluster_links.append(self.create_link(properties))
		# L12	
		properties['_key'] = 'L12'
		properties['_type'] = 'hasSubclass'
		properties['_from'] = 'T10'
		properties['_to'] = 'T13'
		cluster_links.append(self.create_link(properties))
		# L13	
		properties['_key'] = 'L13'
		properties['_type'] = 'hasSubclass'
		properties['_from'] = 'T21'
		properties['_to'] = 'T22'
		cluster_links.append(self.create_link(properties))
		# L14	
		properties['_key'] = 'L14'
		properties['_type'] = 'hasSubclass'
		properties['_from'] = 'T21'
		properties['_to'] = 'T23'
		cluster_links.append(self.create_link(properties))
		# L15	
		properties['_key'] = 'L15'
		properties['_type'] = 'encompasses'
		properties['_from'] = 'T1'
		properties['_to'] = 'T24'
		cluster_links.append(self.create_link(properties))
		# L16	
		properties['_key'] = 'L16'
		properties['_type'] = 'hasSubclass'
		properties['_from'] = 'T24'
		properties['_to'] = 'T25'
		cluster_links.append(self.create_link(properties))
		# L17	
		properties['_key'] = 'L17'
		properties['_type'] = 'hasSubclass'
		properties['_from'] = 'T24'
		properties['_to'] = 'T26'
		cluster_links.append(self.create_link(properties))
		# L19	
		properties['_key'] = 'L19'
		properties['_type'] = 'hasSubclass'
		properties['_from'] = 'T21'
		properties['_to'] = 'T29'
		cluster_links.append(self.create_link(properties))
		# L20	
		properties['_key'] = 'L20'
		properties['_type'] = 'hasSubclass'
		properties['_from'] = 'T21'
		properties['_to'] = 'T30'
		cluster_links.append(self.create_link(properties))
		# L21	
		properties['_key'] = 'L21'
		properties['_type'] = 'hasSubclass'
		properties['_from'] = 'T2'
		properties['_to'] = 'T31'
		cluster_links.append(self.create_link(properties))
		# L22	
		properties['_key'] = 'L22'
		properties['_type'] = 'hasSubclass'
		properties['_from'] = 'T37'
		properties['_to'] = 'T32'
		cluster_links.append(self.create_link(properties))
		# L23	
		properties['_key'] = 'L23'
		properties['_type'] = 'hasSubclass'
		properties['_from'] = 'T37'
		properties['_to'] = 'T33'
		cluster_links.append(self.create_link(properties))
		# L24	
		properties['_key'] = 'L24'
		properties['_type'] = 'hasSubclass'
		properties['_from'] = 'T37'
		properties['_to'] = 'T34'
		cluster_links.append(self.create_link(properties))
		# L25	
		properties['_key'] = 'L25'
		properties['_type'] = 'encompasses'
		properties['_from'] = 'T1'
		properties['_to'] = 'T38'
		cluster_links.append(self.create_link(properties))
		# L26	
		properties['_key'] = 'L26'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T38'
		properties['_to'] = 'T39'
		cluster_links.append(self.create_link(properties))
		# L27	
		properties['_key'] = 'L27'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T38'
		properties['_to'] = 'T48'
		cluster_links.append(self.create_link(properties))
		# L28	
		properties['_key'] = 'L28'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T38'
		properties['_to'] = 'T53'
		cluster_links.append(self.create_link(properties))
		# L29	
		properties['_key'] = 'L29'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T38'
		properties['_to'] = 'T58'
		cluster_links.append(self.create_link(properties))
		# L30	
		properties['_key'] = 'L30'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T38'
		properties['_to'] = 'T70'
		cluster_links.append(self.create_link(properties))
		# L31	
		properties['_key'] = 'L31'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T38'
		properties['_to'] = 'T76'
		cluster_links.append(self.create_link(properties))
		# L32	
		properties['_key'] = 'L32'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T39'
		properties['_to'] = 'T40'
		cluster_links.append(self.create_link(properties))
		# L33	
		properties['_key'] = 'L33'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T39'
		properties['_to'] = 'T41'
		cluster_links.append(self.create_link(properties))
		# L34	
		properties['_key'] = 'L34'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T39'
		properties['_to'] = 'T42'
		cluster_links.append(self.create_link(properties))
		# L35	
		properties['_key'] = 'L35'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T39'
		properties['_to'] = 'T43'
		cluster_links.append(self.create_link(properties))
		# L36	
		properties['_key'] = 'L36'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T39'
		properties['_to'] = 'T44'
		cluster_links.append(self.create_link(properties))
		# L37	
		properties['_key'] = 'L37'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T39'
		properties['_to'] = 'T45'
		cluster_links.append(self.create_link(properties))
		# L38	
		properties['_key'] = 'L38'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T39'
		properties['_to'] = 'T46'
		cluster_links.append(self.create_link(properties))
		# L39	
		properties['_key'] = 'L39'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T39'
		properties['_to'] = 'T47'
		cluster_links.append(self.create_link(properties))
		# L40	
		properties['_key'] = 'L40'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T48'
		properties['_to'] = 'T49'
		cluster_links.append(self.create_link(properties))
		# L41	
		properties['_key'] = 'L41'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T48'
		properties['_to'] = 'T50'
		cluster_links.append(self.create_link(properties))
		# L42	
		properties['_key'] = 'L42'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T48'
		properties['_to'] = 'T51'
		cluster_links.append(self.create_link(properties))
		# L43	
		properties['_key'] = 'L43'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T48'
		properties['_to'] = 'T52'
		cluster_links.append(self.create_link(properties))
		# L44	
		properties['_key'] = 'L44'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T53'
		properties['_to'] = 'T54'
		cluster_links.append(self.create_link(properties))
		# L45	
		properties['_key'] = 'L45'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T53'
		properties['_to'] = 'T55'
		cluster_links.append(self.create_link(properties))
		# L46	
		properties['_key'] = 'L46'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T53'
		properties['_to'] = 'T56'
		cluster_links.append(self.create_link(properties))
		# L47	
		properties['_key'] = 'L47'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T53'
		properties['_to'] = 'T57'
		cluster_links.append(self.create_link(properties))
		# L48	
		properties['_key'] = 'L48'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T58'
		properties['_to'] = 'T59'
		cluster_links.append(self.create_link(properties))
		# L49	
		properties['_key'] = 'L49'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T58'
		properties['_to'] = 'T60'
		cluster_links.append(self.create_link(properties))
		# L50	
		properties['_key'] = 'L50'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T58'
		properties['_to'] = 'T61'
		cluster_links.append(self.create_link(properties))
		# L51	
		properties['_key'] = 'L51'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T58'
		properties['_to'] = 'T62'
		cluster_links.append(self.create_link(properties))
		# L52	
		properties['_key'] = 'L52'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T58'
		properties['_to'] = 'T63'
		cluster_links.append(self.create_link(properties))
		# L53	
		properties['_key'] = 'L53'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T58'
		properties['_to'] = 'T64'
		cluster_links.append(self.create_link(properties))
		# L54	
		properties['_key'] = 'L54'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T58'
		properties['_to'] = 'T65'
		cluster_links.append(self.create_link(properties))
		# L55	
		properties['_key'] = 'L55'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T58'
		properties['_to'] = 'T66'
		cluster_links.append(self.create_link(properties))
		# L56	
		properties['_key'] = 'L56'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T58'
		properties['_to'] = 'T67'
		cluster_links.append(self.create_link(properties))
		# L57	
		properties['_key'] = 'L57'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T58'
		properties['_to'] = 'T68'
		cluster_links.append(self.create_link(properties))
		# L58	
		properties['_key'] = 'L58'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T58'
		properties['_to'] = 'T69'
		cluster_links.append(self.create_link(properties))
		# L59	
		properties['_key'] = 'L59'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T70'
		properties['_to'] = 'T71'
		cluster_links.append(self.create_link(properties))
		# L60	
		properties['_key'] = 'L60'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T70'
		properties['_to'] = 'T72'
		cluster_links.append(self.create_link(properties))
		# L61	
		properties['_key'] = 'L61'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T70'
		properties['_to'] = 'T73'
		cluster_links.append(self.create_link(properties))
		# L62	
		properties['_key'] = 'L62'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T70'
		properties['_to'] = 'T74'
		cluster_links.append(self.create_link(properties))
		# L63	
		properties['_key'] = 'L63'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T70'
		properties['_to'] = 'T75'
		cluster_links.append(self.create_link(properties))
		# L64	
		properties['_key'] = 'L64'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T76'
		properties['_to'] = 'T77'
		cluster_links.append(self.create_link(properties))
		# L65	
		properties['_key'] = 'L65'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T76'
		properties['_to'] = 'T78'
		cluster_links.append(self.create_link(properties))
		# L66	
		properties['_key'] = 'L66'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T76'
		properties['_to'] = 'T79'
		cluster_links.append(self.create_link(properties))
		# L67	
		properties['_key'] = 'L67'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T76'
		properties['_to'] = 'T80'
		cluster_links.append(self.create_link(properties))
		# L68	
		properties['_key'] = 'L68'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T76'
		properties['_to'] = 'T81'
		cluster_links.append(self.create_link(properties))
		# L69	
		properties['_key'] = 'L69'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T76'
		properties['_to'] = 'T82'
		cluster_links.append(self.create_link(properties))
		# L70	
		properties['_key'] = 'L70'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T76'
		properties['_to'] = 'T83'
		cluster_links.append(self.create_link(properties))
		# L71	
		properties['_key'] = 'L71'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T76'
		properties['_to'] = 'T84'
		cluster_links.append(self.create_link(properties))
		# L72	
		properties['_key'] = 'L72'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T76'
		properties['_to'] = 'T85'
		cluster_links.append(self.create_link(properties))
		# L73	
		properties['_key'] = 'L73'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T76'
		properties['_to'] = 'T86'
		cluster_links.append(self.create_link(properties))
		# L74	
		properties['_key'] = 'L74'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T76'
		properties['_to'] = 'T87'
		cluster_links.append(self.create_link(properties))
		# L75	
		properties['_key'] = 'L75'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T76'
		properties['_to'] = 'T88'
		cluster_links.append(self.create_link(properties))
		# L76	
		properties['_key'] = 'L76'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T76'
		properties['_to'] = 'T89'
		cluster_links.append(self.create_link(properties))
		# L77	
		properties['_key'] = 'L77'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T76'
		properties['_to'] = 'T90'
		cluster_links.append(self.create_link(properties))
		# L78	
		properties['_key'] = 'L78'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T76'
		properties['_to'] = 'T91'
		cluster_links.append(self.create_link(properties))
		# L79	
		properties['_key'] = 'L79'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T76'
		properties['_to'] = 'T92'
		cluster_links.append(self.create_link(properties))
		# L80	
		properties['_key'] = 'L80'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T76'
		properties['_to'] = 'T93'
		cluster_links.append(self.create_link(properties))
		# L81	
		properties['_key'] = 'L81'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T76'
		properties['_to'] = 'T94'
		cluster_links.append(self.create_link(properties))
		# L82	
		properties['_key'] = 'L82'
		properties['_type'] = 'categorizes'
		properties['_from'] = 'T76'
		properties['_to'] = 'T95'
		cluster_links.append(self.create_link(properties))
		# L83	
		properties['_key'] = 'L83'
		properties['_type'] = 'hasSubclass'
		properties['_from'] = 'T1'
		properties['_to'] = 'T96'
		cluster_links.append(self.create_link(properties))

		return cluster_topics, cluster_links, len(cluster_topics) + 1, len(cluster_links) + 1
	def create_topic(self, properties):
		topic_json_struct = {}
		for prop, value in properties.items():
			topic_json_struct[prop] = value
		return topic_json_struct
	def create_link(self, properties):
		link_json_struct = {}
		for prop, value in properties.items():
			link_json_struct[prop] = value
		return link_json_struct

class Convert_Researchers():
	def __init__(self):
		print("Protocol B")
	def parse_orcid_id(self, row, authors):
		orcidIDs = dict()
		if (row == ''):
			return orcidIDs
		# First check for /xxxx-xxxx-xxxx-xxxx versus lastName, firstName/xxxx-xxxx-xxxx-xxxx
		if row[0] == '/':
			# In this case, we need the author name. I will assume it is the first, and hopefully only, author
			first_name, last_name = parse_author(authors[0])
			author = form_author_name(first_name, last_name)
			orcid_id = row[1:]
			orcidIDs[author] = orcid_id
		else:
			# If there is more than one, they will be separated by ;.
			if (row.find(';') == -1):
				# Only one orcidId
				reversed_author = parse_author(row[:row.find('/')])
				author = form_author_name(reversed_author[0], reversed_author[1])

				orcid_id = row[row.find('/') + 1:]
				# print(row, author, orcid_id)
				orcidIDs[author] = orcid_id
			else:
				# There are multiple
				elements = row.split(';')
				for element in elements:
					if (element != '' and element.find(',') != -1):
						reversed_author = parse_author(element[:element.find('/')])
						author = form_author_name(reversed_author[0], reversed_author[1])

						orcid_id = element[element.find('/') + 1:]
						orcidIDs[author] = orcid_id

		return orcidIDs

	# Protocol B main function to run
	def convert_researchers(self, data, topic_key_val, link_key_val):
		researcher_topics = list()
		researcher_links = list()

		for rowidx in range(len(data)):
			# Get current row in dataset
			publication_row = data.iloc[rowidx,:]
			# Get the authors using the AF key
			authors = publication_row['AF'].split(";")
			reprint_address_last_name = publication_row['RP'].split(",")[0].title()
			orcidIDs = self.parse_orcid_id(publication_row['OI'], authors)
			for author in authors:
				# Check for incorrectly formatted name - very rare, but has to be done
				if (author.find(',') == -1):
					# Skip if no comma
					continue
				topic_key = 'T' + str(topic_key_val)
				# Increment key value for next topic
				topic_key_val = topic_key_val + 1

				first_name, last_name = parse_author(author)
				initials = first_name[0] + "." + last_name[0] + "."
				terms = [form_author_name(first_name, last_name), last_name, initials]
				title = form_author_name(first_name, last_name)

				if (last_name == reprint_address_last_name):
					email = publication_row['EM']
				else:
					email = ""

				orcid_id = orcidIDs.get(title)
				if (orcid_id == None):
					orcid_id = ''

				# Look for duplicates
				possible_duplicates = []
				duplicate = False
				for topic in researcher_topics:
					if topic['title'] == title:
						# If the orcid IDs match and we can't deduplicate
						if (topic['orcidID'] == orcid_id and orcid_id == ""):
							topic['Possible_Duplicates'].append(topic_key)
							possible_duplicates.append(topic['_key'])
						elif (topic['orcidID'] == orcid_id and orcid_id != ""):
							# This is a duplicate based on orcid id - we don't need to store it
							duplicate = True
				# Skip making a topic for this author
				if (duplicate):
					continue

				# Output topic to JSON format
				topic_json_struct = {}
				topic_json_struct['_key'] = topic_key
				topic_json_struct["_type"] = "individual"
				topic_json_struct['title'] = title
				topic_json_struct['terms'] = terms
				topic_json_struct['definition'] = ''
				topic_json_struct['sources'] = "Web of Science, row " + str(rowidx + 2)
				topic_json_struct['firstName'] = first_name
				topic_json_struct['lastName'] = last_name
				topic_json_struct['initials'] = initials
				topic_json_struct['email'] = email
				topic_json_struct['orcidID'] = orcid_id
				topic_json_struct['Possible_Duplicates'] = possible_duplicates

				# Store in list to output at end
				researcher_topics.append(topic_json_struct)

				link_key = 'L' + str(link_key_val)
				# Increment key value for next link
				link_key_val = link_key_val + 1

				# Output link to JSON format
				link_json_struct = {}
				link_json_struct['_key'] = link_key
				link_json_struct['_type'] = 'hasInstance'
				link_json_struct['name'] = ''
				link_json_struct['definition'] = ''
				link_json_struct['_from'] = 'T3'
				link_json_struct['_to'] = topic_key

				# Store in list to output at end
				researcher_links.append(link_json_struct)
		return researcher_topics, researcher_links, topic_key_val, link_key_val

class Convert_Publications():
	def __init__(self):
		print("Protocol C")
	# Protocol C main function to run
	def convert_publications(self, data, topic_key_val, link_key_val):
		publication_topics = list()
		publication_links = list()

		for rowidx in range(len(data)):
			# Get current row in dataset
			publication_row = data.iloc[rowidx,:]
			issn = publication_row['SN']
			electronic_issn = publication_row['EI']
			isbn = publication_row['BN']
			# Determine which columns to read based off value of ISBN
			if (isbn == ""):
				topic_title = publication_row['SO'].title()
				terms = [topic_title, publication_row['J9'].title(), publication_row['JI'].title()]
				conference_proceeding = False
				_type = "journal"
			else:
				topic_title = publication_row['SE'].title()
				terms = [topic_title, publication_row['J9'].title()]
				conference_proceeding = True
				_type = "journal"

			# Look for duplicates
			duplicate = False
			for topic in publication_topics:
				if topic['title'] == topic_title:
					# If the ISSN or ISBN match, assuming there is data, then this is a duplicate
					if (topic['ISBN'] == isbn and isbn != "") or (topic['ISSN'] == issn and issn != ""):
						topic['sources'] = topic['sources'] + ', row ' + str(rowidx + 2)
						duplicate = True
					# No data for issn/isbn but electronic issn matches
					elif (isbn == '' and issn == '' and topic['Electronic_ISSN'] == electronic_issn):
						topic['sources'] = topic['sources'] + ', row ' + str(rowidx + 2)
						duplicate = True
			# Skip making a topic for this publication
			if (duplicate):
				continue

			topic_key = 'T' + str(topic_key_val)
			# Increment key value for next topic
			topic_key_val = topic_key_val + 1

			# Output topic to JSON format
			topic_json_struct = {}
			topic_json_struct['_key'] = topic_key
			topic_json_struct["_type"] = _type
			topic_json_struct['title'] = topic_title
			topic_json_struct['terms'] = terms
			topic_json_struct['sources'] = "Web of Science, row " + str(rowidx + 2)
			topic_json_struct['ISSN'] = issn
			topic_json_struct['Electronic_ISSN'] = electronic_issn
			topic_json_struct['ISBN'] = isbn

			# Store in list to output at end
			publication_topics.append(topic_json_struct)

			link_key = 'L' + str(link_key_val)
			# Increment key value for next link
			link_key_val = link_key_val + 1

			# Output link to JSON format
			link_json_struct = {}
			link_json_struct['_key'] = link_key
			link_json_struct['_type'] = 'hasSubclass'
			link_json_struct['name'] = ''
			link_json_struct['definition'] = ''
			link_json_struct['_from'] = 'T12' if conference_proceeding else 'T11' 
			link_json_struct['_to'] = topic_key

			# Store in list to output at end
			publication_links.append(link_json_struct)
		return publication_topics, publication_links, topic_key_val, link_key_val

class Convert_Journals():
	def __init__(self):
		print("Protocol D")
	def parse_month_published(self, content):
		if (content == ""):
			return ""
		# Could be 26-Sep, OCT, SEP-OCT
		content = content.upper()
		if ('-' in content):
			content = content[content.find('-')+1:]
		if content == "JAN":
			return "01"
		elif content == "FEB":
			return "02"
		elif content == "MAR":
			return "03"
		elif content == "APR":
			return "04"
		elif content == "MAY":
			return "05"
		elif content == "JUN":
			return "06"
		elif content == "JUL":
			return "07"
		elif content == "AUG":
			return "08"
		elif content == "SEP":
			return "09"
		elif content == "OCT":
			return "10"
		elif content == "NOV":
			return "11"
		else:
			return "12"
	def determine_property_access_link_value(self, content):
		if content == '':
			return ["Traditional Publishing"]
		else:
			if "," in content:
				output = []
				strs = content.split(",")
				for element in strs:
					output.append(element.strip() + " Open Access")
				return output
			else:
				return [content + " Open Access"]

	# Protocol D main function to run
	def convert_journals(self, data, topic_key_val, link_key_val, publication_topics):
		journal_topics = list()
		journal_links = list()
		
		# This dict will tell us if links are already going to be created. Keyed by (from, to), value doesn't matter
		duplicated_links_dict = dict()

		for rowidx in range(len(data)):
			# Get current row in dataset
			publication_row = data.iloc[rowidx,:]

			# Find corresponding topic in publication_topics
			my_row = "row " + str(rowidx + 2) + ','
			my_row2 = "row " + str(rowidx + 2)
			temporary_topic_struct = {}
			for topic in publication_topics:
				if my_row in topic['sources'] or topic['sources'].endswith(my_row2):
					temporary_topic_struct = topic
					break

			month_published = self.parse_month_published(publication_row['PD'])
			year_published = str(publication_row['PY'])
			volume = str(publication_row['VL'])
			issue = str(publication_row['IS'])
			part = str(publication_row['PN'])

			# Determine title for this journal instance
			topic_title = 'Volume '
			if volume == '':
				topic_title = topic_title + year_published
			else:
				topic_title = topic_title + volume

			if issue != '':
				topic_title = topic_title + ', Issue ' + issue
			if part != '':
				topic_title = topic_title + ', Part ' + part

			if month_published != '':
				topic_title = topic_title + ', ' + month_published + '-' + year_published + ' - ' + temporary_topic_struct['title']
			else:
				topic_title = topic_title + ', ' + year_published + ' - ' + temporary_topic_struct['title']
			# Terms is just the topic title
			terms = [topic_title]

			# Look for duplicates
			duplicate = False
			for topic in journal_topics:
				if topic['title'] == topic_title:
					topic['sources'] = topic['sources'] + ', row ' + str(rowidx + 2)
					duplicate = True
			# Skip making a topic for this publication
			if (duplicate):
				continue

			topic_key = 'T' + str(topic_key_val)
			# Increment key value for next topic
			topic_key_val = topic_key_val + 1

			# Output topic to JSON format
			topic_json_struct = {}
			topic_json_struct['_key'] = topic_key
			topic_json_struct["_type"] = 'publication'
			topic_json_struct['title'] = topic_title
			topic_json_struct['terms'] = terms
			topic_json_struct['sources'] = "Web of Science, row " + str(rowidx + 2)
			topic_json_struct['month published'] = month_published
			topic_json_struct['year published'] = year_published
			topic_json_struct['volume'] = volume
			topic_json_struct['issue'] = issue
			topic_json_struct['part'] = part
			topic_json_struct['ISSN'] = temporary_topic_struct['ISSN']
			topic_json_struct['Electronic_ISSN'] = temporary_topic_struct['Electronic_ISSN']
			topic_json_struct['ISBN'] = temporary_topic_struct['ISBN']
			# Store in list to output at end
			journal_topics.append(topic_json_struct)

			# (1) Link from journal to instance
			link_key = 'L' + str(link_key_val)
			# Increment key value for next link
			link_key_val = link_key_val + 1
			# Output link to JSON format
			link_json_struct = {}
			link_json_struct['_key'] = link_key
			link_json_struct['_type'] = 'hasInstance'
			link_json_struct['name'] = ''
			link_json_struct['definition'] = ''
			link_json_struct['_from'] = temporary_topic_struct['_key'] 
			link_json_struct['_to'] = topic_key
			# Store in list to output at end
			journal_links.append(link_json_struct)

			# (2) Link to property access type
			access_values = self.determine_property_access_link_value(publication_row['OA'])
			for value in access_values:
				link_key = 'L' + str(link_key_val)
				# Increment key value for next link
				link_key_val = link_key_val + 1
				# Output link to JSON format
				link_json_struct = {}
				link_json_struct['_key'] = link_key
				link_json_struct['_type'] = 'has'
				link_json_struct['name'] = ''
				link_json_struct['definition'] = ''
				link_json_struct['_from'] = temporary_topic_struct['_key'] 
				link_json_struct['_to'] = "T14"
				link_json_struct['value'] = value
				# Store in list to output at end if link does not already exit
				if (duplicated_links_dict.get((temporary_topic_struct['_key'], "T14")) == None):
					journal_links.append(link_json_struct)
			# This can only be marked at the end of the first run, otherwise there will only be one link, when actually we want 'duplicate links' with different values
			duplicated_links_dict[(temporary_topic_struct['_key'], "T14")] = 1


			# (3) Link to property publication type
			link_key = 'L' + str(link_key_val)
			# Increment key value for next link
			link_key_val = link_key_val + 1

			value = ''
			if publication_row['PT'] == 'J':
				value = "Journal"
			elif publication_row['PT'] == 'S':
				value = "Series"
			elif publication_row['PT'] == 'P':
				value = 'Patent'
			elif publication_row['PT'] == 'B':
				value = 'Book'
			# Output link to JSON format
			link_json_struct = {}
			link_json_struct['_key'] = link_key
			link_json_struct['_type'] = 'has'
			link_json_struct['name'] = ''
			link_json_struct['definition'] = ''
			link_json_struct['_from'] = temporary_topic_struct['_key'] 
			link_json_struct['_to'] = "T16"
			link_json_struct['value'] = value
			# Store in list to output at end if link does not already exit
			if (duplicated_links_dict.get((temporary_topic_struct['_key'], "T16")) == None):
				journal_links.append(link_json_struct)
				duplicated_links_dict[(temporary_topic_struct['_key'], "T16")] = 1

			# (4) Link to property Language
			link_key = 'L' + str(link_key_val)
			# Increment key value for next link
			link_key_val = link_key_val + 1

			# Output link to JSON format
			link_json_struct = {}
			link_json_struct['_key'] = link_key
			link_json_struct['_type'] = 'has'
			link_json_struct['name'] = ''
			link_json_struct['definition'] = ''
			link_json_struct['_from'] = temporary_topic_struct['_key'] 
			link_json_struct['_to'] = "T17"
			link_json_struct['value'] = publication_row['LA']
			# Store in list to output at end if link does not already exit
			if (duplicated_links_dict.get((temporary_topic_struct['_key'], "T17")) == None):
				journal_links.append(link_json_struct)
				duplicated_links_dict[(temporary_topic_struct['_key'], "T17")] = 1

			# (5) Link to property published date
			link_key = 'L' + str(link_key_val)
			# Increment key value for next link
			link_key_val = link_key_val + 1

			value = ''
			if month_published != '' and year_published != '':
				value = month_published + '-' + year_published
			elif month_published == '' and year_published != '':
				value = year_published
			elif month_published != '' and year_published == '':
				value = month_published

			# Output link to JSON format
			link_json_struct = {}
			link_json_struct['_key'] = link_key
			link_json_struct['_type'] = 'has'
			link_json_struct['name'] = ''
			link_json_struct['definition'] = ''
			link_json_struct['_from'] = temporary_topic_struct['_key'] 
			link_json_struct['_to'] = "T18"
			link_json_struct['value'] = value
			if (duplicated_links_dict.get((temporary_topic_struct['_key'], "T18")) == None):
				journal_links.append(link_json_struct)
				duplicated_links_dict[(temporary_topic_struct['_key'], "T18")] = 1
		return journal_topics, journal_links, topic_key_val, link_key_val

class Convert_Articles():
	def __init__(self):
		print("Protocol E")
	# Protocol E main function to run
	def convert_articles(self, data, topic_key_val, link_key_val, researcher_topics, publication_topics, journal_topics, journal_links):
		article_topics = list()
		article_links = list()

		# For later use, I will convert all the researcher names to a dict mapping name to key
		researchers_name_to_key = dict()
		for topic in researcher_topics:
			researchers_name_to_key[topic['title']] = topic['_key']

		for rowidx in range(len(data)):
			# Get current row in dataset
			publication_row = data.iloc[rowidx,:]

			topic_title = publication_row['TI']
			terms = [topic_title]
			definition = publication_row['AB']
			acknowledgement = publication_row['FX']
			b_page = str(publication_row['BP'])
			e_page = str(publication_row['EP'])
			doi = str(publication_row['DI'])
			articleID = publication_row['AR']
			woSID = publication_row['UT']
			pubMedID = publication_row['PM']
			date_downloaded = publication_row['DA']
			grants = publication_row['FU']
			cited_reference = [x.strip() for x in publication_row['CR'].split(';')]

			# Look for duplicates
			duplicate = False
			for topic in article_topics:
				if topic['title'] == topic_title:
					topic['sources'] = topic['sources'] + ', row ' + str(rowidx + 2)
					duplicate = True
			# Skip making a topic for this article. There is one duplicate, so to simplify the logic, we will just say that line in the dataset does not provide any additional information
			if (duplicate):
				continue

			# Find corresponding created topic in journal_topics
			my_row = "row " + str(rowidx + 2) + ','
			my_row2 = "row " + str(rowidx + 2)
			temporary_journal_topic_struct = {}
			for topic in journal_topics:
				if my_row in topic['sources'] or topic['sources'].endswith(my_row2):
					temporary_journal_topic_struct = topic
					break

			# Find corresponding created topic in publication_topics
			temporary_publication_topic_struct = {}
			for topic in publication_topics:
				if my_row in topic['sources'] or topic['sources'].endswith(my_row2):
					temporary_publication_topic_struct = topic
					break
			# Inherit certain properties from this topic
			journal_key = temporary_journal_topic_struct['_key']
			issn = temporary_journal_topic_struct['ISSN']
			electronic_issn = temporary_journal_topic_struct['Electronic_ISSN']
			isbn = temporary_journal_topic_struct['ISBN']
			month_published = temporary_journal_topic_struct['month published']
			year_published = temporary_journal_topic_struct['year published']
			volume = temporary_journal_topic_struct['volume']
			issue = temporary_journal_topic_struct['issue']
			part = temporary_journal_topic_struct['part']
			journal = temporary_publication_topic_struct['title']

			topic_key = 'T' + str(topic_key_val)
			# Increment key value for next topic
			topic_key_val = topic_key_val + 1

			# Output topic to JSON format
			topic_json_struct = {}
			topic_json_struct['_key'] = topic_key
			topic_json_struct["_type"] = "publication"
			topic_json_struct['title'] = topic_title
			topic_json_struct['terms'] = terms
			topic_json_struct['definition'] = definition
			topic_json_struct['sources'] = "Web of Science, row " + str(rowidx + 2)
			topic_json_struct['ISSN'] = issn
			topic_json_struct['Electronic_ISSN'] = electronic_issn
			topic_json_struct['ISBN'] = isbn
			topic_json_struct['month published'] = month_published
			topic_json_struct['year published'] = year_published
			topic_json_struct['volume'] = volume
			topic_json_struct['issue'] = issue
			topic_json_struct['part'] = part
			topic_json_struct['acknowledgement'] = acknowledgement
			topic_json_struct['beginning page'] = b_page
			topic_json_struct['ending page'] = e_page
			topic_json_struct['DOI'] = doi
			topic_json_struct['ArticleID'] = articleID
			topic_json_struct['WoSID'] = woSID
			topic_json_struct['PubMedID'] = pubMedID
			topic_json_struct['date downloaded'] = date_downloaded
			topic_json_struct['grants'] = grants
			topic_json_struct['cited reference'] = cited_reference
			topic_json_struct['journal'] = journal

			# Store in list to output at end
			article_topics.append(topic_json_struct)

			# (1) Create links between cluster - topic
			link_key = 'L' + str(link_key_val)
			# Increment key value for next link
			link_key_val = link_key_val + 1
			# Output link to JSON format
			link_json_struct = {}
			link_json_struct['_key'] = link_key
			link_json_struct['_type'] = 'hasInstance'
			link_json_struct['name'] = ''
			link_json_struct['definition'] = ''
			link_json_struct['_from'] = 'T13'
			link_json_struct['_to'] = topic_key
			# Store in list to output at end
			article_links.append(link_json_struct)

			# (2) Create link between journal instances and article
			link_key = 'L' + str(link_key_val)
			# Increment key value for next link
			link_key_val = link_key_val + 1
			# Output link to JSON format
			link_json_struct = {}
			link_json_struct['_key'] = link_key
			link_json_struct['_type'] = 'link'
			link_json_struct['name'] = 'contains_01'
			link_json_struct['definition'] = ''
			link_json_struct['_from'] = journal_key
			link_json_struct['_to'] = topic_key
			# Store in list to output at end
			article_links.append(link_json_struct)
			# (3) Create links between researcher and article
			authors = publication_row['AF'].split(";")
			# Determine who reprint author is
			reprint = publication_row['RP']
			loc = reprint.find('(reprint author)') + 18
			flipped_name = reprint[:loc - 19]
			reprint_last_name = flipped_name[:flipped_name.find(',')].title()

			researcher_key = None
			for author in authors:
				# Check for incorrectly formatted name - very rare, but has to be done
				if (author.find(',') == -1):
					# Skip if no comma
					continue
				first, last = parse_author(author)
				researcher_key = researchers_name_to_key.get(form_author_name(first, last))
				# This is possible and is due to different spellings of the name. 
				if researcher_key == None:
					pass
				else:
					link_key = 'L' + str(link_key_val)
					# Increment key value for next link
					link_key_val = link_key_val + 1
					# Output link to JSON format
					link_json_struct = {}
					link_json_struct['_key'] = link_key
					link_json_struct['_type'] = 'link'
					link_json_struct['name'] = 'authors'
					link_json_struct['definition'] = ''
					link_json_struct['_from'] =  researcher_key
					link_json_struct['_to'] = topic_key
					# Add to list
					article_links.append(link_json_struct)

					# Reprint author link
					if reprint_last_name == last:
						link_key = 'L' + str(link_key_val)
						# Increment key value for next link
						link_key_val = link_key_val + 1
						# Output link to JSON format
						link_json_struct = {}
						link_json_struct['_key'] = link_key
						link_json_struct['_type'] = 'link'
						link_json_struct['name'] = 'reprint'
						link_json_struct['definition'] = ''
						link_json_struct['_from'] =  researcher_key
						link_json_struct['_to'] = topic_key
						# Add to list
						article_links.append(link_json_struct)

			# (5) Link to download date
			link_key = 'L' + str(link_key_val)
			# Increment key value for next link
			link_key_val = link_key_val + 1
			# Output link to JSON format
			link_json_struct = {}
			link_json_struct['_key'] = link_key
			link_json_struct['_type'] = 'has'
			link_json_struct['name'] = ''
			link_json_struct['definition'] = ''
			link_json_struct['_from'] = topic_key
			link_json_struct['_to'] = 'T15'
			link_json_struct['value'] = date_downloaded
			# Store in list to output at end
			article_links.append(link_json_struct)

			# (4, 6, 7) Link to property access type, language, published date,
			# First find the corresponding journal from this journal instance
			j_key = ''
			for link in journal_links:
				if link['_to'] == journal_key:
					j_key = link['_from']

			# Now get the values for the specific properties using the original journal's key
			access_types = []
			language = ''
			published_date = ''
			for link in journal_links:
				if link['_from'] == j_key and j_key != journal_key:
					if link['_to'] == 'T14':
						access_types.append(link['value'])
					elif link['_to'] == 'T17':
						language = link['value']
					elif link['_to'] == 'T18':
						published_date = link['value']

			# Link for each access type
			for access_type in access_types:
				link_key = 'L' + str(link_key_val)
				# Increment key value for next link
				link_key_val = link_key_val + 1
				# Output link to JSON format
				link_json_struct = {}
				link_json_struct['_key'] = link_key
				link_json_struct['_type'] = 'has'
				link_json_struct['name'] = ''
				link_json_struct['definition'] = ''
				link_json_struct['_from'] = topic_key
				link_json_struct['_to'] = 'T14'
				link_json_struct['value'] = access_type
				# Store in list to output at end
				article_links.append(link_json_struct)
			# (6) Link for language
			link_key = 'L' + str(link_key_val)
			# Increment key value for next link
			link_key_val = link_key_val + 1
			# Output link to JSON format
			link_json_struct = {}
			link_json_struct['_key'] = link_key
			link_json_struct['_type'] = 'has'
			link_json_struct['name'] = ''
			link_json_struct['definition'] = ''
			link_json_struct['_from'] = topic_key
			link_json_struct['_to'] = 'T17'
			link_json_struct['value'] = language
			# Store in list to output at end
			article_links.append(link_json_struct)		

			# (7) Link to published date
			link_key = 'L' + str(link_key_val)
			# Increment key value for next link
			link_key_val = link_key_val + 1
			# Output link to JSON format
			link_json_struct = {}
			link_json_struct['_key'] = link_key
			link_json_struct['_type'] = 'has'
			link_json_struct['name'] = ''
			link_json_struct['definition'] = ''
			link_json_struct['_from'] = topic_key
			link_json_struct['_to'] = 'T18'
			link_json_struct['value'] = published_date
			# Store in list to output at end
			article_links.append(link_json_struct)

			# (8) Link to property document type
			doc_types = []
			# There are multiple document types
			if publication_row['DT'].find(';') != -1:
				doc_types = publication_row['DT'].split(';')
			else:
				doc_types = [publication_row['DT']]
			for doc_type in doc_types:
				doc_type = doc_type.strip()

				link_key = 'L' + str(link_key_val)
				# Increment key value for next link
				link_key_val = link_key_val + 1
				# Output link to JSON format
				link_json_struct = {}
				link_json_struct['_key'] = link_key
				link_json_struct['_type'] = 'has'
				link_json_struct['name'] = ''
				link_json_struct['definition'] = ''
				link_json_struct['_from'] = topic_key
				link_json_struct['_to'] = 'T19'
				link_json_struct['value'] = doc_type
				# Store in list to output at end
				article_links.append(link_json_struct)

		return article_topics, article_links, topic_key_val, link_key_val

class Convert_Events():
	def __init__(self):
		print("Protocol F")
	def parse_conference_year(self, date):
		# Format is either MONTH DATE-RANGE, YEAR
		# or format is DAY-MONTH-2_DIGIT_YEAR
		# or format is just YEAR
		if "," in date: # Case 1
			year = str(date[date.find(',') + 2:])
		else:
			if '-' in date: # Case 2
				year = '20' + str(date[date.find('-',3) + 1:])
			else: # Case 3
				year = str(date)
		return year
	# Protocol F main function to run
	def convert_events(self, data, topic_key_val, link_key_val, article_topics):
		event_topics = list()
		event_links = list()

		for rowidx in range(len(data)):
			# Get current row in dataset
			publication_row = data.iloc[rowidx,:]
			# Ensure value for CT
			if (publication_row['CT'] == ''):
				continue

			_type = "topic"
			topic_title = publication_row['CT']
			terms = [topic_title]
			definition = "The " + topic_title + " was hosted on " + publication_row['CY'] + " at " + publication_row['CL'] + '.'
			if (publication_row['SP'] != ""):
				definition = definition + " This event was sponsored by " + publication_row['SP'] + '.'

			# Look for duplicates
			duplicate = False
			topic_key = ''
			for topic in event_topics:
				if topic['title'] == topic_title:
					topic['sources'] = topic['sources'] + ', row ' + str(rowidx + 2)
					duplicate = True
					topic_key = topic['_key']
			# Only make topic if not a duplicate
			if (not duplicate):
				topic_key = 'T' + str(topic_key_val)
				# Increment key value for next topic
				topic_key_val = topic_key_val + 1

				# Output topic to JSON format
				topic_json_struct = {}
				topic_json_struct['_key'] = topic_key
				topic_json_struct["_type"] = _type
				topic_json_struct['title'] = topic_title
				topic_json_struct['terms'] = terms
				topic_json_struct['definition'] = definition
				topic_json_struct['sources'] = "Web of Science, row " + str(rowidx + 2)

				# Store in list to output at end
				event_topics.append(topic_json_struct)

				# (1) Link the events to their corresponding cluster
				# Determine the cluster
				standard_case_topic_title = topic_title.title()
				if 'Conference' in standard_case_topic_title:
					_from = 'T5'
				elif 'Workshop' in standard_case_topic_title:
					_from = 'T6'
				elif 'Symposium' in standard_case_topic_title:
					_from = 'T7'
				elif 'Congress' in standard_case_topic_title:
					_from = 'T8'
				else: 
					# It is a 'Meeting' or one of the following conferences that did not receive a classification
					# Default for 5th Interdisciplinary Transport Phenomena - Fluid, Thermal, Biological, Materials and Space Sciences
					# Default for 35th COSPAR Scientific Assembly
					_from = 'T9'
				link_key = 'L' + str(link_key_val)
				# Increment key value for next link
				link_key_val = link_key_val + 1

				# Output link to JSON format
				link_json_struct = {}
				link_json_struct['_key'] = link_key
				link_json_struct['_type'] = 'hasInstance'
				link_json_struct['name'] = ''
				link_json_struct['definition'] = ''
				link_json_struct['_from'] = _from 
				link_json_struct['_to'] = topic_key

				# Store in list to output at end
				event_links.append(link_json_struct)

				# (2) Link the events to the conference year property
				year = self.parse_conference_year(publication_row['CY'])
				link_key = 'L' + str(link_key_val)
				# Increment key value for next link
				link_key_val = link_key_val + 1

				# Output link to JSON format
				link_json_struct = {}
				link_json_struct['_key'] = link_key
				link_json_struct['_type'] = 'has'
				link_json_struct['name'] = ''
				link_json_struct['definition'] = ''
				link_json_struct['_from'] = topic_key 
				link_json_struct['_to'] = 'T20'
				link_json_struct['value'] = str(year)

				# Store in list to output at end
				event_links.append(link_json_struct)

			# (3) Link the events to the articles. We still want to link the article even if the event already exists. For example, the 18th Humans in Space (HIS) Symposium of the International-Academy-of-Astronautics (IAA) should only be created once but have multiple links to various articles
			# Since articles are unique, we don't need to worry about duplicate links
			# Find corresponding topic in article_topics
			my_row = "row " + str(rowidx + 2) + ','
			my_row2 = "row " + str(rowidx + 2)
			temporary_topic_struct = {}
			for topic in article_topics:
				if my_row in topic['sources'] or topic['sources'].endswith(my_row2):
					temporary_topic_struct = topic
					break
			article_key = temporary_topic_struct['_key']

			link_key = 'L' + str(link_key_val)
			# Increment key value for next link
			link_key_val = link_key_val + 1

			# Output link to JSON format
			link_json_struct = {}
			link_json_struct['_key'] = link_key
			link_json_struct['_type'] = 'link'
			link_json_struct['name'] = 'presents'
			link_json_struct['definition'] = ''
			link_json_struct['_from'] = topic_key 
			link_json_struct['_to'] = article_key

			# Store in list to output at end
			event_links.append(link_json_struct)

		return event_topics, event_links, topic_key_val, link_key_val

class Convert_Organizations():
	def __init__(self):
		print("Protocol G")
	def post_process_organizations(self, organization_topics):
		terms = dict()
		terms['Univ'] = 'University'
		terms['Amer'] = 'American'
		terms['Assoc'] = 'Association'
		terms['Soc'] = 'Society'
		terms['Int'] = 'International'
		terms['Inst'] = 'Institute'
		terms['Acad'] = 'Academy'
		terms['Sci'] = 'Science'
		terms['Appl'] = 'Applied'
		terms['Natl'] = 'National'
		terms['Extraterr'] = 'Extraterrestrial'
		terms['Mech'] = 'Mechanics'
		terms['Calif'] = 'California'
		terms['Technol'] = 'Technology'
		terms['Ctr'] = 'Center'
		terms['Nucl'] = 'Nuclear'
		terms['Explorat'] = 'Exploration'
		terms['Agcy'] = 'Agency'
		terms['Mol'] = 'Molecular'
		terms['Physiol'] = 'Physiology'
		terms['Hlth'] = 'Health'
		terms['Fdn'] = 'Foundation'
		terms['Hosp'] = 'Hospital'
		terms['Sch'] = 'School'
		terms['Res'] = 'Research'
		terms['Math'] = 'Mathematics'
		terms['Aeron'] = 'Aeronomy'
		terms['Genet'] = 'Genetics'
		terms['Select'] = 'Selection'
		terms['Ind'] = 'Industrial'
		terms['Grp'] = 'Group'
		terms['Engn'] = 'Engineering'
		terms['Atmospher'] = 'Atmospheric'
		terms['Pharmaceut'] = 'Pharmaceutical'
		terms['Coll'] = 'College'
		terms['Lab'] = 'Laboratory'
		terms['Biochem'] = 'Biochemistry'
		terms['Hop'] = 'Hopital'
		terms['Fac'] = 'Faculty'
		terms['Prop'] = 'Propulsion'
		terms['Nutr'] = 'Nutritional'
		terms['Dept'] = 'Department'
		terms['Federat'] = 'Federation'
		terms['Promot'] = 'Promotion'
		terms['Informat'] = 'Information'
		terms['Commun'] = 'Communication'
		terms['Ecol'] = 'Ecology'
		terms['Techn'] = 'Techniques'
		terms['Solut'] = 'Solutions'
		terms['Adm'] = 'Administration'
		terms['Vet'] = 'Veterans'
		terms['Tech'] = 'Technology'
		terms['Radiol'] = 'Radiological'
		terms['Environm'] = 'Environmental'
		terms['Syst'] = 'Systems'
		terms['Off'] = 'Office'
		terms['Rech'] = 'Recherches'
		terms['Meteorol'] = 'Meteorological'
		terms['Minist'] = 'Ministry'
		terms['Canc'] = 'Cancer'
		terms['Biosci'] = 'Bioscience'
		terms['Bldg'] = 'Building'
		terms['Cent'] = 'Central'
		terms['Surg'] = 'Surgery'
		terms['Operat'] = 'Operations'
		terms['Adv'] = 'Advanced'
		terms['So'] = 'Southern'
		terms['S'] = 'Southern'
		terms['Infect'] = 'Infection'
		terms['Biol'] = 'Biology'
		terms['Dynam'] = 'Dynamics'
		terms['Corp'] = 'Corportation'
		terms['Gen'] = 'General'
		terms['Utilizat'] = 'Utilization'
		terms['Promot'] = 'Promotion'
		terms['Isl'] = 'Island'	

		for topic in organization_topics:
			topic_title = topic['title']
			words_in_title = topic_title.split(" ")
			temp_topic_title = ""
			for index, word in enumerate(words_in_title):
				if index == 0 and word == 'Univ':
					word = 'University of'
				else:
					word = terms.get(word) or word
				temp_topic_title = temp_topic_title + " " + word
			topic['title'] = temp_topic_title.strip()
		return organization_topics

	# Protocol G main function to run
	def convert_organizations(self, data, topic_key_val, link_key_val, researcher_topics, publication_topics):
		organization_topics = list()
		organization_links = list()
		
		# This dict will tell us if links are already going to be created. Keyed by (from, to), value doesn't matter
		duplicated_links_dict = dict()
		# For later use, I will convert all the researcher names to a dict mapping name to key
		researchers_name_to_key = dict()
		for topic in researcher_topics:
			researchers_name_to_key[topic['title']] = topic['_key']

		# G1
		for rowidx in range(len(data)):
			# Get current row in dataset
			publication_row = data.iloc[rowidx,:]
			# Set properties
			_type = "topic"
			topic_title = publication_row['PU'].title()
			definition = topic_title + " has address " + publication_row['PA'].title()

			# Find corresponding topic in publication_topics
			my_row = "row " + str(rowidx + 2) + ','
			my_row2 = "row " + str(rowidx + 2)
			temporary_topic_struct = {}
			for topic in publication_topics:
				if my_row in topic['sources'] or topic['sources'].endswith(my_row2):
					temporary_topic_struct = topic
					break

			# Look for duplicates
			duplicate = False
			topic_key = ''
			for topic in organization_topics:
				if topic['title'] == topic_title:
					topic['sources'] = topic['sources'] + ', row ' + str(rowidx + 2)
					duplicate = True
					topic_key = topic['_key']
			# Only make a topic for this publisher if it is not a duplicate. In that case, we have to link to the publishers cluster.
			# We have to link to the journal regardless as long as that specific link is not a duplicate. A publisher could have multiple journals, so a row in the dataset could have an already created publisher with a new journal we have not seen yet
			if (not duplicate):
				topic_key = 'T' + str(topic_key_val)
				# Increment key value for next topic
				topic_key_val = topic_key_val + 1

				# Output topic to JSON format
				topic_json_struct = {}
				topic_json_struct['_key'] = topic_key
				topic_json_struct["_type"] = _type
				topic_json_struct['title'] = topic_title
				topic_json_struct['definition'] = definition
				topic_json_struct['sources'] = "Web of Science, row " + str(rowidx + 2)

				# Store in list to output at end
				organization_topics.append(topic_json_struct)

				# (1) Link from publishers cluster to publisher
				link_key = 'L' + str(link_key_val)
				# Increment key value for next link
				link_key_val = link_key_val + 1
				# Output link to JSON format
				link_json_struct = {}
				link_json_struct['_key'] = link_key
				link_json_struct['_type'] = 'hasInstance'
				link_json_struct['name'] = ''
				link_json_struct['definition'] = ''
				link_json_struct['_from'] = 'T23' 
				link_json_struct['_to'] = topic_key
				# Store in list to output at end
				organization_links.append(link_json_struct)

			# (2) Link publisher to journal
			link_key = 'L' + str(link_key_val)
			# Increment key value for next link
			link_key_val = link_key_val + 1

			# Output link to JSON format
			link_json_struct = {}
			link_json_struct['_key'] = link_key
			link_json_struct['_type'] = 'link'
			link_json_struct['name'] = 'publishes'
			link_json_struct['definition'] = ''
			link_json_struct['_from'] =  topic_key
			link_json_struct['_to'] = temporary_topic_struct['_key']
			# Store in list to output at end if link does not already exit
			if (duplicated_links_dict.get((topic_key, temporary_topic_struct['_key'])) == None):
				organization_links.append(link_json_struct)
				duplicated_links_dict[(topic_key, temporary_topic_struct['_key'])] = 1
		# G2
		for rowidx in range(len(data)):
			# Get current row in dataset
			publication_row = data.iloc[rowidx,:]
			if (publication_row['RP'] != ""):
				_type = "topic"
				reprint = publication_row['RP']
				loc = reprint.find('(reprint author)') + 18
				topic_title = reprint[loc: reprint.find(',', loc)].title()
				terms = [topic_title]
				definition = reprint[loc: reprint.find('.', loc) + 1]

				# Look for duplicates
				duplicate = False
				topic_key = ''
				for topic in organization_topics:
					if topic['title'] == topic_title:
						topic['sources'] = topic['sources'] + ', row ' + str(rowidx + 2)
						duplicate = True
						topic_key = topic['_key']
				# Only make a topic for this publisher if it is not a duplicate. In that case, we have to link to the research organizations cluster. 
				# However, linking research organizations to the researcher needs to be done regardless rows refering to the the same research organization may have different researchers
				if (not duplicate):
					topic_key = 'T' + str(topic_key_val)
					# Increment key value for next topic
					topic_key_val = topic_key_val + 1

					# Output topic to JSON format
					topic_json_struct = {}
					topic_json_struct['_key'] = topic_key
					topic_json_struct["_type"] = _type
					topic_json_struct['title'] = topic_title
					topic_json_struct['definition'] = definition
					topic_json_struct['terms'] = terms
					topic_json_struct['sources'] = "Web of Science, row " + str(rowidx + 2)

					# Store in list to output at end
					organization_topics.append(topic_json_struct)

					# (1) Link from research organizations cluster to organization
					link_key = 'L' + str(link_key_val)
					# Increment key value for next link
					link_key_val = link_key_val + 1
					# Output link to JSON format
					link_json_struct = {}
					link_json_struct['_key'] = link_key
					link_json_struct['_type'] = 'hasInstance'
					link_json_struct['name'] = ''
					link_json_struct['definition'] = ''
					link_json_struct['_from'] = 'T22' 
					link_json_struct['_to'] = topic_key
					# Store in list to output at end
					organization_links.append(link_json_struct)

				# (2) Link research organizations to researcher
				# Researchers does not follow the same method of adding row x, row y to sources. We have a last name and a first initial, but that is not enough due to duplicate names. We cannot rely on topic['sources'] either
				# As a result, I am getting a list of all the authors for this row and finding the corresponding key in researcher_topics. 
				flipped_name = reprint[:loc - 19]
				last_name = flipped_name[:flipped_name.find(',')].title()
				authors = publication_row['AF'].split(";")
				researcher_key = None
				for author in authors:
					# Check for incorrectly formatted name - very rare, but has to be done
					if (author.find(',') == -1):
						# Skip if no comma
						continue
					first, last = parse_author(author)
					if (last_name == last):
						researcher_key = researchers_name_to_key.get(form_author_name(first, last))
				# This is possible and is due to different spellings of the name. There are 7 researchers where this occurs
				if researcher_key == None:
					pass
					# print(flipped_name + " on row " + str(rowidx + 2) + " could not be found in the created researchers")
				else:
					link_key = 'L' + str(link_key_val)
					# Increment key value for next link
					link_key_val = link_key_val + 1
					# Output link to JSON format
					link_json_struct = {}
					link_json_struct['_key'] = link_key
					link_json_struct['_type'] = 'link'
					link_json_struct['name'] = 'is affiliated with'
					link_json_struct['definition'] = ''
					link_json_struct['_from'] =  researcher_key
					link_json_struct['_to'] = topic_key
					# Store in list to output at end if link does not already exit
					if (duplicated_links_dict.get((researcher_key, topic_key)) == None):
						organization_links.append(link_json_struct)
						duplicated_links_dict[(researcher_key, topic_key)] = 1
		organization_topics = self.post_process_organizations(organization_topics)
		return organization_topics, organization_links, topic_key_val, link_key_val

# General helper function
def add_new_topics(old_topics, new_topics):
	for topic in new_topics:
		old_topics.append(topic)
	return old_topics

# General helper function
def add_new_links(old_links, new_links):
	for link in new_links:
		old_links.append(link)
	return old_links

# General helper function
def parse_author(author):
	# The form is LastName, FirstName or LastName, FirstName Middle
	# The middle name will remain part of the first name
	author = author.strip()
	last_name = author.split(',')[0].strip().title()
	first_name = author.split(",")[1].strip().title()
	return first_name, last_name

# General helper function
def form_author_name(first_name, last_name):
	return first_name + " " + last_name

# General helper function
def output_to_file(info, file):
	with open(file, 'w') as f:
		# There's probably a better way to output as a list of JSON objects
		f.write('[')
		i = 0
		for topic in info:
			f.write(json.dumps(topic))
			if i != len(info) - 1:
				f.write(",\n")
			else:
				f.write('\n')
			i = i + 1
		f.write(']')

def main():
	# Create list of topics
	new_topics = list()
	new_links = list()

	# Load and clean the data
	wos_data = pd.concat([pd.read_csv("wos_data.csv"), pd.read_csv('wos_data2.csv')])
	wos_data = wos_data.fillna('')
	wos_data.drop_duplicates('DI')

	print("Creating clusters")
	cluster_runner = Convert_Clusters()
	cluster_topics, cluster_links, topic_key_val, link_key_val = cluster_runner.convert_clusters()
	new_topics = add_new_topics(new_topics, cluster_topics)
	new_links = add_new_links(new_links, cluster_links)

	print("Converting researchers")
	researcher_runner = Convert_Researchers()
	researcher_topics, researcher_links, topic_key_val, link_key_val = 	researcher_runner.convert_researchers(wos_data, topic_key_val, link_key_val)
	new_topics = add_new_topics(new_topics, researcher_topics)
	new_links = add_new_links(new_links, researcher_links)

	print("Converting publications")
	publication_runner = Convert_Publications()
	publication_topics, publication_links, topic_key_val, link_key_val = publication_runner.convert_publications(wos_data, topic_key_val, link_key_val)
	new_topics = add_new_topics(new_topics, publication_topics)
	new_links = add_new_links(new_links, publication_links)

	print("Converting journals")
	journal_runner = Convert_Journals()
	journal_topics, journal_links, topic_key_val, link_key_val = journal_runner.convert_journals(wos_data, topic_key_val, link_key_val, publication_topics)
	new_topics = add_new_topics(new_topics, journal_topics)
	new_links = add_new_links(new_links, journal_links)

	print("Converting articles")
	article_runner = Convert_Articles()
	article_topics, article_links, topic_key_val, link_key_val = article_runner.convert_articles(wos_data, topic_key_val, link_key_val, researcher_topics, publication_topics, journal_topics, journal_links)
	new_topics = add_new_topics(new_topics, article_topics)
	new_links = add_new_links(new_links, article_links)

	print("Converting events")
	event_runner = Convert_Events()
	event_topics, event_links, topic_key_val, link_key_val = event_runner.convert_events(wos_data, topic_key_val, link_key_val, article_topics)
	new_topics = add_new_topics(new_topics, event_topics)
	new_links = add_new_links(new_links, event_links)

	print("Converting organizations")
	organization_runner = Convert_Organizations()
	organization_topics, organization_links, topic_key_val, link_key_val = organization_runner.convert_organizations(wos_data, topic_key_val, link_key_val, researcher_topics, publication_topics)
	new_topics = add_new_topics(new_topics, organization_topics)
	new_links = add_new_links(new_links, organization_links)

	# ---- ISS	----

	print("Outputting to files")
	# Output topics to file
	output_to_file(new_topics, 'output/combined_topics.json')
	output_to_file(new_links, 'output/combined_links.json')

if __name__ == '__main__':
	main()