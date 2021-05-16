# 8.5lambda函数.py

f1 = lambda x,y : x+y
f2 = lambda : "lambda函数"
print(f1(10,15))
print(f2())


# lambda函数返回函数名作为结果
# lambda函数是一种匿名函数，即没有名字的函数
# 使用lambda保留字定义，用于定义简单的、能够在一行内表示的函数
# <函数名> = lambda<参数>:<表达式>

# 尽量不用
# 主要用于用作一些特定的函数或方法的参数
# 有固定的使用方式