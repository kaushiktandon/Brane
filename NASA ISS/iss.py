import json
import csv
import numpy as np
import pandas as pd

def convert_clusters():
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
	properties['title'] = "ISS research ecosystem"
	cluster_topics.append(create_topic(properties))
	# T2
	properties['_key'] = 'T2'
	properties['_type'] = 'cluster'
	properties['title'] = "Individual"
	cluster_topics.append(create_topic(properties))
	# T3
	properties['_key'] = 'T3'
	properties['_type'] = 'cluster'
	properties['title'] = "Researcher"
	cluster_topics.append(create_topic(properties))
	# T4
	properties['_key'] = 'T4'
	properties['_type'] = 'cluster'
	properties['title'] = "Event"
	cluster_topics.append(create_topic(properties))
	# T5
	properties['_key'] = 'T5'
	properties['_type'] = 'cluster'
	properties['title'] = "Conference"
	cluster_topics.append(create_topic(properties))
	# T6
	properties['_key'] = 'T6'
	properties['_type'] = 'cluster'
	properties['title'] = "Workshop"
	cluster_topics.append(create_topic(properties))
	# T7
	properties['_key'] = 'T7'
	properties['_type'] = 'cluster'
	properties['title'] = "Symposium"
	cluster_topics.append(create_topic(properties))
	# T8
	properties['_key'] = 'T8'
	properties['_type'] = 'cluster'
	properties['title'] = "Congress"
	cluster_topics.append(create_topic(properties))
	# T9
	properties['_key'] = 'T9'
	properties['_type'] = 'cluster'
	properties['title'] = "Meeting"
	cluster_topics.append(create_topic(properties))
	# T10
	properties['_key'] = 'T10'
	properties['_type'] = 'cluster'
	properties['title'] = "Publication"
	cluster_topics.append(create_topic(properties))
	# T11
	properties['_key'] = 'T11'
	properties['_type'] = 'cluster'
	properties['title'] = "Journal"
	cluster_topics.append(create_topic(properties))
	# T12
	properties['_key'] = 'T12'
	properties['_type'] = 'cluster'
	properties['title'] = "Conference Proceeding"
	cluster_topics.append(create_topic(properties))
	# T13
	properties['_key'] = 'T13'
	properties['_type'] = 'cluster'
	properties['title'] = "Article"
	cluster_topics.append(create_topic(properties))
	# T14
	properties['_key'] = 'T14'
	properties['_type'] = 'property'
	properties['title'] = "Access type"
	properties['valueType'] = 'String'		
	cluster_topics.append(create_topic(properties))
	# T15
	properties['_key'] = 'T15'
	properties['_type'] = 'property'
	properties['title'] = "Download date"
	properties['valueType'] = 'Date'		
	cluster_topics.append(create_topic(properties))
	# T16
	properties['_key'] = 'T16'
	properties['_type'] = 'property'
	properties['title'] = "Publication type"
	properties['valueType'] = 'String'		
	cluster_topics.append(create_topic(properties))
	# T17
	properties['_key'] = 'T17'
	properties['_type'] = 'property'
	properties['title'] = "Language"
	properties['valueType'] = 'String'		
	cluster_topics.append(create_topic(properties))
	# T18
	properties['_key'] = 'T18'
	properties['_type'] = 'property'
	properties['title'] = "Published date"
	properties['valueType'] = 'Date'		
	cluster_topics.append(create_topic(properties))
	# T19
	properties['_key'] = 'T19'
	properties['_type'] = 'property'
	properties['title'] = "Document type"
	properties['valueType'] = 'String'		
	cluster_topics.append(create_topic(properties))
	# T20
	properties['_key'] = 'T20'
	properties['_type'] = 'property'
	properties['title'] = "Conference year"
	properties['valueType'] = 'String'		
	cluster_topics.append(create_topic(properties))
	# T21
	properties['_key'] = 'T21'
	properties['_type'] = 'cluster'
	properties['title'] = "Organization"
	properties['valueType'] = ''		
	cluster_topics.append(create_topic(properties))
	# T22
	properties['_key'] = 'T22'
	properties['_type'] = 'cluster'
	properties['title'] = "Other research organization"
	cluster_topics.append(create_topic(properties))
	# T23
	properties['_key'] = 'T23'
	properties['_type'] = 'cluster'
	properties['title'] = "Publisher"
	cluster_topics.append(create_topic(properties))
	# T24
	properties['_key'] = 'T24'
	properties['_type'] = 'cluster'
	properties['title'] = "Web of Science Keyword"
	cluster_topics.append(create_topic(properties))
	# T25
	properties['_key'] = 'T25'
	properties['_type'] = 'cluster'
	properties['title'] = 'Tagged Web of Science Keyword'
	cluster_topics.append(create_topic(properties))
	# T26
	properties['_key'] = 'T26'
	properties['_type'] = 'cluster'
	properties['title'] = 'Untagged Web of Science Keyword'
	cluster_topics.append(create_topic(properties))
	# T27
	properties['_key'] = 'T27'
	properties['_type'] = 'cluster'
	properties['title'] = 'ISS Investigation'
	cluster_topics.append(create_topic(properties))
	# T29
	properties['_key'] = 'T29'
	properties['_type'] = 'cluster'
	properties['title'] = 'Space agency'
	cluster_topics.append(create_topic(properties))
	# T30
	properties['_key'] = 'T30'
	properties['_type'] = 'cluster'
	properties['title'] = 'Sponsoring organization'
	cluster_topics.append(create_topic(properties))
	# T31
	properties['_key'] = 'T31'
	properties['_type'] = 'cluster'
	properties['title'] = 'Principal investigator'
	cluster_topics.append(create_topic(properties))
	# T32
	properties['_key'] = 'T32'
	properties['_type'] = 'cluster'
	properties['title'] = 'City'
	cluster_topics.append(create_topic(properties))
	# T33
	properties['_key'] = 'T33'
	properties['_type'] = 'cluster'
	properties['title'] = 'State'
	cluster_topics.append(create_topic(properties))
	# T34
	properties['_key'] = 'T34'
	properties['_type'] = 'cluster'
	properties['title'] = 'Country'
	cluster_topics.append(create_topic(properties))
	# T35
	properties['_key'] = 'T35'
	properties['_type'] = 'property'
	properties['title'] = 'Operations location'
	cluster_topics.append(create_topic(properties))
	# T36
	properties['_key'] = 'T36'
	properties['_type'] = 'cluster'
	properties['title'] = 'Academic activity'
	cluster_topics.append(create_topic(properties))
	# T37
	properties['_key'] = 'T37'
	properties['_type'] = 'cluster'
	properties['title'] = 'Location'
	cluster_topics.append(create_topic(properties))
	# T38
	properties['_key'] = 'T38'
	properties['_type'] = 'cluster'
	properties['title'] = 'Category'
	cluster_topics.append(create_topic(properties))
	# T39
	properties['_key'] = 'T39'
	properties['_type'] = 'cluster'
	properties['title'] = 'Biology and Biotechnology investigation'
	cluster_topics.append(create_topic(properties))
	# T40
	properties['_key'] = 'T40'
	properties['_type'] = 'cluster'
	properties['title'] = 'Animal Biology - Invertebrates'
	cluster_topics.append(create_topic(properties))
	# T41
	properties['_key'] = 'T41'
	properties['_type'] = 'cluster'
	properties['title'] = 'Animal Biology - Vertebrates'
	cluster_topics.append(create_topic(properties))
	# T42
	properties['_key'] = 'T42'
	properties['_type'] = 'cluster'
	properties['title'] = 'Cellular Biology investigation'
	cluster_topics.append(create_topic(properties))
	# T43
	properties['_key'] = 'T43'
	properties['_type'] = 'cluster'
	properties['title'] = 'Macromolecular Crystal Growth investigation'
	cluster_topics.append(create_topic(properties))
	# T44
	properties['_key'] = 'T44'
	properties['_type'] = 'cluster'
	properties['title'] = 'Microbiology investigation'
	cluster_topics.append(create_topic(properties))
	# T45
	properties['_key'] = 'T45'
	properties['_type'] = 'cluster'
	properties['title'] = 'Microencapsulation investigation'
	cluster_topics.append(create_topic(properties))
	# T46
	properties['_key'] = 'T46'
	properties['_type'] = 'cluster'
	properties['title'] = 'Plant Biology investigation'
	cluster_topics.append(create_topic(properties))
	# T47
	properties['_key'] = 'T47'
	properties['_type'] = 'cluster'
	properties['title'] = 'Vaccine Development investigation'
	cluster_topics.append(create_topic(properties))
	# T48
	properties['_key'] = 'T48'
	properties['_type'] = 'cluster'
	properties['title'] = 'Earth and Space Science investigation'
	cluster_topics.append(create_topic(properties))
	# T49
	properties['_key'] = 'T49'
	properties['_type'] = 'cluster'
	properties['title'] = 'Astrobiology investigation'
	cluster_topics.append(create_topic(properties))
	# T50
	properties['_key'] = 'T50'
	properties['_type'] = 'cluster'
	properties['title'] = 'Astrophysics investigation'
	cluster_topics.append(create_topic(properties))
	# T51
	properties['_key'] = 'T51'
	properties['_type'] = 'cluster'
	properties['title'] = 'Earth Remote Sensing investigation'
	cluster_topics.append(create_topic(properties))
	# T52
	properties['_key'] = 'T52'
	properties['_type'] = 'cluster'
	properties['title'] = 'Heliophysics investigation'
	cluster_topics.append(create_topic(properties))
	# T53
	properties['_key'] = 'T53'
	properties['_type'] = 'cluster'
	properties['title'] = 'Educational and cultural activities investigation'
	cluster_topics.append(create_topic(properties))
	# T54
	properties['_key'] = 'T54'
	properties['_type'] = 'cluster'
	properties['title'] = 'Classroom Versions of ISS Investigations investigation'
	cluster_topics.append(create_topic(properties))
	# T55
	properties['_key'] = 'T55'
	properties['_type'] = 'cluster'
	properties['title'] = 'Educational Competitions investigation'
	cluster_topics.append(create_topic(properties))
	# T56
	properties['_key'] = 'T56'
	properties['_type'] = 'cluster'
	properties['title'] = 'Educational Demonstrations investigation'
	cluster_topics.append(create_topic(properties))
	# T57
	properties['_key'] = 'T57'
	properties['_type'] = 'cluster'
	properties['title'] = 'Student-Developed Investigations'
	cluster_topics.append(create_topic(properties))
	# T58
	properties['_key'] = 'T58'
	properties['_type'] = 'cluster'
	properties['title'] = 'Human Research investigation'
	cluster_topics.append(create_topic(properties))
	# T59
	properties['_key'] = 'T59'
	properties['_type'] = 'cluster'
	properties['title'] = 'Bone and Muscle Physiology investigation'
	cluster_topics.append(create_topic(properties))
	# T60
	properties['_key'] = 'T60'
	properties['_type'] = 'cluster'
	properties['title'] = 'Cardiovascular and Respiratory Systems investigation'
	cluster_topics.append(create_topic(properties))
	# T61
	properties['_key'] = 'T61'
	properties['_type'] = 'cluster'
	properties['title'] = 'Crew Healthcare Systems investigation'
	cluster_topics.append(create_topic(properties))
	# T62
	properties['_key'] = 'T62'
	properties['_type'] = 'cluster'
	properties['title'] = 'Habitability and Human Factors investigation'
	cluster_topics.append(create_topic(properties))
	# T63
	properties['_key'] = 'T63'
	properties['_type'] = 'cluster'
	properties['title'] = 'Human Behavior and Performance investigation'
	cluster_topics.append(create_topic(properties))
	# T64
	properties['_key'] = 'T64'
	properties['_type'] = 'cluster'
	properties['title'] = 'Human Microbiome investigation'
	cluster_topics.append(create_topic(properties))
	# T65
	properties['_key'] = 'T65'
	properties['_type'] = 'cluster'
	properties['title'] = 'Immune System investigation'
	cluster_topics.append(create_topic(properties))
	# T66
	properties['_key'] = 'T66'
	properties['_type'] = 'cluster'
	properties['title'] = 'Integrated Physiology and Nutrition investigation'
	cluster_topics.append(create_topic(properties))
	# T67
	properties['_key'] = 'T67'
	properties['_type'] = 'cluster'
	properties['title'] = 'Nervous and Vestibular Systems investigation'
	cluster_topics.append(create_topic(properties))
	# T68
	properties['_key'] = 'T68'
	properties['_type'] = 'cluster'
	properties['title'] = 'Radiation Impacts on Humans investigation'
	cluster_topics.append(create_topic(properties))
	# T69
	properties['_key'] = 'T69'
	properties['_type'] = 'cluster'
	properties['title'] = 'Vision investigation'
	cluster_topics.append(create_topic(properties))
	# T70
	properties['_key'] = 'T70'
	properties['_type'] = 'cluster'
	properties['title'] = 'Physical science investigation'
	cluster_topics.append(create_topic(properties))
	# T71
	properties['_key'] = 'T71'
	properties['_type'] = 'cluster'
	properties['title'] = 'Combustion Science investigation'
	cluster_topics.append(create_topic(properties))
	# T72
	properties['_key'] = 'T72'
	properties['_type'] = 'cluster'
	properties['title'] = 'Complex Fluids investigation'
	cluster_topics.append(create_topic(properties))
	# T73
	properties['_key'] = 'T73'
	properties['_type'] = 'cluster'
	properties['title'] = 'Fluid Physics investigation'
	cluster_topics.append(create_topic(properties))
	# T74
	properties['_key'] = 'T74'
	properties['_type'] = 'cluster'
	properties['title'] = 'Fundamental Physics investigation'
	cluster_topics.append(create_topic(properties))
	# T75
	properties['_key'] = 'T75'
	properties['_type'] = 'cluster'
	properties['title'] = 'Materials Science investigation'
	cluster_topics.append(create_topic(properties))
	# T76
	properties['_key'] = 'T76'
	properties['_type'] = 'cluster'
	properties['title'] = 'Technology Development and Demonstration investigation'
	cluster_topics.append(create_topic(properties))
	# T77
	properties['_key'] = 'T77'
	properties['_type'] = 'cluster'
	properties['title'] = 'Air, Water and Surface Monitoring'
	cluster_topics.append(create_topic(properties))
	# T78
	properties['_key'] = 'T78'
	properties['_type'] = 'cluster'
	properties['title'] = 'Avionics and Software investigation'
	cluster_topics.append(create_topic(properties))
	# T79
	properties['_key'] = 'T79'
	properties['_type'] = 'cluster'
	properties['title'] = 'Characterizing Experiment Hardware investigation'
	cluster_topics.append(create_topic(properties))
	# T80
	properties['_key'] = 'T80'
	properties['_type'] = 'cluster'
	properties['title'] = 'Commercial Demonstrations investigation'
	cluster_topics.append(create_topic(properties))
	# T81
	properties['_key'] = 'T81'
	properties['_type'] = 'cluster'
	properties['title'] = 'Communication and Navigation investigation'
	cluster_topics.append(create_topic(properties))
	# T82
	properties['_key'] = 'T82'
	properties['_type'] = 'cluster'
	properties['title'] = 'Fire Suppression and Detection investigation'
	cluster_topics.append(create_topic(properties))
	# T83
	properties['_key'] = 'T83'
	properties['_type'] = 'cluster'
	properties['title'] = 'Food and Clothing Systems investigation'
	cluster_topics.append(create_topic(properties))
	# T84
	properties['_key'] = 'T84'
	properties['_type'] = 'cluster'
	properties['title'] = 'Imaging Technology investigation'
	cluster_topics.append(create_topic(properties))
	# T85
	properties['_key'] = 'T85'
	properties['_type'] = 'cluster'
	properties['title'] = 'Life Support Systems and Habitation investigation'
	cluster_topics.append(create_topic(properties))
	# T86
	properties['_key'] = 'T86'
	properties['_type'] = 'cluster'
	properties['title'] = 'Microbial Populations in Spacecraft investigation'
	cluster_topics.append(create_topic(properties))
	# T87
	properties['_key'] = 'T87'
	properties['_type'] = 'cluster'
	properties['title'] = 'Microgravity Environment Measurement investigation'
	cluster_topics.append(create_topic(properties))
	# T88
	properties['_key'] = 'T88'
	properties['_type'] = 'cluster'
	properties['title'] = 'Radiation Measurements and Shielding investigation'
	cluster_topics.append(create_topic(properties))
	# T89
	properties['_key'] = 'T89'
	properties['_type'] = 'cluster'
	properties['title'] = 'Repair and Fabrication Technologies investigation'
	cluster_topics.append(create_topic(properties))
	# T90
	properties['_key'] = 'T90'
	properties['_type'] = 'cluster'
	properties['title'] = 'Robotics investigation'
	cluster_topics.append(create_topic(properties))
	# T91
	properties['_key'] = 'T91'
	properties['_type'] = 'cluster'
	properties['title'] = 'Small Satellites and Control Technologies investigation'
	cluster_topics.append(create_topic(properties))
	# T92
	properties['_key'] = 'T92'
	properties['_type'] = 'cluster'
	properties['title'] = 'Space Structures investigation'
	cluster_topics.append(create_topic(properties))
	# T93
	properties['_key'] = 'T93'
	properties['_type'] = 'cluster'
	properties['title'] = 'Spacecraft and Orbital Environments investigation'
	cluster_topics.append(create_topic(properties))
	# T94
	properties['_key'] = 'T94'
	properties['_type'] = 'cluster'
	properties['title'] = 'Spacecraft Materials investigation'
	cluster_topics.append(create_topic(properties))
	# T95
	properties['_key'] = 'T95'
	properties['_type'] = 'cluster'
	properties['title'] = 'Thermal Management Systems investigation'
	cluster_topics.append(create_topic(properties))
	# T96
	properties['_key'] = 'T96'
	properties['_type'] = 'cluster'
	properties['title'] = 'Wordnet ontology'
	cluster_topics.append(create_topic(properties))
	# T97
	properties['_key'] = 'T97'
	properties['_type'] = 'cluster'
	properties['title'] = 'University'
	cluster_topics.append(create_topic(properties))

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
	cluster_links.append(create_link(properties))
	# L2
	properties['_key'] = 'L2'
	properties['_type'] = 'encompasses'
	properties['_from'] = 'T1'
	properties['_to'] = 'T27'
	cluster_links.append(create_link(properties))
	# L3
	properties['_key'] = 'L3'
	properties['_type'] = 'encompasses'
	properties['_from'] = 'T1'
	properties['_to'] = 'T36'
	cluster_links.append(create_link(properties))
	# L4
	properties['_key'] = 'L4'
	properties['_type'] = 'encompasses'
	properties['_from'] = 'T1'
	properties['_to'] = 'T21'
	cluster_links.append(create_link(properties))
	# L5
	properties['_key'] = 'L5'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T2'
	properties['_to'] = 'T3'
	cluster_links.append(create_link(properties))
	# L6
	properties['_key'] = 'L6'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T4'
	properties['_to'] = 'T5'
	cluster_links.append(create_link(properties))
	# L7
	properties['_key'] = 'L7'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T4'
	properties['_to'] = 'T6'
	cluster_links.append(create_link(properties))
	# L8
	properties['_key'] = 'L8'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T4'
	properties['_to'] = 'T7'
	cluster_links.append(create_link(properties))
	# L9
	properties['_key'] = 'L9'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T4'
	properties['_to'] = 'T8'
	cluster_links.append(create_link(properties))
	# L9
	properties['_key'] = 'L9'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T4'
	properties['_to'] = 'T9'
	cluster_links.append(create_link(properties))
	# L10	
	properties['_key'] = 'L10'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T10'
	properties['_to'] = 'T11'
	cluster_links.append(create_link(properties))
	# L11	
	properties['_key'] = 'L11'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T10'
	properties['_to'] = 'T12'
	cluster_links.append(create_link(properties))
	# L12	
	properties['_key'] = 'L12'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T10'
	properties['_to'] = 'T13'
	cluster_links.append(create_link(properties))
	# L13	
	properties['_key'] = 'L13'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T21'
	properties['_to'] = 'T22'
	cluster_links.append(create_link(properties))
	# L14	
	properties['_key'] = 'L14'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T21'
	properties['_to'] = 'T23'
	cluster_links.append(create_link(properties))
	# L15	
	properties['_key'] = 'L15'
	properties['_type'] = 'encompasses'
	properties['_from'] = 'T1'
	properties['_to'] = 'T24'
	cluster_links.append(create_link(properties))
	# L16	
	properties['_key'] = 'L16'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T24'
	properties['_to'] = 'T25'
	cluster_links.append(create_link(properties))
	# L17	
	properties['_key'] = 'L17'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T24'
	properties['_to'] = 'T26'
	cluster_links.append(create_link(properties))
	# L19	
	properties['_key'] = 'L19'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T21'
	properties['_to'] = 'T29'
	cluster_links.append(create_link(properties))
	# L20	
	properties['_key'] = 'L20'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T21'
	properties['_to'] = 'T30'
	cluster_links.append(create_link(properties))
	# L21	
	properties['_key'] = 'L21'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T2'
	properties['_to'] = 'T31'
	cluster_links.append(create_link(properties))
	# L22	
	properties['_key'] = 'L22'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T37'
	properties['_to'] = 'T32'
	cluster_links.append(create_link(properties))
	# L23	
	properties['_key'] = 'L23'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T37'
	properties['_to'] = 'T33'
	cluster_links.append(create_link(properties))
	# L24	
	properties['_key'] = 'L24'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T37'
	properties['_to'] = 'T34'
	cluster_links.append(create_link(properties))
	# L26	
	properties['_key'] = 'L26'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T27'
	properties['_to'] = 'T39'
	cluster_links.append(create_link(properties))
	# L27	
	properties['_key'] = 'L27'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T27'
	properties['_to'] = 'T48'
	cluster_links.append(create_link(properties))
	# L28	
	properties['_key'] = 'L28'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T27'
	properties['_to'] = 'T53'
	cluster_links.append(create_link(properties))
	# L29	
	properties['_key'] = 'L29'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T27'
	properties['_to'] = 'T58'
	cluster_links.append(create_link(properties))
	# L30	
	properties['_key'] = 'L30'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T27'
	properties['_to'] = 'T70'
	cluster_links.append(create_link(properties))
	# L31	
	properties['_key'] = 'L31'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T27'
	properties['_to'] = 'T76'
	cluster_links.append(create_link(properties))
	# L32	
	properties['_key'] = 'L32'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T39'
	properties['_to'] = 'T40'
	cluster_links.append(create_link(properties))
	# L33	
	properties['_key'] = 'L33'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T39'
	properties['_to'] = 'T41'
	cluster_links.append(create_link(properties))
	# L34	
	properties['_key'] = 'L34'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T39'
	properties['_to'] = 'T42'
	cluster_links.append(create_link(properties))
	# L35	
	properties['_key'] = 'L35'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T39'
	properties['_to'] = 'T43'
	cluster_links.append(create_link(properties))
	# L36	
	properties['_key'] = 'L36'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T39'
	properties['_to'] = 'T44'
	cluster_links.append(create_link(properties))
	# L37	
	properties['_key'] = 'L37'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T39'
	properties['_to'] = 'T45'
	cluster_links.append(create_link(properties))
	# L38	
	properties['_key'] = 'L38'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T39'
	properties['_to'] = 'T46'
	cluster_links.append(create_link(properties))
	# L39	
	properties['_key'] = 'L39'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T39'
	properties['_to'] = 'T47'
	cluster_links.append(create_link(properties))
	# L40	
	properties['_key'] = 'L40'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T48'
	properties['_to'] = 'T49'
	cluster_links.append(create_link(properties))
	# L41	
	properties['_key'] = 'L41'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T48'
	properties['_to'] = 'T50'
	cluster_links.append(create_link(properties))
	# L42	
	properties['_key'] = 'L42'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T48'
	properties['_to'] = 'T51'
	cluster_links.append(create_link(properties))
	# L43	
	properties['_key'] = 'L43'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T48'
	properties['_to'] = 'T52'
	cluster_links.append(create_link(properties))
	# L44	
	properties['_key'] = 'L44'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T53'
	properties['_to'] = 'T54'
	cluster_links.append(create_link(properties))
	# L45	
	properties['_key'] = 'L45'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T53'
	properties['_to'] = 'T55'
	cluster_links.append(create_link(properties))
	# L46	
	properties['_key'] = 'L46'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T53'
	properties['_to'] = 'T56'
	cluster_links.append(create_link(properties))
	# L47	
	properties['_key'] = 'L47'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T53'
	properties['_to'] = 'T57'
	cluster_links.append(create_link(properties))
	# L48	
	properties['_key'] = 'L48'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T58'
	properties['_to'] = 'T59'
	cluster_links.append(create_link(properties))
	# L49	
	properties['_key'] = 'L49'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T58'
	properties['_to'] = 'T60'
	cluster_links.append(create_link(properties))
	# L50	
	properties['_key'] = 'L50'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T58'
	properties['_to'] = 'T61'
	cluster_links.append(create_link(properties))
	# L51	
	properties['_key'] = 'L51'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T58'
	properties['_to'] = 'T62'
	cluster_links.append(create_link(properties))
	# L52	
	properties['_key'] = 'L52'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T58'
	properties['_to'] = 'T63'
	cluster_links.append(create_link(properties))
	# L53	
	properties['_key'] = 'L53'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T58'
	properties['_to'] = 'T64'
	cluster_links.append(create_link(properties))
	# L54	
	properties['_key'] = 'L54'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T58'
	properties['_to'] = 'T65'
	cluster_links.append(create_link(properties))
	# L55	
	properties['_key'] = 'L55'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T58'
	properties['_to'] = 'T66'
	cluster_links.append(create_link(properties))
	# L56	
	properties['_key'] = 'L56'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T58'
	properties['_to'] = 'T67'
	cluster_links.append(create_link(properties))
	# L57	
	properties['_key'] = 'L57'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T58'
	properties['_to'] = 'T68'
	cluster_links.append(create_link(properties))
	# L58	
	properties['_key'] = 'L58'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T58'
	properties['_to'] = 'T69'
	cluster_links.append(create_link(properties))
	# L59	
	properties['_key'] = 'L59'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T70'
	properties['_to'] = 'T71'
	cluster_links.append(create_link(properties))
	# L60	
	properties['_key'] = 'L60'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T70'
	properties['_to'] = 'T72'
	cluster_links.append(create_link(properties))
	# L61	
	properties['_key'] = 'L61'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T70'
	properties['_to'] = 'T73'
	cluster_links.append(create_link(properties))
	# L62	
	properties['_key'] = 'L62'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T70'
	properties['_to'] = 'T74'
	cluster_links.append(create_link(properties))
	# L63	
	properties['_key'] = 'L63'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T70'
	properties['_to'] = 'T75'
	cluster_links.append(create_link(properties))
	# L64	
	properties['_key'] = 'L64'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T76'
	properties['_to'] = 'T77'
	cluster_links.append(create_link(properties))
	# L65	
	properties['_key'] = 'L65'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T76'
	properties['_to'] = 'T78'
	cluster_links.append(create_link(properties))
	# L66	
	properties['_key'] = 'L66'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T76'
	properties['_to'] = 'T79'
	cluster_links.append(create_link(properties))
	# L67	
	properties['_key'] = 'L67'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T76'
	properties['_to'] = 'T80'
	cluster_links.append(create_link(properties))
	# L68	
	properties['_key'] = 'L68'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T76'
	properties['_to'] = 'T81'
	cluster_links.append(create_link(properties))
	# L69	
	properties['_key'] = 'L69'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T76'
	properties['_to'] = 'T82'
	cluster_links.append(create_link(properties))
	# L70	
	properties['_key'] = 'L70'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T76'
	properties['_to'] = 'T83'
	cluster_links.append(create_link(properties))
	# L71	
	properties['_key'] = 'L71'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T76'
	properties['_to'] = 'T84'
	cluster_links.append(create_link(properties))
	# L72	
	properties['_key'] = 'L72'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T76'
	properties['_to'] = 'T85'
	cluster_links.append(create_link(properties))
	# L73	
	properties['_key'] = 'L73'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T76'
	properties['_to'] = 'T86'
	cluster_links.append(create_link(properties))
	# L74	
	properties['_key'] = 'L74'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T76'
	properties['_to'] = 'T87'
	cluster_links.append(create_link(properties))
	# L75	
	properties['_key'] = 'L75'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T76'
	properties['_to'] = 'T88'
	cluster_links.append(create_link(properties))
	# L76	
	properties['_key'] = 'L76'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T76'
	properties['_to'] = 'T89'
	cluster_links.append(create_link(properties))
	# L77	
	properties['_key'] = 'L77'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T76'
	properties['_to'] = 'T90'
	cluster_links.append(create_link(properties))
	# L78	
	properties['_key'] = 'L78'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T76'
	properties['_to'] = 'T91'
	cluster_links.append(create_link(properties))
	# L79	
	properties['_key'] = 'L79'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T76'
	properties['_to'] = 'T92'
	cluster_links.append(create_link(properties))
	# L80	
	properties['_key'] = 'L80'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T76'
	properties['_to'] = 'T93'
	cluster_links.append(create_link(properties))
	# L81	
	properties['_key'] = 'L81'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T76'
	properties['_to'] = 'T94'
	cluster_links.append(create_link(properties))
	# L82	
	properties['_key'] = 'L82'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T76'
	properties['_to'] = 'T95'
	cluster_links.append(create_link(properties))
	# L83	
	properties['_key'] = 'L83'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T36'
	properties['_to'] = 'T4'
	cluster_links.append(create_link(properties))
	# L84	
	properties['_key'] = 'L84'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T36'
	properties['_to'] = 'T10'
	cluster_links.append(create_link(properties))
	# L85	
	properties['_key'] = 'L85'
	properties['_type'] = 'encompasses'
	properties['_from'] = 'T1'
	properties['_to'] = 'T96'
	cluster_links.append(create_link(properties))
	# L86	
	properties['_key'] = 'L86'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T21'
	properties['_to'] = 'T97'
	cluster_links.append(create_link(properties))

	return cluster_topics, cluster_links, len(cluster_topics) + 1, len(cluster_links) + 1
def create_topic(properties):
	topic_json_struct = {}
	for prop, value in properties.items():
		topic_json_struct[prop] = value
	return topic_json_struct
def create_link(properties):
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

def convert_investigations(data, topic_key_val, link_key_val, subcategory_topics, article_topics):
	investigation_topics = list()
	investigation_links = list()

	# Preprocess by mapping article DOI to article key
	article_topic_doi_to_key = dict()
	for article_topic_json in article_topics:
		article_topic_doi_to_key[article_topic_json['DOI']] = article_topic_json["_key"]

	for rowidx in range(len(data)):
		# Get current row in dataset
		investigation_row = data.iloc[rowidx,:]
		_type = "topic"
		topic_title = investigation_row['Name']
		definition = topic_title + " - " + investigation_row['PAOSummary']
		terms = [topic_title, investigation_row['PAOSummary']]
		pst_id = investigation_row['PST ID']
		# Look for duplicates
		duplicate = False
		for topic in investigation_topics:
			if topic['title'] == topic_title:
				duplicate = True
		# Skip making a topic for this publication
		if (duplicate):
			continue

		topic_key = 'T' + str(topic_key_val)
		# Increment key value for next topic
		topic_key_val = topic_key_val + 1

		# (1) Output investigation topic to JSON format
		topic_json_struct = {}
		topic_json_struct['_key'] = topic_key
		topic_json_struct["_type"] = _type
		topic_json_struct['title'] = topic_title
		topic_json_struct['definition'] = definition
		topic_json_struct['terms'] = terms
		topic_json_struct['PST ID'] = str(pst_id)
		topic_json_struct['sources'] = "Investigations, row " + str(rowidx + 2)

		# Store in list to output at end
		investigation_topics.append(topic_json_struct)

		link_key = 'L' + str(link_key_val)
		# Increment key value for next link
		link_key_val = link_key_val + 1

		# (2) Output link to JSON format between investigation and T27
		link_json_struct = {}
		link_json_struct['_key'] = link_key
		link_json_struct['_type'] = 'hasInstance'
		link_json_struct['name'] = ''
		link_json_struct['_from'] = 'T27' 
		link_json_struct['_to'] = topic_key

		# Store in list to output at end
		investigation_links.append(link_json_struct)

		# (3) Link between subcategory and investigation ID
		found = False
		subcategory_id = -1
		title_to_check = investigation_row['Subcategory'] + " investigation"
		for subcategory_topic_json in subcategory_topics:
			if subcategory_topic_json['title'] == title_to_check:
				found = True
				subcategory_id = subcategory_topic_json['_key']
		if found:
			link_key = 'L' + str(link_key_val)
			# Increment key value for next link
			link_key_val = link_key_val + 1

			link_json_struct = {}
			link_json_struct['_key'] = link_key
			link_json_struct['_type'] = 'hasInstance'
			link_json_struct['name'] = ''
			link_json_struct['_from'] = subcategory_id 
			link_json_struct['_to'] = topic_key

			# Store in list to output at end
			investigation_links.append(link_json_struct)

		# (8) Link between Operations and investigation ID
		link_key = 'L' + str(link_key_val)
		# Increment key value for next link
		link_key_val = link_key_val + 1

		link_json_struct = {}
		link_json_struct['_key'] = link_key
		link_json_struct['_type'] = 'has'
		link_json_struct['name'] = ''
		link_json_struct['_from'] = topic_key 
		link_json_struct['_to'] = 'T35'
		link_json_struct['value'] = investigation_row['OperationsLocation']

		# Store in list to output at end
		investigation_links.append(link_json_struct)

		# (21) Link between investigation ID and article ID
		for i in range(1, 46):
			doi = investigation_row['DOI' + str(i)]
			if (doi == ''): break
			article_key = article_topic_doi_to_key.get(doi)
			if (article_key != None):
				link_key = 'L' + str(link_key_val)
				# Increment key value for next link
				link_key_val = link_key_val + 1

				link_json_struct = {}
				link_json_struct['_key'] = link_key
				link_json_struct['_type'] = 'link'
				link_json_struct['name'] = 'outputs'
				link_json_struct['_from'] = topic_key 
				link_json_struct['_to'] = article_key
				investigation_links.append(link_json_struct)
			
	return investigation_topics, investigation_links, topic_key_val, link_key_val

def convert_sponsoring_space_agencies(data, topic_key_val, link_key_val, investigation_topics):
	sponsoring_space_agency_topics = list()
	sponsoring_space_agency_links = list()
	for rowidx in range(len(data)):
		# Get current row in dataset
		agency_row = data.iloc[rowidx,:]
		topic_title = agency_row['SponsoringSpaceAgency']
		abrev = topic_title[topic_title.find('(') + 1 : topic_title.find(')')]
		terms = [topic_title, abrev]		
		# Look for duplicates
		duplicate = False
		topic_key = None
		for topic in sponsoring_space_agency_topics:
			if topic['title'] == topic_title:
				duplicate = True
				topic['sources'] = topic['sources'] + ', row ' + str(rowidx + 2)
				topic_key = topic['_key']
		# Make a new topic if not duplicate
		if (not duplicate):

			topic_key = 'T' + str(topic_key_val)
			# Increment key value for next topic
			topic_key_val = topic_key_val + 1

			# (4a) Create topic for sponsoring agency
			topic_json_struct = {}
			topic_json_struct['_key'] = topic_key
			topic_json_struct["_type"] = 'topic'
			topic_json_struct['title'] = topic_title
			topic_json_struct['definition'] = ''
			topic_json_struct['terms'] = terms
			topic_json_struct['sources'] = "Investigations, row " + str(rowidx + 2)

			sponsoring_space_agency_topics.append(topic_json_struct)

			# (4b) Link sponsoring agency to cluster T29
			link_key = 'L' + str(link_key_val)
			# Increment key value for next link
			link_key_val = link_key_val + 1

			link_json_struct = {}
			link_json_struct['_key'] = link_key
			link_json_struct['_type'] = 'hasInstance'
			link_json_struct['name'] = ''
			link_json_struct['_from'] = 'T29' 
			link_json_struct['_to'] = topic_key

			sponsoring_space_agency_links.append(link_json_struct)

		# (4c) Link between SponsoringSpaceAgency and investigation ID
		# Find corresponding topic in investigation_topics
		my_row = "row " + str(rowidx + 2) + ','
		my_row2 = "row " + str(rowidx + 2)
		temporary_topic_struct = {}
		for topic in investigation_topics:
			if my_row in topic['sources'] or topic['sources'].endswith(my_row2):
				temporary_topic_struct = topic
				break
		investigation_key = temporary_topic_struct['_key']

		link_key = 'L' + str(link_key_val)
		# Increment key value for next link
		link_key_val = link_key_val + 1

		# Output link to JSON format
		link_json_struct = {}
		link_json_struct['_key'] = link_key
		link_json_struct['_type'] = 'link'
		link_json_struct['name'] = 'sponsors'
		link_json_struct['definition'] = ''
		link_json_struct['_from'] = topic_key 
		link_json_struct['_to'] = investigation_key

		# Store in list to output at end
		sponsoring_space_agency_links.append(link_json_struct)

	return sponsoring_space_agency_topics, sponsoring_space_agency_links, topic_key_val, link_key_val

def convert_sponsoring_space_organizations(data, topic_key_val, link_key_val, investigation_topics, sponsoring_space_agency_topics):
	sponsoring_space_organization_topics = list()
	sponsoring_space_organization_links = list()

	nasa_key = None
	for topic in sponsoring_space_agency_topics:
		if topic['title'] == 'National Aeronautics and Space Administration (NASA)':
			nasa_key = topic['_key']
			break

	for rowidx in range(len(data)):
		# Get current row in dataset
		agency_row = data.iloc[rowidx,:]
		topic_title = agency_row['SponsoringOrganization']
		# Don't need to create a topic for this organization
		if topic_title == "Not Applicable":
			continue
		abrev = topic_title[topic_title.find('(') + 1 : topic_title.find(')')]
		terms = [topic_title, abrev]		
		# Look for duplicates
		duplicate = False
		topic_key = None
		matched_with_space_agency = False
		for topic in sponsoring_space_agency_topics:
			if topic['title'] == topic_title:
				matched_with_space_agency = True
				topic_key = topic['_key']
		# Will be overwritten if duplicate
		for topic in sponsoring_space_organization_topics:
			if topic['title'] == topic_title:
				duplicate = True
				topic['sources'] = topic['sources'] + ', row ' + str(rowidx + 2)
				topic_key = topic['_key']

		# Make a new topic if not duplicate
		if (not duplicate and not matched_with_space_agency):

			topic_key = 'T' + str(topic_key_val)
			# Increment key value for next topic
			topic_key_val = topic_key_val + 1

			# (5) Create topic for sponsoring organization
			topic_json_struct = {}
			topic_json_struct['_key'] = topic_key
			topic_json_struct["_type"] = 'topic'
			topic_json_struct['title'] = topic_title
			topic_json_struct['definition'] = ''
			topic_json_struct['terms'] = terms
			topic_json_struct['sources'] = "Investigations, row " + str(rowidx + 2)

			sponsoring_space_organization_topics.append(topic_json_struct)

			# (6) Link sponsoring agency to cluster T30
			link_key = 'L' + str(link_key_val)
			# Increment key value for next link
			link_key_val = link_key_val + 1

			link_json_struct = {}
			link_json_struct['_key'] = link_key
			link_json_struct['_type'] = 'hasInstance'
			link_json_struct['name'] = ''
			link_json_struct['_from'] = 'T30' 
			link_json_struct['_to'] = topic_key

			sponsoring_space_organization_links.append(link_json_struct)

			# (6a) Check if links with NASA
			if ('NASA' in topic_title):
				link_key = 'L' + str(link_key_val)
				# Increment key value for next link
				link_key_val = link_key_val + 1

				link_json_struct = {}
				link_json_struct['_key'] = link_key
				link_json_struct['_type'] = 'is affiliated with'
				link_json_struct['name'] = ''
				link_json_struct['_from'] = nasa_key 
				link_json_struct['_to'] = topic_key

				sponsoring_space_organization_links.append(link_json_struct)

		if (matched_with_space_agency):
			# (5) Link sponsoring agency to cluster T30
			link_key = 'L' + str(link_key_val)
			# Increment key value for next link
			link_key_val = link_key_val + 1

			link_json_struct = {}
			link_json_struct['_key'] = link_key
			link_json_struct['_type'] = 'hasInstance'
			link_json_struct['name'] = ''
			link_json_struct['_from'] = 'T30' 
			link_json_struct['_to'] = topic_key

			sponsoring_space_organization_links.append(link_json_struct)

		else:
			# (7) Link between SponsoringAgency and investigation ID
			# Find corresponding topic in investigation_topics
			my_row = "row " + str(rowidx + 2) + ','
			my_row2 = "row " + str(rowidx + 2)
			temporary_topic_struct = {}
			for topic in investigation_topics:
				if my_row in topic['sources'] or topic['sources'].endswith(my_row2):
					temporary_topic_struct = topic
					break
			investigation_key = temporary_topic_struct['_key']

			link_key = 'L' + str(link_key_val)
			# Increment key value for next link
			link_key_val = link_key_val + 1

			# Output link to JSON format
			link_json_struct = {}
			link_json_struct['_key'] = link_key
			link_json_struct['_type'] = 'link'
			link_json_struct['name'] = 'sponsors'
			link_json_struct['definition'] = ''
			link_json_struct['_from'] = topic_key 
			link_json_struct['_to'] = investigation_key

			# Store in list to output at end
			sponsoring_space_organization_links.append(link_json_struct)

	# Post process to fix a broken character
	for topic in sponsoring_space_organization_topics:
		topic['title'] = topic['title'].replace('\u2013', '-')
		topic['terms'][0] = topic['terms'][0].replace('\u2013', '-')

	return sponsoring_space_organization_topics, sponsoring_space_organization_links, topic_key_val, link_key_val

def convert_principal_investigators(data, topic_key_val, link_key_val, investigation_topics):
	principal_investigator_topics = list()
	principal_investigator_links = list()

	# This dict will tell us if links are already going to be created. Keyed by (from, to), value doesn't matter
	duplicated_links_dict = dict()

	for rowidx in range(len(data)):
		# Get current row in dataset
		investigation_row = data.iloc[rowidx,:]
		pis_in_row = [(investigation_row['PI1-FN'], investigation_row['PI1-LN'], investigation_row['PI1-City'], investigation_row['PI1-State'], investigation_row['PI1-Country']),
		 			  (investigation_row['PI2-FN'], investigation_row['PI2-LN'], investigation_row['PI2-City'], investigation_row['PI2-State'], investigation_row['PI2-Country']),
		 			  (investigation_row['PI3-FN'], investigation_row['PI3-LN'], investigation_row['PI3-City'], investigation_row['PI3-State'], investigation_row['PI3-Country']),
		 			  (investigation_row['PI4-FN'], investigation_row['PI4-LN'], investigation_row['PI4-City'], investigation_row['PI4-State'], investigation_row['PI4-Country']),
		 			  (investigation_row['PI5-FN'], investigation_row['PI5-LN'], investigation_row['PI5-City'], investigation_row['PI5-State'], investigation_row['PI5-Country']),
		 			  (investigation_row['PI6-FN'], investigation_row['PI6-LN'], investigation_row['PI6-City'], investigation_row['PI6-State'], investigation_row['PI6-Country']),
		 			  (investigation_row['PI7-FN'], investigation_row['PI7-LN'], investigation_row['PI7-City'], investigation_row['PI7-State'], investigation_row['PI7-Country'])]
		for idx, pi in enumerate(pis_in_row):
			if(pi[0] == '' or pi[1] == ''): # No info for name, just skip this entry
				continue
			if(',' in pi[0]):
				name = pi[0][:pi[0].find(',')]
				first_name = name.split(" ")[0]
				last_name = name.split(" ")[1]
			else:
				first_name = pi[0]
				last_name = pi[1]
			topic_title = first_name + " " + last_name
			initials = first_name[0] + "." + last_name[0] + "."
			terms = [topic_title, last_name, initials]
			# (9) Create topic for this PI if doesn't already exist
			# Look for duplicates
			duplicate = False
			investigator_topic_key = None
			for topic in principal_investigator_topics:
				if topic['title'] == topic_title:
					duplicate = True
					topic['sources'] = topic['sources'] + ', row ' + str(rowidx + 2)
					investigator_topic_key = topic['_key']
			# Make a new topic if not duplicate
			if (not duplicate):

				investigator_topic_key = 'T' + str(topic_key_val)
				# Increment key value for next topic
				topic_key_val = topic_key_val + 1
				topic_json_struct = {}
				topic_json_struct['_key'] = investigator_topic_key
				topic_json_struct["_type"] = 'individual'
				topic_json_struct['title'] = first_name + " " + last_name
				topic_json_struct['firstName'] = first_name 
				topic_json_struct['lastName'] = last_name
				topic_json_struct['initials'] = initials
				topic_json_struct['terms'] = terms
				topic_json_struct['sources'] = "Investigations, row " + str(rowidx + 2)

				principal_investigator_topics.append(topic_json_struct)

				# (10) Link PI to cluster T31
				link_key = 'L' + str(link_key_val)
				# Increment key value for next link
				link_key_val = link_key_val + 1

				link_json_struct = {}
				link_json_struct['_key'] = link_key
				link_json_struct['_type'] = 'hasInstance'
				link_json_struct['name'] = ''
				link_json_struct['_from'] = 'T31' 
				link_json_struct['_to'] = investigator_topic_key

				principal_investigator_links.append(link_json_struct)
			# (11) Link between PI and investigation ID
			# Find corresponding topic in investigation_topics
			my_row = "row " + str(rowidx + 2) + ','
			my_row2 = "row " + str(rowidx + 2)
			temporary_topic_struct = {}
			for topic in investigation_topics:
				if my_row in topic['sources'] or topic['sources'].endswith(my_row2):
					temporary_topic_struct = topic
					break
			investigation_key = temporary_topic_struct['_key']

			link_key = 'L' + str(link_key_val)
			# Increment key value for next link
			link_key_val = link_key_val + 1

			definition = topic_title + " is the "
			if (idx == 0):
				definition += "first"
			elif (idx == 1):
				definition += "second"
			elif (idx == 2):
				definition += "third"
			elif (idx == 3):
				definition += "fourth"
			elif (idx == 4):
				definition += "fifth"
			elif (idx == 5):
				definition += "sixth"
			elif (idx == 6):
				definition += "seventh"
			definition += " person responsible for " + temporary_topic_struct['title']

			# Output link to JSON format
			link_json_struct = {}
			link_json_struct['_key'] = link_key
			link_json_struct['_type'] = 'link'
			link_json_struct['name'] = 'leads'
			link_json_struct['definition'] = definition
			link_json_struct['_from'] = investigator_topic_key 
			link_json_struct['_to'] = investigation_key

			# Store in list to output at end
			principal_investigator_links.append(link_json_struct)

			# (12) Create topic for city if not duplicate
			topic_title = pi[2]
			if (topic_title != ''):
				duplicate = False
				city_topic_key = None
				for topic in principal_investigator_topics:
					if topic['title'] == topic_title:
						duplicate = True
						if (', row ' + str(rowidx + 2) not in topic['sources']):
							topic['sources'] = topic['sources'] + ', row ' + str(rowidx + 2)
						city_topic_key = topic['_key']
				# Make a new topic if not duplicate
				if (not duplicate):
					city_topic_key = 'T' + str(topic_key_val)
					# Increment key value for next topic
					topic_key_val = topic_key_val + 1
					topic_json_struct = {}
					topic_json_struct['_key'] = city_topic_key
					topic_json_struct["_type"] = 'topic'
					topic_json_struct['title'] = topic_title
					topic_json_struct['terms'] = [topic_title]
					topic_json_struct['sources'] = "Investigations, row " + str(rowidx + 2)

					principal_investigator_topics.append(topic_json_struct)

					# (13) Link PI city to cluster T32
					link_key = 'L' + str(link_key_val)
					# Increment key value for next link
					link_key_val = link_key_val + 1

					link_json_struct = {}
					link_json_struct['_key'] = link_key
					link_json_struct['_type'] = 'hasInstance'
					link_json_struct['name'] = ''
					link_json_struct['_from'] = 'T32' 
					link_json_struct['_to'] = city_topic_key

					principal_investigator_links.append(link_json_struct)

				# (14) Link PI to city if link doesn't already exist
				if (duplicated_links_dict.get((investigator_topic_key, city_topic_key)) == None):
					link_key = 'L' + str(link_key_val)
					# Increment key value for next link
					link_key_val = link_key_val + 1

					link_json_struct = {}
					link_json_struct['_key'] = link_key
					link_json_struct['_type'] = 'link'
					link_json_struct['name'] = 'is located in'
					link_json_struct['_from'] = investigator_topic_key
					link_json_struct['_to'] = city_topic_key

					principal_investigator_links.append(link_json_struct)
					duplicated_links_dict[(investigator_topic_key, city_topic_key)] = 1

			# (15) Create topic for state if not duplicate
			topic_title = pi[3]
			if (topic_title != ""):
				duplicate = False
				state_topic_key = None
				for topic in principal_investigator_topics:
					if topic['title'] == topic_title:
						duplicate = True
						if (', row ' + str(rowidx + 2) not in topic['sources']):
							topic['sources'] = topic['sources'] + ', row ' + str(rowidx + 2)
						state_topic_key = topic['_key']
				# Make a new topic if not duplicate
				if (not duplicate):
					state_topic_key = 'T' + str(topic_key_val)
					# Increment key value for next topic
					topic_key_val = topic_key_val + 1
					topic_json_struct = {}
					topic_json_struct['_key'] = state_topic_key
					topic_json_struct["_type"] = 'topic'
					topic_json_struct['title'] = topic_title
					topic_json_struct['terms'] = [topic_title]
					topic_json_struct['sources'] = "Investigations, row " + str(rowidx + 2)

					principal_investigator_topics.append(topic_json_struct)

					# (16) Link PI state to cluster T33
					link_key = 'L' + str(link_key_val)
					# Increment key value for next link
					link_key_val = link_key_val + 1

					link_json_struct = {}
					link_json_struct['_key'] = link_key
					link_json_struct['_type'] = 'hasInstance'
					link_json_struct['name'] = ''
					link_json_struct['_from'] = 'T33' 
					link_json_struct['_to'] = state_topic_key

					principal_investigator_links.append(link_json_struct)

				# (17) Link city to state if link doesn't already exist
				if (duplicated_links_dict.get((city_topic_key, state_topic_key)) == None):
					link_key = 'L' + str(link_key_val)
					# Increment key value for next link
					link_key_val = link_key_val + 1

					link_json_struct = {}
					link_json_struct['_key'] = link_key
					link_json_struct['_type'] = 'link'
					link_json_struct['name'] = 'is located in'
					link_json_struct['_from'] = city_topic_key
					link_json_struct['_to'] = state_topic_key

					principal_investigator_links.append(link_json_struct)
					duplicated_links_dict[(city_topic_key, state_topic_key)] = 1
			# (18) Create topic for country if not duplicate
			topic_title = pi[4]
			if (topic_title != ""):
				duplicate = False
				country_topic_key = None
				for topic in principal_investigator_topics:
					if topic['title'] == topic_title:
						duplicate = True
						if (', row ' + str(rowidx + 2) not in topic['sources']):
							topic['sources'] = topic['sources'] + ', row ' + str(rowidx + 2)
						country_topic_key = topic['_key']
				# Make a new topic if not duplicate
				if (not duplicate):
					country_topic_key = 'T' + str(topic_key_val)
					# Increment key value for next topic
					topic_key_val = topic_key_val + 1
					topic_json_struct = {}
					topic_json_struct['_key'] = country_topic_key
					topic_json_struct["_type"] = 'topic'
					topic_json_struct['title'] = topic_title
					topic_json_struct['terms'] = [topic_title]
					topic_json_struct['sources'] = "Investigations, row " + str(rowidx + 2)

					principal_investigator_topics.append(topic_json_struct)

					# (19) Link PI country to cluster T34
					link_key = 'L' + str(link_key_val)
					# Increment key value for next link
					link_key_val = link_key_val + 1

					link_json_struct = {}
					link_json_struct['_key'] = link_key
					link_json_struct['_type'] = 'hasInstance'
					link_json_struct['name'] = ''
					link_json_struct['_from'] = 'T34' 
					link_json_struct['_to'] = country_topic_key

					principal_investigator_links.append(link_json_struct)
				if (pi[3] == ''):
					key_to_use = city_topic_key
				else:
					key_to_use = state_topic_key
				# (20) Link city/state to country if link doesn't already exist
				if (duplicated_links_dict.get((key_to_use, country_topic_key)) == None):
					link_key = 'L' + str(link_key_val)
					# Increment key value for next link
					link_key_val = link_key_val + 1

					link_json_struct = {}
					link_json_struct['_key'] = link_key
					link_json_struct['_type'] = 'link'
					link_json_struct['name'] = 'is located in'
					link_json_struct['_from'] = key_to_use
					link_json_struct['_to'] = country_topic_key

					principal_investigator_links.append(link_json_struct)
					duplicated_links_dict[(key_to_use, country_topic_key)] = 1
			
	return principal_investigator_topics, principal_investigator_links, topic_key_val, link_key_val

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

def main():
	# Create list of topics
	new_topics = list()
	new_links = list()

	# Load and clean the data
	iss_data = pd.read_csv("iss_data.csv")
	iss_data = iss_data.fillna('')

	wos_data = pd.concat([pd.read_csv("wos_data.csv"), pd.read_csv('wos_data2.csv')])
	wos_data = wos_data.fillna('')
	wos_data.drop_duplicates('DI')

	subcategory_topics, subcategory_links, topic_key_val, link_key_val = convert_clusters()
	print("Converting researchers")
	researcher_runner = Convert_Researchers()
	researcher_topics, researcher_links, topic_key_val, link_key_val = 	researcher_runner.convert_researchers(wos_data, topic_key_val, link_key_val)
	# new_topics = add_new_topics(new_topics, researcher_topics)
	# new_links = add_new_links(new_links, researcher_links)

	print("Converting publications")
	publication_runner = Convert_Publications()
	publication_topics, publication_links, topic_key_val, link_key_val = publication_runner.convert_publications(wos_data, topic_key_val, link_key_val)
	# new_topics = add_new_topics(new_topics, publication_topics)
	# new_links = add_new_links(new_links, publication_links)

	print("Converting journals")
	journal_runner = Convert_Journals()
	journal_topics, journal_links, topic_key_val, link_key_val = journal_runner.convert_journals(wos_data, topic_key_val, link_key_val, publication_topics)
	# new_topics = add_new_topics(new_topics, journal_topics)
	# new_links = add_new_links(new_links, journal_links)

	print("Converting articles")
	article_runner = Convert_Articles()
	article_topics, article_links, topic_key_val, link_key_val = article_runner.convert_articles(wos_data, topic_key_val, link_key_val, researcher_topics, publication_topics, journal_topics, journal_links)
	# new_topics = add_new_topics(new_topics, article_topics)
	# new_links = add_new_links(new_links, article_links)
	print("Running ISS")

	# ---- ISS ----
	# Step 1 - 3, 8, 21
	investigation_topics, investigation_links, topic_key_val, link_key_val = convert_investigations(iss_data, topic_key_val, link_key_val, subcategory_topics, article_topics)
	# Step 4
	sponsoring_space_agency_topics, sponsoring_space_agency_links, topic_key_val, link_key_val = convert_sponsoring_space_agencies(iss_data, topic_key_val, link_key_val, investigation_topics)
	# Step 5 - 7
	sponsoring_space_organization_topics, sponsoring_space_organization_links, topic_key_val, link_key_val = convert_sponsoring_space_organizations(iss_data, topic_key_val, link_key_val, investigation_topics, sponsoring_space_agency_topics)
	# Step 9 - 20
	principal_investigator_topics, principal_investigator_links, topic_key_val, link_key_val = convert_principal_investigators(iss_data, topic_key_val, link_key_val, investigation_topics)

	new_topics = investigation_topics + sponsoring_space_agency_topics + sponsoring_space_organization_topics + principal_investigator_topics
	new_links = investigation_links + sponsoring_space_agency_links + sponsoring_space_organization_links + principal_investigator_links

	# Output topics to file
	with open('output/iss_topics.json', 'w') as f:
		# There's probably a better way to output as a list of JSON objects
		f.write('[')
		i = 0
		for topic in new_topics:
			f.write(json.dumps(topic))
			if i != len(new_topics) - 1:
				f.write(",\n")
			else:
				f.write('\n')
			i = i + 1
		f.write(']')
	# Output links to file
	with open('output/iss_links.json', 'w') as f:
		f.write('[')
		i = 0
		for link in new_links:
			f.write(json.dumps(link))
			if i != len(new_topics) - 1:
				f.write(",\n")
			else:
				f.write('\n')
			i = i + 1
		f.write(']')
if __name__ == '__main__':
	main()