f = open(r'F:\cn csr.txt',encoding='utf-8')

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()
def clean(doc):
    stop_free = [i for i in doc.lower().split(" ") if i not in stop]
    punc_free = " ".join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized
doc_clean = []
for doc in f:
doc_clean.append(clean(doc).split())    #格式！！！

import gensim
from gensim import corpora

dictionary = corpora.Dictionary(doc_clean)

doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

ldamodel = gensim.models.ldamodel.LdaModel(doc_term_matrix, num_topics=5, id2word = dictionary, passes=20)
print(ldamodel.print_topics(num_topics=5, num_words=2))