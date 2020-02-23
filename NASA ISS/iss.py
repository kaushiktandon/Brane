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
	properties['title'] = "ISS investigation"
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
	properties['title'] = "Research organization"
	cluster_topics.append(create_topic(properties))
	# T23
	properties['_key'] = 'T23'
	properties['_type'] = 'cluster'
	properties['title'] = "Publisher"
	cluster_topics.append(create_topic(properties))
	# T24
	properties['_key'] = 'T24'
	properties['_type'] = 'cluster'
	properties['title'] = "Keyword"
	cluster_topics.append(create_topic(properties))
	# T25
	properties['_key'] = 'T25'
	properties['_type'] = 'cluster'
	properties['title'] = 'Tagged Keyword'
	cluster_topics.append(create_topic(properties))
	# T26
	properties['_key'] = 'T26'
	properties['_type'] = 'cluster'
	properties['title'] = 'Untagged Keyword'
	cluster_topics.append(create_topic(properties))
	# T27
	properties['_key'] = 'T27'
	properties['_type'] = 'cluster'
	properties['title'] = 'Investigation'
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
	properties['title'] = 'Biology and Biotechnology'
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
	properties['title'] = 'Cellular Biology'
	cluster_topics.append(create_topic(properties))
	# T43
	properties['_key'] = 'T43'
	properties['_type'] = 'cluster'
	properties['title'] = 'Macromolecular Crystal Growth'
	cluster_topics.append(create_topic(properties))
	# T44
	properties['_key'] = 'T44'
	properties['_type'] = 'cluster'
	properties['title'] = 'Microbiology'
	cluster_topics.append(create_topic(properties))
	# T45
	properties['_key'] = 'T45'
	properties['_type'] = 'cluster'
	properties['title'] = 'Microencapsulation'
	cluster_topics.append(create_topic(properties))
	# T46
	properties['_key'] = 'T46'
	properties['_type'] = 'cluster'
	properties['title'] = 'Plant Biology'
	cluster_topics.append(create_topic(properties))
	# T47
	properties['_key'] = 'T47'
	properties['_type'] = 'cluster'
	properties['title'] = 'Vaccine Development'
	cluster_topics.append(create_topic(properties))
	# T48
	properties['_key'] = 'T48'
	properties['_type'] = 'cluster'
	properties['title'] = 'Earth and Space Science'
	cluster_topics.append(create_topic(properties))
	# T49
	properties['_key'] = 'T49'
	properties['_type'] = 'cluster'
	properties['title'] = 'Astrobiology'
	cluster_topics.append(create_topic(properties))
	# T50
	properties['_key'] = 'T50'
	properties['_type'] = 'cluster'
	properties['title'] = 'Astrophysics'
	cluster_topics.append(create_topic(properties))
	# T51
	properties['_key'] = 'T51'
	properties['_type'] = 'cluster'
	properties['title'] = 'Earth Remote Sensing'
	cluster_topics.append(create_topic(properties))
	# T52
	properties['_key'] = 'T52'
	properties['_type'] = 'cluster'
	properties['title'] = 'Heliophysics'
	cluster_topics.append(create_topic(properties))
	# T53
	properties['_key'] = 'T53'
	properties['_type'] = 'cluster'
	properties['title'] = 'Educational and cultural activities'
	cluster_topics.append(create_topic(properties))
	# T54
	properties['_key'] = 'T54'
	properties['_type'] = 'cluster'
	properties['title'] = 'Classroom Versions of ISS Investigations'
	cluster_topics.append(create_topic(properties))
	# T55
	properties['_key'] = 'T55'
	properties['_type'] = 'cluster'
	properties['title'] = 'Educational Competitions'
	cluster_topics.append(create_topic(properties))
	# T56
	properties['_key'] = 'T56'
	properties['_type'] = 'cluster'
	properties['title'] = 'Educational Demonstrations'
	cluster_topics.append(create_topic(properties))
	# T57
	properties['_key'] = 'T57'
	properties['_type'] = 'cluster'
	properties['title'] = 'Student-Developed Investigations'
	cluster_topics.append(create_topic(properties))
	# T58
	properties['_key'] = 'T58'
	properties['_type'] = 'cluster'
	properties['title'] = 'Human Research'
	cluster_topics.append(create_topic(properties))
	# T59
	properties['_key'] = 'T59'
	properties['_type'] = 'cluster'
	properties['title'] = 'Bone and Muscle Physiology'
	cluster_topics.append(create_topic(properties))
	# T60
	properties['_key'] = 'T60'
	properties['_type'] = 'cluster'
	properties['title'] = 'Cardiovascular and Respiratory Systems'
	cluster_topics.append(create_topic(properties))
	# T61
	properties['_key'] = 'T61'
	properties['_type'] = 'cluster'
	properties['title'] = 'Crew Healthcare Systems'
	cluster_topics.append(create_topic(properties))
	# T62
	properties['_key'] = 'T62'
	properties['_type'] = 'cluster'
	properties['title'] = 'Habitability and Human Factors'
	cluster_topics.append(create_topic(properties))
	# T63
	properties['_key'] = 'T63'
	properties['_type'] = 'cluster'
	properties['title'] = 'Human Behavior and Performance'
	cluster_topics.append(create_topic(properties))
	# T64
	properties['_key'] = 'T64'
	properties['_type'] = 'cluster'
	properties['title'] = 'Human Microbiome'
	cluster_topics.append(create_topic(properties))
	# T65
	properties['_key'] = 'T65'
	properties['_type'] = 'cluster'
	properties['title'] = 'Immune System'
	cluster_topics.append(create_topic(properties))
	# T66
	properties['_key'] = 'T66'
	properties['_type'] = 'cluster'
	properties['title'] = 'Integrated Physiology and Nutrition'
	cluster_topics.append(create_topic(properties))
	# T67
	properties['_key'] = 'T67'
	properties['_type'] = 'cluster'
	properties['title'] = 'Nervous and Vestibular Systems'
	cluster_topics.append(create_topic(properties))
	# T68
	properties['_key'] = 'T68'
	properties['_type'] = 'cluster'
	properties['title'] = 'Radiation Impacts on Humans'
	cluster_topics.append(create_topic(properties))
	# T69
	properties['_key'] = 'T69'
	properties['_type'] = 'cluster'
	properties['title'] = 'Vision'
	cluster_topics.append(create_topic(properties))
	# T70
	properties['_key'] = 'T70'
	properties['_type'] = 'cluster'
	properties['title'] = 'Physical science'
	cluster_topics.append(create_topic(properties))
	# T71
	properties['_key'] = 'T71'
	properties['_type'] = 'cluster'
	properties['title'] = 'Combustion Science'
	cluster_topics.append(create_topic(properties))
	# T72
	properties['_key'] = 'T72'
	properties['_type'] = 'cluster'
	properties['title'] = 'Complex Fluids'
	cluster_topics.append(create_topic(properties))
	# T73
	properties['_key'] = 'T73'
	properties['_type'] = 'cluster'
	properties['title'] = 'Fluid Physics'
	cluster_topics.append(create_topic(properties))
	# T74
	properties['_key'] = 'T74'
	properties['_type'] = 'cluster'
	properties['title'] = 'Fundamental Physics'
	cluster_topics.append(create_topic(properties))
	# T75
	properties['_key'] = 'T75'
	properties['_type'] = 'cluster'
	properties['title'] = 'Materials Science'
	cluster_topics.append(create_topic(properties))
	# T76
	properties['_key'] = 'T76'
	properties['_type'] = 'cluster'
	properties['title'] = 'Technology Development and Demonstration'
	cluster_topics.append(create_topic(properties))
	# T77
	properties['_key'] = 'T77'
	properties['_type'] = 'cluster'
	properties['title'] = 'Air, Water and Surface Monitoring'
	cluster_topics.append(create_topic(properties))
	# T78
	properties['_key'] = 'T78'
	properties['_type'] = 'cluster'
	properties['title'] = 'Avionics and Software'
	cluster_topics.append(create_topic(properties))
	# T79
	properties['_key'] = 'T79'
	properties['_type'] = 'cluster'
	properties['title'] = 'Characterizing Experiment Hardware'
	cluster_topics.append(create_topic(properties))
	# T80
	properties['_key'] = 'T80'
	properties['_type'] = 'cluster'
	properties['title'] = 'Commercial Demonstrations'
	cluster_topics.append(create_topic(properties))
	# T81
	properties['_key'] = 'T81'
	properties['_type'] = 'cluster'
	properties['title'] = 'Communication and Navigation'
	cluster_topics.append(create_topic(properties))
	# T82
	properties['_key'] = 'T82'
	properties['_type'] = 'cluster'
	properties['title'] = 'Fire Suppression and Detection'
	cluster_topics.append(create_topic(properties))
	# T83
	properties['_key'] = 'T83'
	properties['_type'] = 'cluster'
	properties['title'] = 'Food and Clothing Systems'
	cluster_topics.append(create_topic(properties))
	# T84
	properties['_key'] = 'T84'
	properties['_type'] = 'cluster'
	properties['title'] = 'Imaging Technology'
	cluster_topics.append(create_topic(properties))
	# T85
	properties['_key'] = 'T85'
	properties['_type'] = 'cluster'
	properties['title'] = 'Life Support Systems and Habitation'
	cluster_topics.append(create_topic(properties))
	# T86
	properties['_key'] = 'T86'
	properties['_type'] = 'cluster'
	properties['title'] = 'Microbial Populations in Spacecraft'
	cluster_topics.append(create_topic(properties))
	# T87
	properties['_key'] = 'T87'
	properties['_type'] = 'cluster'
	properties['title'] = 'Microgravity Environment Measurement'
	cluster_topics.append(create_topic(properties))
	# T88
	properties['_key'] = 'T88'
	properties['_type'] = 'cluster'
	properties['title'] = 'Radiation Measurements and Shielding'
	cluster_topics.append(create_topic(properties))
	# T89
	properties['_key'] = 'T89'
	properties['_type'] = 'cluster'
	properties['title'] = 'Repair and Fabrication Technologies'
	cluster_topics.append(create_topic(properties))
	# T90
	properties['_key'] = 'T90'
	properties['_type'] = 'cluster'
	properties['title'] = 'Robotics'
	cluster_topics.append(create_topic(properties))
	# T91
	properties['_key'] = 'T91'
	properties['_type'] = 'cluster'
	properties['title'] = 'Small Satellites and Control Technologies'
	cluster_topics.append(create_topic(properties))
	# T92
	properties['_key'] = 'T92'
	properties['_type'] = 'cluster'
	properties['title'] = 'Space Structures'
	cluster_topics.append(create_topic(properties))
	# T93
	properties['_key'] = 'T93'
	properties['_type'] = 'cluster'
	properties['title'] = 'Spacecraft and Orbital Environments'
	cluster_topics.append(create_topic(properties))
	# T94
	properties['_key'] = 'T94'
	properties['_type'] = 'cluster'
	properties['title'] = 'Spacecraft Materials'
	cluster_topics.append(create_topic(properties))
	# T95
	properties['_key'] = 'T95'
	properties['_type'] = 'cluster'
	properties['title'] = 'Thermal Management Systems'
	cluster_topics.append(create_topic(properties))
	# T96
	properties['_key'] = 'T96'
	properties['_type'] = 'cluster'
	properties['title'] = 'Wordnet tag'
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
	# L25	
	properties['_key'] = 'L25'
	properties['_type'] = 'encompasses'
	properties['_from'] = 'T1'
	properties['_to'] = 'T38'
	cluster_links.append(create_link(properties))
	# L26	
	properties['_key'] = 'L26'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T38'
	properties['_to'] = 'T39'
	cluster_links.append(create_link(properties))
	# L27	
	properties['_key'] = 'L27'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T38'
	properties['_to'] = 'T48'
	cluster_links.append(create_link(properties))
	# L28	
	properties['_key'] = 'L28'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T38'
	properties['_to'] = 'T53'
	cluster_links.append(create_link(properties))
	# L29	
	properties['_key'] = 'L29'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T38'
	properties['_to'] = 'T58'
	cluster_links.append(create_link(properties))
	# L30	
	properties['_key'] = 'L30'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T38'
	properties['_to'] = 'T70'
	cluster_links.append(create_link(properties))
	# L31	
	properties['_key'] = 'L31'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T38'
	properties['_to'] = 'T76'
	cluster_links.append(create_link(properties))
	# L32	
	properties['_key'] = 'L32'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T39'
	properties['_to'] = 'T40'
	cluster_links.append(create_link(properties))
	# L33	
	properties['_key'] = 'L33'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T39'
	properties['_to'] = 'T41'
	cluster_links.append(create_link(properties))
	# L34	
	properties['_key'] = 'L34'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T39'
	properties['_to'] = 'T42'
	cluster_links.append(create_link(properties))
	# L35	
	properties['_key'] = 'L35'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T39'
	properties['_to'] = 'T43'
	cluster_links.append(create_link(properties))
	# L36	
	properties['_key'] = 'L36'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T39'
	properties['_to'] = 'T44'
	cluster_links.append(create_link(properties))
	# L37	
	properties['_key'] = 'L37'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T39'
	properties['_to'] = 'T45'
	cluster_links.append(create_link(properties))
	# L38	
	properties['_key'] = 'L38'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T39'
	properties['_to'] = 'T46'
	cluster_links.append(create_link(properties))
	# L39	
	properties['_key'] = 'L39'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T39'
	properties['_to'] = 'T47'
	cluster_links.append(create_link(properties))
	# L40	
	properties['_key'] = 'L40'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T48'
	properties['_to'] = 'T49'
	cluster_links.append(create_link(properties))
	# L41	
	properties['_key'] = 'L41'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T48'
	properties['_to'] = 'T50'
	cluster_links.append(create_link(properties))
	# L42	
	properties['_key'] = 'L42'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T48'
	properties['_to'] = 'T51'
	cluster_links.append(create_link(properties))
	# L43	
	properties['_key'] = 'L43'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T48'
	properties['_to'] = 'T52'
	cluster_links.append(create_link(properties))
	# L44	
	properties['_key'] = 'L44'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T53'
	properties['_to'] = 'T54'
	cluster_links.append(create_link(properties))
	# L45	
	properties['_key'] = 'L45'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T53'
	properties['_to'] = 'T55'
	cluster_links.append(create_link(properties))
	# L46	
	properties['_key'] = 'L46'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T53'
	properties['_to'] = 'T56'
	cluster_links.append(create_link(properties))
	# L47	
	properties['_key'] = 'L47'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T53'
	properties['_to'] = 'T57'
	cluster_links.append(create_link(properties))
	# L48	
	properties['_key'] = 'L48'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T58'
	properties['_to'] = 'T59'
	cluster_links.append(create_link(properties))
	# L49	
	properties['_key'] = 'L49'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T58'
	properties['_to'] = 'T60'
	cluster_links.append(create_link(properties))
	# L50	
	properties['_key'] = 'L50'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T58'
	properties['_to'] = 'T61'
	cluster_links.append(create_link(properties))
	# L51	
	properties['_key'] = 'L51'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T58'
	properties['_to'] = 'T62'
	cluster_links.append(create_link(properties))
	# L52	
	properties['_key'] = 'L52'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T58'
	properties['_to'] = 'T63'
	cluster_links.append(create_link(properties))
	# L53	
	properties['_key'] = 'L53'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T58'
	properties['_to'] = 'T64'
	cluster_links.append(create_link(properties))
	# L54	
	properties['_key'] = 'L54'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T58'
	properties['_to'] = 'T65'
	cluster_links.append(create_link(properties))
	# L55	
	properties['_key'] = 'L55'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T58'
	properties['_to'] = 'T66'
	cluster_links.append(create_link(properties))
	# L56	
	properties['_key'] = 'L56'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T58'
	properties['_to'] = 'T67'
	cluster_links.append(create_link(properties))
	# L57	
	properties['_key'] = 'L57'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T58'
	properties['_to'] = 'T68'
	cluster_links.append(create_link(properties))
	# L58	
	properties['_key'] = 'L58'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T58'
	properties['_to'] = 'T69'
	cluster_links.append(create_link(properties))
	# L59	
	properties['_key'] = 'L59'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T70'
	properties['_to'] = 'T71'
	cluster_links.append(create_link(properties))
	# L60	
	properties['_key'] = 'L60'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T70'
	properties['_to'] = 'T72'
	cluster_links.append(create_link(properties))
	# L61	
	properties['_key'] = 'L61'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T70'
	properties['_to'] = 'T73'
	cluster_links.append(create_link(properties))
	# L62	
	properties['_key'] = 'L62'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T70'
	properties['_to'] = 'T74'
	cluster_links.append(create_link(properties))
	# L63	
	properties['_key'] = 'L63'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T70'
	properties['_to'] = 'T75'
	cluster_links.append(create_link(properties))
	# L64	
	properties['_key'] = 'L64'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T76'
	properties['_to'] = 'T77'
	cluster_links.append(create_link(properties))
	# L65	
	properties['_key'] = 'L65'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T76'
	properties['_to'] = 'T78'
	cluster_links.append(create_link(properties))
	# L66	
	properties['_key'] = 'L66'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T76'
	properties['_to'] = 'T79'
	cluster_links.append(create_link(properties))
	# L67	
	properties['_key'] = 'L67'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T76'
	properties['_to'] = 'T80'
	cluster_links.append(create_link(properties))
	# L68	
	properties['_key'] = 'L68'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T76'
	properties['_to'] = 'T81'
	cluster_links.append(create_link(properties))
	# L69	
	properties['_key'] = 'L69'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T76'
	properties['_to'] = 'T82'
	cluster_links.append(create_link(properties))
	# L70	
	properties['_key'] = 'L70'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T76'
	properties['_to'] = 'T83'
	cluster_links.append(create_link(properties))
	# L71	
	properties['_key'] = 'L71'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T76'
	properties['_to'] = 'T84'
	cluster_links.append(create_link(properties))
	# L72	
	properties['_key'] = 'L72'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T76'
	properties['_to'] = 'T85'
	cluster_links.append(create_link(properties))
	# L73	
	properties['_key'] = 'L73'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T76'
	properties['_to'] = 'T86'
	cluster_links.append(create_link(properties))
	# L74	
	properties['_key'] = 'L74'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T76'
	properties['_to'] = 'T87'
	cluster_links.append(create_link(properties))
	# L75	
	properties['_key'] = 'L75'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T76'
	properties['_to'] = 'T88'
	cluster_links.append(create_link(properties))
	# L76	
	properties['_key'] = 'L76'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T76'
	properties['_to'] = 'T89'
	cluster_links.append(create_link(properties))
	# L77	
	properties['_key'] = 'L77'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T76'
	properties['_to'] = 'T90'
	cluster_links.append(create_link(properties))
	# L78	
	properties['_key'] = 'L78'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T76'
	properties['_to'] = 'T91'
	cluster_links.append(create_link(properties))
	# L79	
	properties['_key'] = 'L79'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T76'
	properties['_to'] = 'T92'
	cluster_links.append(create_link(properties))
	# L80	
	properties['_key'] = 'L80'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T76'
	properties['_to'] = 'T93'
	cluster_links.append(create_link(properties))
	# L81	
	properties['_key'] = 'L81'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T76'
	properties['_to'] = 'T94'
	cluster_links.append(create_link(properties))
	# L82	
	properties['_key'] = 'L82'
	properties['_type'] = 'categorizes'
	properties['_from'] = 'T76'
	properties['_to'] = 'T95'
	cluster_links.append(create_link(properties))
	# L83	
	properties['_key'] = 'L83'
	properties['_type'] = 'hasSubclass'
	properties['_from'] = 'T1'
	properties['_to'] = 'T96'
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

def convert_investigations(data, topic_key_val, link_key_val, subcategory_topics):
	investigation_topics = list()
	investigation_links = list()
	for rowidx in range(len(data)):
		# Get current row in dataset
		investigation_row = data.iloc[rowidx,:]
		_type = "topic"
		topic_title = investigation_row['Name']
		definition = topic_title + " - PAO Summary"
		terms = [topic_title, "PAO Summary"]
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
		for subcategory_topic_json in subcategory_topics:
			if subcategory_topic_json['title'] == investigation_row['Subcategory']:
				found = True
				subcategory_id = subcategory_topic_json['_key']
		if found:
			link_key = 'L' + str(link_key_val)
			# Increment key value for next link
			link_key_val = link_key_val + 1

			link_json_struct = {}
			link_json_struct['_key'] = link_key
			link_json_struct['_type'] = 'categorizes'
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

def convert_sponsoring_space_organizations(data, topic_key_val, link_key_val, investigation_topics):
	sponsoring_space_organization_topics = list()
	sponsoring_space_organization_links = list()
	for rowidx in range(len(data)):
		# Get current row in dataset
		agency_row = data.iloc[rowidx,:]
		topic_title = agency_row['SponsoringOrganization']
		abrev = topic_title[topic_title.find('(') + 1 : topic_title.find(')')]
		terms = [topic_title, abrev]		
		# Look for duplicates
		duplicate = False
		topic_key = None
		for topic in sponsoring_space_organization_topics:
			if topic['title'] == topic_title:
				duplicate = True
				topic['sources'] = topic['sources'] + ', row ' + str(rowidx + 2)
				topic_key = topic['_key']
		# Make a new topic if not duplicate
		if (not duplicate):

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
	for rowidx in range(len(data)):
		# Get current row in dataset
		investigation_row = data.iloc[rowidx,:]
		pis_in_row = [(investigation_row['PI1-FN'], investigation_row['PI1-LN']), (investigation_row['PI2-FN'], investigation_row['PI2-LN']), (investigation_row['PI3-FN'], investigation_row['PI3-LN']), (investigation_row['PI4-FN'], investigation_row['PI4-LN']), (investigation_row['PI5-FN'], investigation_row['PI5-LN']), (investigation_row['PI6-FN'], investigation_row['PI6-LN']), (investigation_row['PI7-FN'], investigation_row['PI7-LN'])]
		for idx, pi in enumerate(pis_in_row):
			if(pi[0] == '' or pi[1] == ''):
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
			topic_key = None
			for topic in principal_investigator_topics:
				if topic['title'] == topic_title:
					duplicate = True
					topic['sources'] = topic['sources'] + ', row ' + str(rowidx + 2)
					topic_key = topic['_key']
			# Make a new topic if not duplicate
			if (not duplicate):

				topic_key = 'T' + str(topic_key_val)
				# Increment key value for next topic
				topic_key_val = topic_key_val + 1
				topic_json_struct = {}
				topic_json_struct['_key'] = topic_key
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
				link_json_struct['_to'] = topic_key

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
			link_json_struct['_from'] = topic_key 
			link_json_struct['_to'] = investigation_key

			# Store in list to output at end
			principal_investigator_links.append(link_json_struct)

	return principal_investigator_topics, principal_investigator_links, topic_key_val, link_key_val

def main():
	# Create list of topics
	new_topics = list()
	new_links = list()

	# Load and clean the data
	data = pd.read_csv("iss_data.csv")
	data = data.fillna('')

	subcategory_topics, subcategory_links, topic_key_val, link_key_val = convert_clusters()
	# Step 1 - 3, 8
	investigation_topics, investigation_links, topic_key_val, link_key_val = convert_investigations(data, topic_key_val, link_key_val, subcategory_topics)
	# Step 4
	sponsoring_space_agency_topics, sponsoring_space_agency_links, topic_key_val, link_key_val = convert_sponsoring_space_agencies(data, topic_key_val, link_key_val, investigation_topics)
	# Step 5 - 7
	sponsoring_space_organization_topics, sponsoring_space_organization_links, topic_key_val, link_key_val = convert_sponsoring_space_organizations(data, topic_key_val, link_key_val, investigation_topics)

	principal_investigator_topics, principal_investigator_links, topic_key_val, link_key_val = convert_principal_investigators(data, topic_key_val, link_key_val, investigation_topics)

	new_topics = subcategory_topics + investigation_topics + sponsoring_space_agency_topics + sponsoring_space_organization_topics + principal_investigator_topics
	new_links = subcategory_links + investigation_links + sponsoring_space_agency_links + sponsoring_space_organization_links + principal_investigator_links

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