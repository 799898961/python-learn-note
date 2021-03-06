# 8.1函数的定义.py

def fact(n):
    s = 1
    for i in range(1, n+1):
        s *= i 
    return s

a = fact(10)
print(a)


# 函数是一段代码表示
# def <函数名>(参数<0个或多个>):
#   <函数体>
#   return <返回值>

# 函数定义时，所指定的参数是一种占位符
# 函数定义后，如果不经过调用，不会被执行
# 函数定义时，参数时输入，函数体是处理，结果是输出(IPO)

# 调用是运行函数代码的方式

# 调用时要给出实际参数
# 实际参数替换定义中的参数
# 函数调用后得到返回值

