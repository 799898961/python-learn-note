# 8.2函数的参数传递.py

def fact1(n, m=1):
    # m 可选参数 #
    # 在函数调用时，若给出第二个参数m的值，则用给出的实际值
    # 若不给出m的值，则默认m=1
    s = 1
    for i in range(1, n+1):
        s *= i 

    return s//m

def fact2(n, *b):
# *b 可变参数 #
# 包括一个或多个参数 也是一个可选参数
    s = 1
    for i in range(1, n+1):
        s *= i 
    for item in b:
        s *= item
    
    return s

def test(tes: dict) : 
    "指定参数的类型"
    tes["name"] = 1
    pass




a = fact1(10)
b = fact1(10, 10)
c = fact2(10, 3)
d = fact1(m=5, n=10)    # 名称传递
print(a, b, c, d)
test(a)




# 函数定义时可以没有参数，但必须保留括号

# 函数定义时可以为某些参数指定默认值，构成可选参数
# Python规定：
# 所有的可选参数必须放在非可选参数(必选参数)之后

# 可变参数传递：
# 函数定义时可以设计可变数量参数，即不确定参数及总数量

# 参数传递的两种方式：
# 函数调用时，参数可以按照位置或名称方式传递

