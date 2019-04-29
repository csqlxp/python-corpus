# -*- coding:utf-8 -*-

import math
import re
import datetime
import time

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

def clean(doc):
    stop_free = [i for i in doc.lower().split(" ") if i not in stop]
    #print([i for i in doc.lower().split()])
    punc_free = ' '.join([ch for ch in stop_free if ch not in exclude])
    #print(stop_free)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    print(normalized)
    return normalized

def cleanWords(words):
    words1_dict = {}
    for word in words:
        word = re.sub('[^a-zA-Z]', '', word)
        word = word.lower()
        if word in stop: continue #remove stopwords
        if word != '' and word in words1_dict:
            num = words1_dict[word]
            words1_dict[word] = num + 1
        elif word != '':
            words1_dict[word] = 1
        else:
            continue
    return words1_dict

def compute_cosine(text_a, text_b):
    ## find words and its freq
    words1 = text_a.split(' ')
    #a = " ".join(words1); print(a.encode('GBK','ignore'))
    words1_dict = cleanWords(words1)
    words2 = text_b.split(' ')
    words2_dict = cleanWords(words2)
    
    ## build the vectors by combined words in two dicts
    '''
    dic1 = sorted(words1_dict.items(), key=lambda asd: asd[1], reverse=True)
    dic2 = sorted(words2_dict.items(), key=lambda asd: asd[1], reverse=True)
    #print(dic1, dic2)
    words_key = []
    for i in range(len(dic1)):
        words_key.append(dic1[i][0])
    for i in range(len(dic2)):
        if dic2[i][0] in words_key:
            pass
        else:
            words_key.append(dic2[i][0]) #merge two dicts
    # print(words_key)
    '''
    words_key = []
    print(len(words1_dict.keys()), len(words2_dict.keys()))
    words_key.extend(words1_dict.keys())
    words_key.extend(words2_dict.keys())
    words_key = list(set(words_key))
    print(len(words_key))

    vect1 = []
    vect2 = []
    for word in words_key:
        if word in words1_dict:
            vect1.append(words1_dict[word])
        else:
            vect1.append(0)
        if word in words2_dict:
            vect2.append(words2_dict[word])
        else:
            vect2.append(0)
    #print(vect1)
    #print(vect2)

    ## compute cosine similarity
    # method1
    from sklearn.metrics.pairwise import cosine_similarity, pairwise_distances
    import numpy as np
    print("cosine similarity:",cosine_similarity(np.array([vect1, vect2])))
    print("cosine distances:",pairwise_distances(np.array([vect1, vect2]),metric="cosine"))
    # method2 by self-built
    return cosine_similar(vect1, vect2)
    
## compute cosine similarity
def cosine_similar(vector1, vector2):
    sum, sqrt1, sqrt2 = 0, 0, 0
    for i in range(len(vector1)):
        sum += vector1[i] * vector2[i]
        sqrt1 += pow(vector1[i],2)
        sqrt2 += pow(vector2[i],2)
    try:
        result = round(float(sum) / (math.sqrt(sqrt1) * math.sqrt(sqrt2)), 4)
    except ZeroDivisionError:
        result = 0.0
    return result

if __name__ == '__main__':
    begin_time = datetime.datetime.now()
    begin = time.time()
    f = open(r'F:\uscsr.txt',encoding='utf-8')
    f2 = open(r'F:\cncsr.txt',encoding='utf-8')
    textA = f.read()#; textA = textA.encode('GBK','ignore'); print(textA)
    textB = f2.read()#; textB = textB.encode('GBK','ignore'); print(textB)
    print(compute_cosine(textA, textB))

    end_time = datetime.datetime.now()
    end = time.time()
    print("datatime:", end_time - begin_time)
print("time:", end - begin)