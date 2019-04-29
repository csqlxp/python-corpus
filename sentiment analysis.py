f = open(r'F:/cn csr.txt', encoding='utf-8')
content = f.read()

import nltk
nltk.download('punkt')

from textblob import TextBlob
blob = TextBlob(content)

blob.sentiment