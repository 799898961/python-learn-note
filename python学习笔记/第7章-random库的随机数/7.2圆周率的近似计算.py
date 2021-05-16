# 7.2圆周率的近似计算.py
# 计算公式:
# π = Σ(k=[0,∞)){[1/(16^k)]*[4/(8k+1)-2/(8k+4)-1/(8k+5)-1/(8k+6)]}
pi = 0
n = 100
for i in range(n):
    pi += 1/pow(16,i)*(
        4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+6)
        )
print("圆周率的近似值为：{}" .format(pi))