# 6.3循环控制保留字.py

for c in "python":
    if c=='t':
        continue
    print(c, end="")

print()

for c in "python":
    if c=='t':
        break
    print(c, end="")

print()

s = "python"
while s != '':
    for c in s:
        print(c, end="")
    print()
    s = s[:-1]
# s为一个字符串 在s不是空字符串的情况下进入循环
# 通过字符串遍历，输出每个字符，并在遍历结束后对s所对应的字符串切片
# 去掉最后一个字符，再进行while循环，直到s为空字符串
s = "python"
while s != '':
    for c in s:
        if c=='t':
            break
        print(c, end="")
    s = s[:-1]


# 循环控制保留字
# break:跳出并结束当前整个循环，执行循环后的语句
# continue:跳过本轮循环
# 二者都可以与for和while循环搭配使用