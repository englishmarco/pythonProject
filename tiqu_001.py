#--*--conding:utf-8 --*--
# Author: Gonggong
# 使用python爬取一个网页中表格的内容，并把抓取到的内容以json格式保存到文件中

import requests
from lxml import etree
import json


# 获取网页源代码
r = requests.get('http://ipwhois.cnnic.cn/bns/query/Query/ipwhoisQuery.do?queryOption=ipv4&txtquery=8.8.8.8')

# 使用xpath对爬取的源代码进行处理
dom_tree = etree.HTML(r.content)
links = dom_tree.xpath("/html/body/center[1]/table[1]/tr/td/font")

# 取出links的单行、双行的数据
res1 = [i.text for i in links[::2]]
res2 = [i.text for i in links[1::2]]

# 把两行数据组合成在一起
result = tuple(zip(res1, res2))

# 使用json格式保存到文件中
json.dump(result, open('D:\get.txt', 'w',encoding='utf-8'), ensure_ascii=False)