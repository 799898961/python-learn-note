# random库是使用随机数的Python标准库

# 随机数：各种条件下产生的确定值
# 伪随机数：采用梅森旋转算法生成的(伪)随机序列中的元素
# random库主要用于生成随机数
# import random

# random库包括两类函数，常用共八个
# 基本随机数函数：
# (1) seed()
# (2) random()
# 
# 扩展随机数函数：
# (1) randint()
# (2) getrandbits()
# (3) uniform()
# (4) randrange()
# (5) choice()
# (6) shuffle()

# 随机数种子
# 随机数种子 ——> 梅森旋转算法 ——> 随机数序列
# 种子相同，随机数序列相同

# random.seed()
# 初始化给定的随机数种子，默认为当前系统时间
# 当不调用seed()函数时，会默认使用当前系统时间作为种子

# random.random()
# 生成一个[0.0, 1.0)之间的随机小数
# 不给种子时，种子是当前调用random()函数时的系统时间

# random.randint(a,b)
# 生成一个[a,b]之间的整数

# random.randrange(m,n[,k])
# 生成一个[m,n)之间（以k为步长）的随机整数
# 例：
# random.randrange(10,100,10)
# 表示生成[10,100)之间，以10为步长的整数
# 即：可能的数有：10,20,30,……,90

# random.getrandbits(k)
# 生成一个k比特长的随机整数

# random.uniform(a,b):
# 生成一个[a,b]之间的随机小数

# choice(seq)
# 从序列seq中随机选择一个元素
# 例：
# random.choice([1,2,3,4,5,6,7,8,9])
# 从列表中随机选取一个元素

# shuffle(seq)
# 将序列seq中的元素随机排列，返回打乱后的序列

# random.choices(population,weights=None,*,cum_weights=None,k=1)
#   population：集群。
#   weights：相对权重。
#   cum_weights：累加权重。
#   k：选取次数。
# 作用：从集群中随机选取k次数据，返回一个列表，可以设置权重。
# 注意每次选取都不会影响原序列，每一次选取都是基于原序列。

# random.sample(population,k)
# 从集群population中选取k个元素，返回一个列表，集群可以是list、tuple、str、set。

# 与random.choices()的区别：一个是选取k次，一个是选取k个，选取k次的相当于选取后又放回，
# 选取k个则选取后不放回。故random.sample()的k值不能超出集群的元素个数。
'''
import numpy as np
import pandas as pd
import random as rd

star_level = [3,4,5,6]
chance = [0.4,0.3,0.2,0.1]
lis = rd.choices(star_level, chance, k=100)
for i in range(len(star_level)) :
    print(lis.count(star_level[i]))
'''