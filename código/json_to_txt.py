# -*- coding: utf-8 -*-

import json
import os
import codecs

newDocument = open('stranger-things_v2.txt','a')
test = open('stranger-things.json','r')
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
