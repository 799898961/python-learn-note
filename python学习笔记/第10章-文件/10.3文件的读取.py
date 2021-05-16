# 10.3文件的读取.py

fp = open("test.txt", "r", encoding="UTF-8").read(2)
fa = open("test.txt", "r", encoding="UTF-8").readline()
fb = open("test.txt", "r", encoding="UTF-8").readlines()
print(fp)
print(fa)
print(fb)

# 遍历全文本的方法
fname = input("请输入要打开的文件名称：")
fo = open(fname, "r")
txt = fo.read(2)
while txt != "" :
    # 对txt进行处理
    txt = fo.read(2)
fo.close()
# 分阶段，按数量读入，逐步处理

# 逐行处理文件：方法一
fname = input("请输入要打开的文件名称：")
fo = open(fname, "r")
for line in fo.readlines():
    print(line)
fo.close()
# 一次读入，分行处理

# 逐行处理文件：方法二
fname = input("请输入要打开的文件名称：")
fo = open(fname, "r")
for line in fo:
    print(line)
fo.close()
# 若使用fo.readline()则不会逐行输出，因为只表示读取一行
# 分行读入，逐行处理


# 读文件：
# a.read(size)
# 读入全部内容，如果给出参数，读入前size长度

# a.readline(size)
# 读入一行内容，如果给出参数，读入该行前size长度

# a.readlines(hint)
# 读入文件所有行，以每行元素形成列表，如果给出参数，读入前hint行
