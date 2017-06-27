# -*- coding: utf-8 -*-

import json
import os
import codecs



def json_to_txt(list_of_json):
	
	for name_json in list_of_json:
		name_file = name_json.split('.')
		name_file = name_file[0]
		print name_file
		name_file = name_file+'.txt'

		newDocument = open(name_file,'a')
		test = open(name_json,'r')
#test = codecs.open('stranger-things.json',encoding='utf-8')
		lines = test.readlines()

		for line in lines:
			js = line
			a = json.loads(js)
			a = a['text']
			a = a.replace("\n"," ")
	#a = a.decode('unicode_escape').encode('ascii','ignore')
	#a = a.encode('ascii','ignore')
			a = a.encode('utf-8')
			#a = a.encode('ascii','ignore')
	#a = unicode(a,errors='ignore')
	#print a
	#a.encode("utf-8")
#js = lines[0]
#a =json.loads(js)
	#print a['text']
			newDocument.write(a + '\n')
	#print "yey"
		newDocument.close()
		test.close()	

#json_to_txt('daredevil.json')