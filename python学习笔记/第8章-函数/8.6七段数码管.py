# 8.6七段数码管.py

import turtle
import time

def drawgap():  # 绘制数码管间隔
    turtle.penup()
    turtle.fd(5)

def drawline(draw): # 绘制单段数码管
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawgap()
    turtle.right(90)

def drawdight(dight): # 根据数字绘制七段数码管
    drawline(True) if dight in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if dight in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if dight in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if dight in [0,2,6,8] else drawline(False)
    turtle.left(90)
    drawline(True) if dight in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if dight in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if dight in [0,1,2,3,4,7,8,9] else drawline(False)
    turtle.left(180) # 调用完drawline函数后的朝向为左，需调转180度
    turtle.penup() #为绘制后续数字确定位置
    turtle.fd(20)  #为绘制后续数字确定位置，决定数字间的距离

def drawdate(date): # 通过eval()函数将数字变成整数
    turtle.pencolor("red")
    for i in date:
        if i=="-" :
            turtle.write("年", font=("Arial", 18, "normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i=="=" :
            turtle.write("月", font=("Arial", 18, "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i=="+" :
            turtle.write("日", font=("Arial", 18, "normal"))
        else :
            drawdight(eval(i))

def main():
    turtle.setup(800, 350, 200, 200)
    turtle.hideturtle()
    turtle.speed(0)
    # turtle.colormode(255)
    # turtle.pencolor(0,100,255)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawdate(time.strftime("%Y-%m=%d+", time.gmtime()))
    # turtle.hideturtle()
    turtle.done()

main()



# 基本思路：
# 步骤一：绘制单个数字对应的数码管
# 步骤二：获得一串数字，绘制对应的数码管
# 步骤三：获取当前系统时间，绘制对应的数码管

# 步骤一：
# 绘制单个数码管
# 七段数码管可以有固定的顺序
# 不同的数字显示不同的线条
#            6→   
#            ——
#         5↑|1→|↓7   
#  start --> ——
#         4↑|  |↓2
#            ——    
#            ←3

# 增加七段数码管之间的线条间隔

# 步骤三：
# 获取系统时间，绘制七段数码管
# 使用time库获得系统当前时间
# 增加年月日标记，且年月日颜色不同

# turtle.write()函数
# turtle.write(arg,move=false,align='left',font=('arial',8,'normal'))
# arg —— 所绘制的文本
# move —— 默认为false 开启后将笔移动到右下角
# align —— 对齐方式 左(left) 中(center) 右(right)
# font —— 字体信息：
# 第一个参数：字体名称
# 第二个：字号大小
# 第三个：字体类型  加粗(bold) 正常(normal)

# 理解方法思维：
# 模块化思维：确定模块接口，封装功能
# 规则化思维：抽象过程为规则，计算机自动执行
# 化繁为简：将大功能分成小功能 
