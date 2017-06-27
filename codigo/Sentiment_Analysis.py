# -*- coding: utf-8 -*-
"""
Created on Sun May 28 17:10:08 2017

@author: Bruno Dias
"""

import nltk
from nltk.corpus import sentiwordnet as swn

def analiseCompleta(filename):
    nota = analysis(getData("wordcount_"+filename+".txt"))
    file = open("rank.txt", "a+")
    file.write(filename + ":" + str(nota) + "\n")
    file.close()
            
#Retorna lista de tuplas com palavras e count delas dos arquivos txt
def getData(filename):
    result = []
    with open(filename, "r") as fp:
        for i in fp.readlines():
            tmp = i.split(",")
            try:
                result.append((tmp[0], int(tmp[1])))
                #result.append((eval(tmp[0]), eval(tmp[1])))
            except:pass
    fp.close()
    return result
    

#Transforma a Tag do NLTK para a tag do SentiWordNet
def transform(lista):
    if(lista[1] == "CC" or lista[1] == "CD" or lista[1] == "IN" or lista[1] == "NN" or lista[1] == "NNP" or lista[1] == "NNPS" or lista[1] == "NNS" or lista[1] == "PDT" or lista[1] == "PRP" or lista[1] == "PRP$" or lista[1] == "TO" or lista[1] == "UH" or lista[1] == "WP" or lista[1] == "WP$"):
        lista[1] = "n"
    if(lista[1] == "MD" or lista[1] == "VB" or lista[1] == "VBD" or lista[1] == "VBG" or lista[1] == "VBN" or lista[1] == "VBP" or lista[1] == "VBZ"):
        lista[1] = "v"
    if(lista[1] == "JJ" or lista[1] == "JJR" or lista[1] == "JJS"):
        lista[1] = "a"
    if(lista[1] == "DT" or lista[1] == "EX" or lista[1] == "RB" or lista[1] == "RBR" or lista[1] == "RBS" or lista[1] == "WDT" or lista[1] == "WRB" or lista[1] == "RP"):
        lista[1] = "r"
    return lista

#Faz a análise de sentimentos e retorna a nota da série
def analysis(lista):
    nota = 0
    for tupla in lista:
        try:
            print(tupla)
            tmp = nltk.pos_tag([tupla[0]])[0]
            print(tmp)
            tmp = list(tmp)
            print(tmp)
            tmp = transform(tmp)
            try:
                sentiment = swn.senti_synset(tmp[0]+"."+tmp[1]+"."+"01")
                pos = sentiment.pos_score()
                neg = sentiment.neg_score()
                nota = nota + pos*tupla[1]
                nota = nota - neg*tupla[1]
            except Exception, e:
                print(str(e))
                pass
        except Exception, e: 
            print(str(e))
            pass
    print(nota)
    return nota


#Ranqueia as séries
def rank():
    data13ReasonsWhy = getData("wordcount_13reasonsWhy_v2.txt")
    dataDaredevil = getData("wordcount_daredevil_v2.txt")
    dataHouseOfCards = getData("wordcount_house-of-cards_v2.txt")
    dataMasterOfNone = getData("wordcount_master-of-none_v2.txt")
    dataOrangeIsTheNewBlack = getData("wordcount_orange-is-the-new-black_v2.txt")
    dataSense8 = getData("wordcount_sense8_v2.txt")
    dataSoue = getData("wordcount_soue_v2.txt")
    dataStrangerThings = getData("wordcount_stranger-things_v2.txt")
    
    dic= {}
    dic[analysis(data13ReasonsWhy)] = "13 Reasons Why"
    dic[analysis(dataDaredevil)] = "Daredevil"
    dic[analysis(dataHouseOfCards)] = "House of Cards"
    dic[analysis(dataMasterOfNone)] = "Master of None"
    dic[analysis(dataOrangeIsTheNewBlack)] = "Orange Is The New Black"
    dic[analysis(dataSense8)] = "Sense 8"
    dic[analysis(dataSoue)] = "A Series of Unfortunate Events"
    dic[analysis(dataStrangerThings)] = "Stranger Things"
    
    return dic

#print(rank())

#ranked = rank()

#for keys,values in ranked.items():
#    print(values, keys)

# from pyspark import SparkContext
# data = getData("wordcount_13reasonswhy_v2.txt")
# sc = SparkContext(master='local[*]',appName='MyPySparkScript')
# rdd = sc.parallelize(data)
# rdd2 = rdd.map(lambda x: analysis(x))
# rdd3 = rdd.map( analysis )
# print(rdd2)
# print(rdd3)

#rdd2.take(10).foreach(println)
#rdd3.take(10).foreach(println)

#rdd2.take(10).foreach(print)
#rdd3.take(10).foreach(print)

#rdd2 = rdd2.collect()
#rdd3 = rdd3.collect()
#print(rdd2)
#print(rdd3)
