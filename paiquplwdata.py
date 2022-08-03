#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import json
lottery_file = open("pailie5.txt", "wb")


webstr = 'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=350133&provinceId=0&pageSize=30&isVerify=1&pageNo=1'

response = urllib.request.urlopen(webstr)
soup = BeautifulSoup(response, "html.parser")
print(soup)

print(json.loads(webstr))