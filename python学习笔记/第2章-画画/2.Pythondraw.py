# Pythondraw.py
import turtle
turtle.setup(650, 350, 200, 200)
turtle.ht() # 隐藏海龟
turtle.speed() # 绘画速度
turtle.penup()
turtle.fd(-250)
turtle.pendown()
# turtle.colormode(255)
turtle.pensize(25)
turtle.pencolor("tomato")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40*2/3)
turtle.done()


# turtle(海龟)库：
# Python标准库之一 入门级的图形绘制函数库

# turtle的绘图窗体
# 以屏幕左上角的坐标为(0,0) 横向为x 纵向为y
# 绘图窗体的左上角是turtle绘图窗体的绘图原点
# 绘图窗体相对于屏幕左上角有一个相对坐标(startx,starty)
# 绘图窗体本身也有着 宽度(横向,width) 和 高度(纵向,height) 两个属性
# 可用turtle中的 setup()函数 设置窗体大小及位置
# 即：turtle.setup(width, height, startx, starty)
# 其中后两个参数可选，当后两个参数不存在时则默认窗体生成在屏幕正中心
# 且setup()函数不是必须的

# turtle的空间坐标体系：
# (1)绝对坐标：绘图窗体的正中心 横向为x 纵向为y
# 一些控制函数：
# turtle.goto(x,y)：对处在任意位置的海龟去到达某一位置
# (2)海龟坐标：前侧为前进方向，类似的有：后退方向、左(右)侧方向
# 一些控制函数：
# turtle.fd(d)：表示向前进方向移动d个像素
# turtle.bk(d)：表示向后退方向移动d个像素
# turtle.circle(r, angle)：以海龟当前前进方向左侧的某一个点为圆心
# 做半径为 r 圆心角为 angle 的圆周运动

# turtle的角度坐标体系：
# (1)绝对角度：在空间角度中，x轴正半轴为 0/360 度；y轴正半轴为 90/-270 度 并以此类推
# 一些控制函数：
# turtle.seth(angle)：改变海龟的行进角度(方向)，且只改变方向而不行进
# 参数 angle ：绝对度数
# (2)海龟角度：从海龟坐标的角度出发，对于海龟运行的方向使用 左 和 右 来提供角度
# 一些控制函数：
# turtle.left(angle)
# turtle.right(angle)

# RGB色彩体系：
# 指由红绿蓝三个通道的颜色组合来覆盖视力所能感知的所有颜色
# RGB每色的取值范围为 0-255 的整数或 0-1 的小数
# turtle的RGB色彩模式：
# 默认采用小数值，可切换为整数值
# 一些控制函数：
# turtle.colormode(mode)
# 1.0：RGB小数值模式
# 255：RGB整数值模式


# 常用RGB色彩：
#   名称             RGB整数值     RGB小数值
# 白色(white)       255,255,255     1,1,1
# 黑色(black)       0,0,0           0,0,0
# 黄色(yellow)      255,255,0       1,1,0
# 洋红(magenta)     255,0,255       1,0,1
# 青色(cyan)        0,255,255       0,1,1
# 蓝色(blue)        0,0,255         0,0,1
# 
# 海贝色(seashell)  255,245,238     1, 0.96, 0.93
# 金色(gold)        255,215,0       1, 0.84, 0
# 粉红色(pink)      255,192,203     1, 0.75, 0.80
# 棕色(brown)       165,42,42       0.65, 0.16, 0.16
# 紫色(purple)      160,32,240      0.63, 0.13, 0.94
# 番茄色(tomato)    255,99,71       1, 0.39, 0.28

# 库引用和import函数：
# 1.库引用：扩充Python程序功能的方式
# 使用 import 保留字完成，采用<a>.<b>()的编码风格
# 例：
#   import <库名>
#   <库名>.<函数名>(<函数参数>)
#
# 2.import函数的其他用法：
# (1) form <库名> import <函数1>,<函数2>,......
# 表示从某库中引用某个或者某些函数
# (2) from <库名> import*
#     <函数名>(<函数参数>)
# 表示引用库中的全部函数，使用时直接使用函数名+函数参数(可选)
# (3) import <库名> as <库别名>
#     <库别名>.<函数名>(<函数参数>)
# 表示给库起一个别名，类似于C语言的 #define <库名> <库别名>
# 
# 3.(1) 和 (2)的比较
# (1)不会出现函数重名问题，但有时不方便
# (2)方便但引用多种库后易造成重名

# turtle画笔控制函数
# (1) turtle.penup() 别名 turtle.pu()
# 表示抬起画笔，使其移动轨迹不显示在画布上，让海龟起飞飞飞~
# (2) turtle.pendown() 别名 turtle.pd()
# 表示落下画笔
# 使用时一般成对出现
# (3) turtle.pensize() 别名 turtle.width
# 画笔宽度，海龟腰围
# (4) turtle.pencolor(color)
# 画笔颜色 
# color 为颜色字符串或 r,g,b 值
# color参数的形式：
# a. 颜色字符串：turtle.pencolor("purple")
# b. RGB的小数值：turtle.pencolor(0.63, 0.13, 0.94)
# c. RGB的元组值：turtle.pencolor( (0.63, 0.13, 0.94) )
# d. RGB的整数值：
#   在默认情况下color参数只接受字符串和小数值所以要使用
# turtle.colormode(255)转换成RGB整数值模式，在此情况下
# turtle.pencolor(160, 32, 240)

# turtle运动控制函数：
# 1.turtle.forward(d) 别名turtle.fd(d)
#   表示向前进方向移动d个像素
#   参数 d 行进距离，可以是负数，负数表示倒退行进
# 2.turtle.circle(r, extent=None)
#   根据半径 r 绘制 extent 角度的弧形
#  r：默认圆心在海龟左侧 r 距离的位置，负数时为右侧半径绝对值距离
#  extent：绘制角度，默认是360度整圆 

# turtle方向控制函数：
# turtle.setheading(angle) 别名 turtle.seth(angle)
# 控制海龟的面对方向：绝对角度 & 海龟角度
# angle：改变海龟当前的行进方向，使其改变为某一绝对角度
# turtle.left(angle) & turtle.right(angle)
# 向左或向右转angle度

# 循环控制：
# 常用结构：
# for <变量> in range (<参数>):
#   <被循环的语句>
# <变量> 表示每次循环的计数，0到<次数>-1
# 在C语言中相当于：for(i=0; i<n; i++){}
# 例：
# for i in range(5):
#   print("hello:",i)
# 输出结果：
# 共5行，为：hello: 0   hello: 1    hello: 2 以此类推
#
# print的一种输出方法：在小括号()内的输出的各种信息间用逗号,隔开
# 输出之后每输出的字符串之间会带有空格
#
# range()函数：产生循环计数序列
# 1.range(n)：产生0到n-1的整数序列，共n个
# 例：range(5)  0,1,2,3,4
# 2.range(m, n)：产生 m 到 n-1 的整数序列
# 例：range(2, 5)   2,3,4