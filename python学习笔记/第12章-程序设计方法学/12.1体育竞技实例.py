# 12.1体育竞技实例.py

from random import random

def printinfo():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值(以0~1之间的小数表示)")

def getinputs():
    a = eval(input("请输入选手A的能力值(0~1): "))
    b = eval(input("请输入选手B的能力值(0~1): "))
    n = eval(input("模拟比赛的场次: "))

    return a,b,n

def printsummary(winsA, winsB):
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛" .format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}" .format(winsA, winsA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}" .format(winsB, winsB/n))
    # {:0.1%} 以百分比形式输出并占0个字符

def simNgames(n,probA,probB):
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA, scoreB = simONEgame(probA,probB)
        if scoreA > scoreB :
            winsA += 1
        else :
            winsB += 1
    return winsA, winsB

def simONEgame(probA, probB):
    scoreA, scoreB = 0, 0
    serving = "A"
    while not gameover(scoreA, scoreB):
        if serving == "A" :
            if random() < probA:
                scoreA += 1
            else :
                serving = "B"
        else :
            if random() < probB :
                scoreB += 1
            else :
                serving = "A"

    return scoreA, scoreB

def gameover(a, b):
    return a==15 or b==15
    # 此处为一个逻辑判断语句 与if的效果相同

def main():
    printinfo()
    probA, probB, n = getinputs()
    winsA, winsB = simNgames(n,probA,probB)
    printsummary(winsA,winsB)

main()

# 比赛规则：
# 双人击球比赛：A & B 回合制 5局3胜
# 开始时一方发球，直至判分，接下来胜者发球
# 球员只能在发球局得分，15分胜一局

# 自顶向下（设计）：
# 大问题分解成小问题，小问题再分解
# 自底向上（执行）：
# 逐步组建复杂系统的有效测试方法
# 分单元测试，逐步组装

# 程序总体框架及步骤：
# 步骤一：打印程序的介绍性信息
# 步骤二：获得程序运行参数
# 步骤三：利用球员A和B的能力值，模拟n局比赛
# 步骤四：输出球员A和B获胜比赛的场次和概率
# -printinfo()
# -getinputs()
# -simngames()
# -printsummary()

# 可以优化：
# 在随机数判断谁赢谁输 simONEgame(probA, probB)
# gameover函数的可读性优化
# 只在发球回合得分的规则
# 算法表明二者不能平分

# 扩展：
# 增加参数以增加分析数据的维度
# 扩展比赛设计
# 如：a在一定情况下失误b得分