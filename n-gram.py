# -*- coding:utf-8 -*-

import math
import re, sys
import datetime
import time

from nltk.corpus import stopwords
import string
from nltk import ngrams

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
stop.add('')

def get_Ngrams(listA, N, key, form):
    #print(listA)
    grams_N = ngrams([word.lower() for word in listA], N)
    #tmpt = list(set(grams_N))
    #print(tmpt)
    #print(grams_N)
    results = {}
    for i in grams_N:
        if (len(set(i) & set(stop)) == 0) and (key in i):
            if (form == 'noun' and i[-1] == key) or (form == 'adj' and i[-1] != key):
                #print(type(i))
                if ' '.join(i) not in results:
                    results[' '.join(i)] = 0
                results[' '.join(i)] += 1
                '''
                try:
                    print(i)
                except:
                    print(i.encode('utf-8'))
                sys.stdout.flush()
                '''
    return results

def cleanWords(textA):
    text1 = re.split('[.,\n]',textA)
    text1 = [re.compile(r'  ').sub(' ', i) for i in text1]
    allwords = []
    for seq in text1:
        words = seq.split(' ')
        #print(words)
        punc_free = [ch for ch in words if ch and (chr not in exclude)]
        allwords = allwords + [re.sub('[^a-zA-Z]', '', word) for word in punc_free]
    return allwords

def printout(grams_N):
    grams_N = sorted(grams_N.items(), key=lambda asd: asd[1], reverse=True)
    for i in grams_N:
        print(i)

if __name__ == '__main__':
    begin_time = datetime.datetime.now()
    begin = time.time()
    f = open(r'F:\uscsr2010.txt',encoding='utf-8')
    f2 = open(r'F:\cncsr2010.txt',encoding='utf-8')
    textA = f.read()#; textA = textA.encode('GBK','ignore'); print(textA)
    textB = f2.read()#; textB = textB.encode('GBK','ignore'); print(textB)
    #text1 = textA.split('\n')
    
    print("2-Ngrams:")
    grams_2 = get_Ngrams(cleanWords(textA), 2, 'environmental', 'adj')
    printout(grams_2)
    print("--------------------------")

    print("2-Ngrams:")
    grams_2 = get_Ngrams(cleanWords(textB), 2, 'environmental', 'adj')
    printout(grams_2)
    print("--------------------------")

    print("2-Ngrams:")
    grams_2 = get_Ngrams(cleanWords(textA), 2, 'environment', 'noun')
    printout(grams_2)
    print("--------------------------")
    
    print("2-Ngrams:")
    grams_2 = get_Ngrams(cleanWords(textB), 2, 'environment', 'noun')
    printout(grams_2)
    print("--------------------------")
    
 
    
    end_time = datetime.datetime.now()
    end = time.time()