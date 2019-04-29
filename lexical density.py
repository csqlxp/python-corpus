from nltk.corpus import PlaintextCorpusReader
corpus_root = r"F:\us csr"
corpora = PlaintextCorpusReader(corpus_root, '.*')
corpora.fileids()
myfiles = corpora.words(corpora.fileids())

stopwords_file = r'F:/stopword list.txt'
token_text = [word.lower()for word in myfiles if word.isalpha()]
clean_text = [word for word in token_text if word not in stopwords_file]
result1 = len(clean_text)/len(token_text)
result2 = len(set(clean_text))/len(token_text)
print ('               ','content words/tokens','   ','types/tokens')
print ('lexical density:',result1,'    ',result2)

from nltk.corpus import PlaintextCorpusReader
corpus_root = r"F:\cn csr"
corpora = PlaintextCorpusReader(corpus_root, '.*')
corpora.fileids()
myfiles = corpora.words(corpora.fileids())

stopwords_file = r'F:/stopword list.txt'
token_text = [word.lower()for word in myfiles if word.isalpha()]
clean_text = [word for word in token_text if word not in stopwords_file]
result1 = len(clean_text)/len(token_text)
result2 = len(set(clean_text))/len(token_text)
print ('               ','content words/tokens','   ','types/tokens')
print ('lexical density:',result1,'    ',result2)