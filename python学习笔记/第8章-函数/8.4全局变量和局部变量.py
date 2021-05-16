# 8.4全局变量和局部变量.py

n, s = 10, 100      # 全局变量
def fact1(n):
    s = 1   # 局部变量
    for i in range(1, n+1):
        s *= i

    return s

def fact2(n):
    global s
    for i in range(1, n+1):
        s *= i

    return s    # 此处s指全局变量

ls = ["F", "f"]   # 通过使用[]来创建一个全局变量列表ls
def func1(a):
    ls.append(a)
# 此处ls为列表类型，并未在函数中创建，则等同与局部变量 #

    return

def func2(a):
    ls = []
    ls.append(a)
# 此处有一个同名ls局部列表类型变量被建立 #
# 则修改在函数内部的列表 #

    return

print(fact1(n), s)
print(fact2(n), s)  # 全局变量s被函数修改

func1("c")  # 全局变量ls被修改
print(ls)


# 使用规则：
# (1)局部变量和全局变量是不同变量
# (2)局部变量为组合数据类型且未创建，等同于局部变量

# 局部变量是函数内部的变量，即使重名也不相同
# 函数运算结束后，局部变量会被释放

# 可以使用global保留字在函数内部使用全局变量
# global用于声明全局变量，存在时使用，不存在就建立