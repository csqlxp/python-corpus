f = open(r'F:/us csr.txt', encoding='utf-8')
content = f.read()

speech = content.lower().split()

dic = {}
for word in speech:
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] = dic[word] + 1

swd = sorted(dic.items(),key=lambda d: d[1],reverse=True)
print(swd)
