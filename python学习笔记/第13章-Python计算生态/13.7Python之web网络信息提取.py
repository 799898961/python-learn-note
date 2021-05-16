# 13.7Python之web网络信息提取.py

import bs4
import re

# beautifulsoup库
# HTML和XML的解析库等web信息功能
# 又名bs4或beautifulsoup4，可以加载多种解析引擎
# 常与网络爬虫库搭配使用，如：scrapy、requests等完成信息的获取和信息
# https://www.crummy.com/software/BeautifulSoup/bs4


# re库
# 正则表达式解析和处理功能库
# 提供了定义和解析正则表达式的一批通用功能
# 可用于各类场景，包括定点的web信息提取
# Python最主要的标准库之一，无需安装
# https://docs.python.org/3.6/library/re.html


# python-goose库
# 提取文章类型web页面提取的功能库
# 提供了对web页面中文章信息/视频等元数据的提取功能
# 针对特定类型web页面，应用覆盖面较广
# python最主要的web信息提取库
# https://github.com/grangier/python-goose