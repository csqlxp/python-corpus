f = open(r'F:/us csr.txt', encoding='utf-8')   #把us变为cn即可#
content = f.read()

from nltk.stem import WordNetLemmatizer
text1 = [word.lower()for word in content if word.isalpha()]
wnl = WordNetLemmatizer()
text2 = [wnl.lemmatize(word)for word in text1]

import nltk
vocab_list1 = open(r'C:/Users/pc/Downloads/10000-headwords/headwords 1st 1000.txt', 'r', encoding='utf-8')
vocab_list2 = open(r'C:/Users/pc/Downloads/10000-headwords/headwords 2nd 1000.txt', 'r', encoding='utf-8')
vocab_list3 = open(r'C:/Users/pc/Downloads/10000-headwords/headwords 3rd 1000.txt', 'r', encoding='utf-8')
vocab_list4 = open(r'C:/Users/pc/Downloads/10000-headwords/headwords 4th 1000.txt', 'r', encoding='utf-8')
vocab_list5 = open(r'C:/Users/pc/Downloads/10000-headwords/headwords 5th 1000.txt', 'r', encoding='utf-8')
vocab_list6 = open(r'C:/Users/pc/Downloads/10000-headwords/headwords 6th 1000.txt', 'r', encoding='utf-8')
vocab_list7 = open(r'C:/Users/pc/Downloads/10000-headwords/headwords 7th 1000.txt', 'r', encoding='utf-8')
vocab_list8 = open(r'C:/Users/pc/Downloads/10000-headwords/headwords 8th 1000.txt', 'r', encoding='utf-8')
vocab_list9 = open(r'C:/Users/pc/Downloads/10000-headwords/headwords 9th 1000.txt', 'r', encoding='utf-8')
vocab_list10 = open(r'C:/Users/pc/Downloads/10000-headwords/headwords 10th 1000.txt', 'r', encoding='utf-8')
vocab_list1_read = vocab_list1.read()
vocab_list2_read = vocab_list2.read()
vocab_list3_read = vocab_list3.read()
vocab_list4_read = vocab_list4.read()
vocab_list5_read = vocab_list5.read()
vocab_list6_read = vocab_list6.read()
vocab_list7_read = vocab_list7.read()
vocab_list8_read = vocab_list8.read()
vocab_list9_read = vocab_list9.read()
vocab_list10_read = vocab_list10.read()
vocab_list1.close()
vocab_list2.close()
vocab_list3.close()
vocab_list4.close()
vocab_list5.close()
vocab_list6.close()
vocab_list7.close()
vocab_list8.close()
vocab_list9.close()
vocab_list10.close()
vlist1 = nltk.word_tokenize(vocab_list1_read.lower())
vlist2 = nltk.word_tokenize(vocab_list2_read.lower())
vlist3 = nltk.word_tokenize(vocab_list3_read.lower())
vlist4 = nltk.word_tokenize(vocab_list4_read.lower())
vlist5 = nltk.word_tokenize(vocab_list5_read.lower())
vlist6 = nltk.word_tokenize(vocab_list6_read.lower())
vlist7 = nltk.word_tokenize(vocab_list7_read.lower())
vlist8 = nltk.word_tokenize(vocab_list8_read.lower())
vlist9 = nltk.word_tokenize(vocab_list9_read.lower())
vlist10 = nltk.word_tokenize(vocab_list10_read.lower())
vocab_list = vlist1 + vlist2 + vlist3 + vlist4 + vlist5 + vlist6 + vlist7 + vlist8 + vlist9 + vlist10
clean_text = [word for word in text2 if word in vocab_list]
result = len(clean_text)/len(text2)
print (result)