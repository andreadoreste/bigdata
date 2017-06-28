# -*- coding: utf-8 -*-
from pyspark import SparkContext
from Tkinter import *
import spark_wordcount
import json_to_txt
import unicode_to_text
import Sentiment_Analysis

class window_research:
    def __init__(self,root):
        self.sc = SparkContext(master='local[*]',appName='MyPySparkScript')
        #self.texts = [self.text_1, self.text_2, self.text_3,self.text_4,self.text_5,self.text_6,self.text_7,self.text_8,self.text_9,self.text_10]

        self.root = root
        
        self.title = Label(root, text="Rankflix")
        self.title.grid(row=0)

        self.title = Label(root, text= "O que você deseja ranquear?")
        self.title.grid(row=1)

        #Campo 1
        self.label_1 = Label(root, text = "#")
        self.label_1.grid(row=2, column=0)

        self.text_1 = Entry(root)
        self.text_1.bind('<FocusIn>', lambda event: self.new_op(event,1))
        self.text_1.grid(row=2, column=1)

        #Campo 2
        self.label_2 = Label(root, text = "#")
        #self.label_2.grid(row=3, column=0)

        self.text_2 = Entry(root)
        self.text_2.bind('<FocusIn>',lambda event: self.new_op(event,2))
        #self.text_2.grid(row=3, column=1)

        #Campo 3
        self.label_3 = Label(root, text = "#")
        #self.label_3.grid(row=4, column=0)

        self.text_3 = Entry(root)

        self.text_3.bind('<FocusIn>',lambda event: self.new_op(event,3))

        #self.text_3.grid(row=4, column=1)

        #Opcionais
        #Campo 4
        self.label_4 = Label(root, text = "#")
        
        self.text_4 = Entry(root)
        self.text_4.bind('<FocusIn>',lambda event: self.new_op(event,4))

        #Campo 5
        self.label_5 = Label(root, text = "#")
                
        self.text_5 = Entry(root)
        self.text_5.bind('<FocusIn>',lambda event: self.new_op(event,5))

        #Campo 6
        self.label_6 = Label(root, text = "#")
        
        self.text_6 = Entry(root)
        self.text_6.bind('<FocusIn>',lambda event: self.new_op(event,6))

        #Campo 7
        self.label_7 = Label(root, text = "#")
        
        self.text_7 = Entry(root)
        self.text_7.bind('<FocusIn>',lambda event: self.new_op(event,7))

        #Campo 8
        self.label_8 = Label(root, text = "#")
        
        self.text_8 = Entry(root)
        self.text_8.bind('<FocusIn>',lambda event: self.new_op(event,8))

        #Campo 9
        self.label_9 = Label(root, text = "#")
        
        self.text_9 = Entry(root)
        self.text_9.bind('<FocusIn>',lambda event: self.new_op(event,9))

        #Campo 10
        self.label_10 = Label(root, text = "#")
        
        self.text_10 = Entry(root)
        #self.text_10.bind('<FocusIn>',lambda event: self.new_op(event,10))

        #Botão Pesquisar
        self.search = Button(root, text="GO!")
        self.search.bind("<Button-1>",self.pesquisar) 
        #p = self.search
        #p.grid(row=12)
        self.search.grid(row=12)
    
    def ok(self,event):
        if(self.text_1.get()):
            print self.text_1.get()
        print self.text_2.get()
        print self.text_3.get()

    def teste(self,event,v):
        print "work!"
        #print event.widget.get()
        print v

    def new_op(self, event, v):
        dic = {1: [self.label_2,self.text_2], 2: [self.label_3,self.text_3],3: [self.label_4,self.text_4], 4: [self.label_5,self.text_5],
               5: [self.label_6,self.text_6], 6: [self.label_7,self.text_7], 7: [self.label_8,self.text_8], 8: [self.label_9,self.text_9],
               9: [self.label_10,self.text_10]}
        
        print self.label_3
        l = dic[v][0]
        t = dic[v][1]
        print l
        r = v+2
        print r
        #self.label_4.grid(row=5, column=0)
        l.grid(row=r,column=0)
        #l.grid(row=r,column=0)
        t.grid(row=r, column=1)

        #self.value = 
    def pesquisar(self,event):
        words = []
        self.texts = [self.text_1, self.text_2, self.text_3,self.text_4,self.text_5,self.text_6,self.text_7,self.text_8,self.text_9,self.text_10]

        for i in self.texts:
            if (i.get()):
                 words.append(i.get())

        self.ranquear(words)
        
    
    def ranquear(self, listaSerie):
        spark_wordcount.BuscaParalelaSpark(listaSerie, self.sc)
        listajson = [serie+".json" for serie in listaSerie]
        json_to_txt.json_to_txt(listajson)
        spark_wordcount.wordCount(listaSerie, self.sc)
        for serie in listaSerie:
            unicode_to_text.unicode_to_txt(serie+".txt")
        data = self.sc.parallelize(listaSerie)
        self.sc.addPyFile("examples\src\main\python\Sentiment_Analysis.py")   
        rdd = data.map(lambda x: (x, Sentiment_Analysis.analiseCompleta(x))).collect()
        rank = Sentiment_Analysis.rank()
        resultado = ""
        for par in rank:
            resultado = resultado + par[1] + ":" + str(par[0]) + "\n"
        window_display_results(self.root, resultado)
            
class window_display_results:
    def __init__(self,root,text):
        #text = 'bla \n bla \n bla'
        T = Text(root,font = ("Times New Roman",20),height=10,width=20)
        T.pack()
        T.insert(END, text)
        
teste = Tk()
new_window = window_research(teste)
print new_window
teste.mainloop()


    

