# 3.1数据类型note1.py
# pow(x, y)：计算x的y次方
0.1 + 0.2 == 0.3
# 由于存在不确定尾数会导致上述式子的结果为 false 
round(0.1+0.2, 1) == 0.3
# 由于保留一位小数，上述式子成立，结果为 true
# round(x, d)：对x四舍五入，d是小数截取位数
# 浮点数间的运算及比较用 round() 函数辅助
# 不确定尾数一般发生在10^(-16)左右，round()十分有效

# 存在复数（虚数）类型的数
# 例：z = 1.23e-4+5.6e+89j
# z.real 获得实部
# z.imag 获得虚部

# Python中的操作运算符：
# x / y 将产生浮点数结果 例：10/3 的结果是 3.33333333……
# x // y 表示整数除，产生整数结果 例：10//3 的结果是 3
# -y y的负值
# x % y 表示取余
# x ** y 表示幂运算 x的y次幂，且当y为小数时做开方运算
# 二元操作符 x op= y 即：x = x op y，op表示二元操作符
# x+=y  x-=y等

# 不同类型间的混合运算，结果生成取值范围更宽的类型
# 以上三种类型存在一个逐渐“变宽”或“扩展”的关系：
#   整数 -> 浮点数 -> 复数

# 数值运算函数：
# abs(x)        取x的绝对值
# divmod(x,y)   取两数的商和余数，(x//y, x%y)其结果作为二元数输出
# 如：divmod(10,3) 结果为 (3,1)
# pow(x, y[,z]) 幂余运算，等价于 (x**y)%z，[,z]表示参数z可省略
# 如：pow(3, pow(3,99), 10000) 表示 3^(3^(99))%10000 结果为 4587
# round(x[,d]) 四舍五入，d是保留位数，不填时默认为0
# max(x1,x2,……,xn) 参数数量不限，取最大值
# min(x1,x2,……,xn) 取最小值
# int(x) 将x变成整数舍弃小数部分或将字符串转变为整数
# float(x) 将x变为浮点数，增加小数部分
# 如：float(12) 结果为 12.0 ; float("1.23") 结果为 1.23
# complex(x) 将x变成复数(虚数)，增加虚数部分
# 如：complex(4) 结果为 4 + 0j(i)