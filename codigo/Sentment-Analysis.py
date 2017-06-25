# -*- coding: utf-8 -*-
"""
Created on Sun May 28 17:10:08 2017

@author: Bruno Dias
"""

import nltk
from nltk.corpus import sentiwordnet as swn

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
    

#def analysis(sentence):
#    tokens = nltk.word_tokenize(sentence)
#    
#    pos = nltk.pos_tag(tokens)
#    
#    dic = {}
#    for i in range(len(pos)):
#        dic[pos[i][0]] = pos[i][1]
#        
#    return dic

#Transforma a Tag do NLTK para a tag do SentiWordNet
def transform(lista):
    lista[1] = "a"
    return lista

#Faz a análise de sentimentos e retorna a nota da série
def analysis(lista):
    nota = 0
    for tupla in lista:
        try:
            tmp = nltk.pos_tag([tupla[0]])[0]
            tmp = list(tmp)
            tmp = transform(tmp)
            try:
                sentiment = swn.senti_synset(tmp[0]+"."+tmp[1]+"."+"01")
                pos = sentiment.pos_score()
                neg = sentiment.neg_score()
                nota = nota + pos*tupla[1]
                nota = nota - neg*tupla[1]
            except:pass
        except:pass
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
    dic[analysis(dataSoue)] = "Soue"
    dic[analysis(dataStrangerThings)] = "Stranger Things"
    
    return dic

print(rank())