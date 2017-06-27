import scrape_hashtags

def BuscaParalelaSpark(listaSerie, sc):
   #Inicia varios processos para buscar os tweets
   data = sc.parallelize(listaSerie)
   sc.addPyFile("examples\src\main\python\scrape_hashtags.py")   
   rdd = data.map(lambda x: (x, scrape_hashtags.ImportTweets(x))).collect()
   
#wordcount para cada serie
def wordCount(listaSerie, sc):
    lnewFiles = ["mR"+nome for nome in listaSerie]
    for i in listaSerie:
		text_file = sc.textFile(i+".txt")
		counts = text_file.flatMap(lambda line: line.split(" ")) \
					.map(lambda word: (word, 1)) \
					.reduceByKey(lambda a, b: a + b)
		
		index = listaSerie.index(i)
		counts.saveAsTextFile(lnewFiles[index])

    