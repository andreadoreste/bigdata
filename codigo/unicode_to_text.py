import os

newDoc = open('wordcount_v2\wordcount_stranger-things.txt','a')
oldDoc0 = open('mRstranger-things\part-00000','r')
oldDoc1 = open('mRstranger-things\part-00001','r')

list = oldDoc0.readlines()
l2 = oldDoc1.readlines()

#list.append(oldDoc1.readlines())
#list = list.replace(')(',');(')
newList = []
for i in list:

	i = eval(i)
	#i = i.partition(',')
	
	#word = i[0].encode('utf-8')
	word = i[0].encode('ascii','ignore')
	newDoc.write(word+','+str(i[1])+'\n')
	
for j in l2:

	j = eval(j)
	#word = j[0].encode('utf-8')
	word = j[0].encode('ascii','ignore')
	newDoc.write(word+','+str(j[1])+'\n')

newDoc.close()
oldDoc0.close()
oldDoc1.close()