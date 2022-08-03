#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup

lottery_file = open("small5.txt", "wb")


webstr = 'https://www.lottery.gov.cn/kj/kjlb.html?plw'
#    print(webstr.encode('utf-8'))

response = urllib.request.urlopen(webstr)
soup = BeautifulSoup(response, "html.parser")
response.close()
td = soup.find_all("td")
data = {}
for x in range(0,len(td)-1,2):
    data[td[x].text.strip()] = td[x+1].text.strip()

print(data)