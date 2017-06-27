from pyspark import SparkContext

sc = SparkContext(master='local[*]',appName='MyPySparkScript')

#Receber a lista com hashtags
urls = [ 'narcos', 'daredevil']
lnewFiles = ["mR"+url for url  in urls]

#Inicia varios processos para buscar os tweets
data = sc.parallelize(urls)
sc.addPyFile("examples\src\main\python\scrape_hashtags.py")
import scrape_hashtags
rdd = data.map(lambda x: (x, scrape_hashtags.ImportTweets(x))).collect()

#wordcount para cada serie
for i in urls:
	text_file = sc.textFile(i+".txt")
	counts = text_file.flatMap(lambda line: line.split(" ")) \
				.map(lambda word: (word, 1)) \
				.reduceByKey(lambda a, b: a + b)
	
	index = urls.index(i)
	counts.saveAsTextFile(lnewFiles[index])
