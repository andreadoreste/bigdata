


from pyspark import SparkContext

sc = SparkContext(master='local[*]',appName='MyPySparkScript')
lista = ['house-of-cards.txt','master-of-none.txt','orange-is-the-new-black.txt','sense8.txt','soue.txt','stranger-things.txt']
lnewFiles = ['mRhouse-of-cards','mRmaster-of-none','mRorange-is-the-new-black','mRsense8','mRsoue','mRstranger-things']

for i in lista:

	text_file = sc.textFile(i)
	counts = text_file.flatMap(lambda line: line.split(" ")) \
				.map(lambda word: (word, 1)) \
				.reduceByKey(lambda a, b: a + b)
	
	index = lista.index(i)
	counts.saveAsTextFile(lnewFiles[index])
