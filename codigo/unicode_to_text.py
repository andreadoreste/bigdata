# -*- coding: utf-8 -*-

import os

#newDoc = open('wordcount_v2\wordcount_stranger-things.txt','a')
#oldDoc0 = open('mRstranger-things\part-00000','r')
#oldDoc1 = open('mRstranger-things\part-00001','r')

def unicode_to_txt(name):
	name_new_doc = name.split('.')
	name_new_doc = name_new_doc[0]
	name_new_doc = 'wordcount_' + name_new_doc + '.txt'
	newDoc = open(name_new_doc,'a')

	oldDoc = open(name,'r')

	l = oldDoc.readlines()
#l2 = oldDoc1.readlines()

#list.append(oldDoc1.readlines())
#list = list.replace(')(',');(')
	newList = []
	for i in l:

		i = eval(i)
	#i = i.partition(',')
	
	#word = i[0].encode('utf-8')
		word = i[0].encode('ascii','ignore')
		newDoc.write(word+','+str(i[1])+'\n')
	'''	
	for j in l2:

		j = eval(j)
		#word = j[0].encode('utf-8')
		word = j[0].encode('ascii','ignore')
		newDoc.write(word+','+str(j[1])+'\n')
	'''
	newDoc.close()
	oldDoc.close()
#oldDoc1.close()

unicode_to_txt('part-00000')