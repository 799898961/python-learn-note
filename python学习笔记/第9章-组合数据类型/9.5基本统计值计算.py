# 9.5基本统计值计算.py

def getnum(): # 用户输入
    nums = []
    inumstr = input("请输入数字(回车退出)：")
    while inumstr != '':
        nums.append(eval(inumstr))
        inumstr = input("请输入数字(回车退出)：")

    return nums

def mean(numbers): # 计算平均值
    s = 0.0
    for num in numbers:
        s = s + num

    return s/len(numbers)

def dev(numbers, mean): # 计算方差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    
    return pow(sdev/(len(numbers)-1), 0.5)

def median(numbers): # 计算中位数
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0 :
        med = (numbers[size//2-1]+numbers[size//2])/2
    else :
        med = numbers[size//2]
    
    return med

n = getnum()
m = mean(n)
print("平均值：{}，方差：{:.2}，中位数：{}" .format(m, dev(n,m), median(n)))

# 问题分析：
# 给出一组数，对他们有个概要理解
# 总个数、求和、方差、平均值、中位数
# 总个数：len()
# 求个：遍历
# 平均数：求和/总个数
# 方差：公式
# 中位数：排序，然后奇数找中间一个，偶数找中间两个取平均