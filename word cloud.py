f = open(r'F:/us csr.txt', encoding='utf-8')
content = f.read()

from wordcloud import WordCloud
wordcloud = WordCloud(background_color = "white", max_font_size = 40).generate(content)

%pylab inline
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("off")