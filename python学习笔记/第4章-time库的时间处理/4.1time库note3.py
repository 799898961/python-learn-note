# time库.py

import time
print(time.time())
print(time.ctime())
print(time.gmtime())

t = time.gmtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", t))

timestr = "2020-08-08 12:40:29"
ti = time.strptime(timestr, "%Y-%m-%d %H:%M:%S")
print(ti)

start = time.perf_counter()
time.sleep(2)
end = time.perf_counter()
print("{:.3f}" .format(end-start))

# time库时Python中处理时间的标准库
# 表达计算机时间
# 提取系统时间并格式化输出功能
# 提供系统级精确计时功能，用于程序程序性能分析
# 使用 import time 和 time.<b>() 调用相关函数

# time库包括三类函数
# 1.时间获取：time()  ctime()  gmtime()
# 2.时间格式化和输出：strftime()  strptime()
# 3.程序计时：sleep()  perf_counter()

# time.time():
# 获取当前时间戳，计算机内部时间值，以一个浮点数表示
# time.ctime():
# 获取当前时间并以易读方式表示，返回字符串
# time.gmtime():
# 获取当前时间，表示为计算机可处理的时间格式
# 结果为 一种struct_time格式的类似于C语言结构体的一种结构
# 该函数获取的时间为UTC时区（0时区）的时间，使用时需加上时差
# 如：中国 为东八区时间（UCT+8）

# 时间格式化：
# 将时间以合理的方式展示出来
# 类似于字符串格式化，需要有展示模板
# 展示模板有特定的格式化控制符组成

# strftime()方法：
# strftime(tpl, ts)
# tpl是格式化模板字符串，用来定义输出效果
# ts是计算机内部时间类型变量
#
# tpl字符串中的时间控制符：
# 格式化字符串  日期/时间说明    值范围和实例
#     %y        两位数年份         00~99 
#     %Y           年份         0000~9999
#     %a         星期缩写         Mon~Sun
#     %A         星期全写      Monday~Sunday
#     %H      小时(24小时制)       00~23
#     %p          上/下午         AM，PM
#     %M           分钟           00~59
#     %S            秒            00~59
#     %b     本地月份名称简写     Jan~Nov
#     %B     本地月份名称全写   January~November
#     %c 本地相应的日期表示和时间表示     
#     %x     本地相应的日期表示
#     %X     本地相应的时间表示
#     %Z       当前时区的名称


# strptime()方法：
# 根据指定的格式把一个时间字符串解析为时间元组。
# 也就是自定义时间格式
#
# strftime(str, tpl)
# str是字符串形式的时间值
# tpl是格式化模板字符串，用来定义输入效果

# 程序计时
# 指测量起止动作所经历的时间的过程
# 测量时间：time.perf_counter()
# 测量CPU以其频率运行的时钟，精度可在纳秒，单位为秒
# 由于数值起点不确定，连续调用取差值才有意义
# 产生时间：time.sleep()
# 让程序暂时挂起一段时间，()内填入浮点数，单位为秒

