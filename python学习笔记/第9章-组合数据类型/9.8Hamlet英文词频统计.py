# 9.8Hamlet英文词频统计.py

def gettext():
    txt = open("C:\\Users\\79989\\Documents\\vscode-Python\\第9章-数据结构\\hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in "!'#$%&()*+,-./:;<=>?@[\\]^_‘{|}~" :
        txt = txt.replace(ch, " ")
    return txt

hamlettxt = gettext()
words = hamlettxt.split()
counts = {}
for word in words :
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10},{1:>5}" .format(word, count))



# str.split(sep=None) 返回一个列表，由str根据sep被分割的部分组成
# d.item()    返回字典d中所有键值对的信息  
