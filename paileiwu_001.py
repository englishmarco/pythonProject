#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup

import sys
print(sys.path)
lottery_file = open("sort5.txt", "wb")

for history_index in range(1, 500):
    webstr = 'http://www.lottery.gov.cn/historykj/history_%d.jspx?_ltype=plw' % history_index
#    print(webstr.encode('utf-8'))

    response = urllib.request.urlopen(webstr)
    soup = BeautifulSoup(response, "html.parser")
    response.close()
    tables = soup.findAll('table')
    tab = tables[0]

    row=0
    for tr in tab.findAll('tr'):
        column = 0
        row=row+1
        if(row == 1 or row == 2):
            continue
        for td in tr.findAll('td'):
            if(column == 0 or column == 1 or column == 7):
                lotteryvalue = td.getText()+'\t'
                lottery_file.write(lotteryvalue.encode('utf-8'))
                #print(td.getText())
            column = column+1
        lottery_file.write("\n".encode('utf-8'))

lottery_file.close()