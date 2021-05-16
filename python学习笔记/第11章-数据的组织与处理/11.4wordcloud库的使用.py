# 11.4wordcloud库的使用.py

import wordcloud
import jieba
from imageio import imread

txt = "程序设计语言是计算机能够理解和识别用户操作意图的一种交互体系，\
    它按照特定的规则组织计算机指令，使计算机能够自动进行各种运算处理"
c = wordcloud.WordCloud(
    width=1000,height=700,
    font_path="msyh.ttc",
    background_color="white"
)
c.generate(" ".join(jieba.lcut(txt)))
c.to_file("pywordcloud.png")


# wordcloud是词云展示的第三方库

# wordcloud库把词云当做一个WordCloud对象
# wordcloud.WordCloud() 代表文本对应词云的对象
# 可以根据文本中词语出现的频率等参数绘制词云
# 绘制词云的形状，尺寸和颜色都可以设定

# w = wordcloud.WordCloud()
# 以WordCloud对象为基础
# 可以像这样一个对象中配置参数、加载文本、输出文件

# 常规方法：
# w = wordcloud.WordCloud()
# w.generate(txt) 向WordCloud对象w中加载文本txt
# 中文需要先分词，再组成由空格分隔的字符串
# w.to_file(filename) 将词云输出为图像文件 .png 或 .jpg 格式

# 词云绘制过程：
# 配置对象参数
# 加载词云文本
# 输出词云文本

# 生成一个图片，宽高比默认为400:200

# 生成过程：
# ① 分隔：以空格为单位分隔单词
# ② 统计：单词出现次数并过滤，单词出现多的显示的大，单词出现少的显示的小
# 过滤掉很短的、1~2个字符的单词
# ③ 字体：根据统计信息配置字号
# ④ 布局：颜色环境尺寸

# c = wordcloud.WordCloud(<参数>)
# 参数：
# width 指定词云对象生成图片的宽度
# height 指定词云对象生成图片的高度
#
# min_font_size 词云中字体的最小字号，默认4号
# max_font_size 词云中字体的最大字号，根据高度自动调节
# font_step 指词云中的字体从最小到对大变化过程中的，字号的增加步长，默认为一
# font_path 指定字体文件路径，默认为None
# 如：c = wordcloud.WordCloud(font_path="msyh.ttc")
# 有中文时加上微软雅黑的字体
# 
# max_words 指定词云显示的最大单词数量，默认为200
# stop_words 指定词云的排除词列表，即不显示的单词列表
#
# mask 指定词云形状，默认为长方形，需要引用imread()函数
# 具体实例：
'''
from scipy.misc import imread imread
imread函数已经在scipy.misc库中被弃用，先包含在imageio库中
'''
# from imageio import imread
# mk = imread("pic.png")
# w = wordcloud.WordCloud(mask=mk)
#
# background_color 背景颜色，默认为黑色