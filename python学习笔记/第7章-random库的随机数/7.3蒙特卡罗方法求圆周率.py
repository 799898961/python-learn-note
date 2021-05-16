# 7.3蒙特卡罗方法求圆周率.py
# 蒙特卡罗方法又称撒豆法
from random import random
from time import perf_counter
darts = 10000*10000   # 撒豆总数
inside = 0.0    # 在圆内部的点的数量
start = perf_counter()
for i in range(1, darts+1):
    x,y = random(), random()
    dist = pow(x**2 + y**2, 0.5)
    if dist <= 1.0:
        inside = inside + 1
pi = 4 * (inside/darts)
print("圆周率的值为：{:.7f}" .format(pi))
print("运算时间为：{:.5f}s" .format(perf_counter() - start))