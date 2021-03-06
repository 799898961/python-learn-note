# 8.3函数的返回值.py

def fact(n, m=1):
    s = 1
    for i in range(1, n+1):
        s *= i 
    return s//m, n, m

a, b, c = fact(10,5)
print(a, b, c)


# 函数的返回值：
# 函数可以返回0个或多个结果
# return保留字用来传递返回值
# 函数可以有返回值，也可以没有，可以有return，也可以没有
# return可以传递0个返回值，也可以传递任意多个返回值

# 若使用一个变量接收多个返回值，则返回返回值的元组类型
# 若使用对应数量的变量接收多个返回值
