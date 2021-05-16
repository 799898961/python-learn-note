# 8.7递归.py

def fact(n): # n的阶乘
    if n==0 :
        return 1
    else :
        return n*fact(n-1)

def rvs(s): # 反转字符串
    if s=="" :
        return s
    else :
        return rvs(s[1:]) + s[0]

def Fibonacci(n): # 斐波那契数列
    if n==1 or n==2 :
        return 1
    else :
        return Fibonacci(n-1) + Fibonacci(n-2)

count = 0
def hanoi(n, src, dst, mid): # 汉诺塔问题
    global count
    if n==1 :
        print("{}:{}->{}" .format(1, src, dst))
        count += 1
    else :
        hanoi(n-1, src, mid, dst)
        print("{}:{}->{}" .format(n, src, dst))
        count += 1
        hanoi(n-1, mid, dst, src)

print(fact(5))
hanoi(3, "a", "b", "c")
print(count)


# 紧耦合：两个部分之间交流很多，无法独立存在
# 松耦合：两个部分之间交流很少，可以独立存在
# 模块内部紧耦合、模块之间松耦合

# 递归：在函数定义中，调用函数自身的方式
# 两个关键特征：
# 链条：计算过程存在递归链条
# 基例：基础实例，存在一个或多个不需要再次递归的基例

# 函数内部，采用分支语句对输入参数进行判断
# 基例和链条，分别编写对应代码