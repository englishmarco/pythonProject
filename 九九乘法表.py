import requests
import lxml.html as lh
import pandas as pd

url='https://www.lottery.gov.cn/kj/kjlb.html?plw'
#Create a handle, page, to handle the contents of the website
page = requests.get(url)
#Store the contents of the website under doc
doc = lh.fromstring(page.content)
#Parse data that are stored between of html
tr_elements = doc.xpath('//tr')
[len(T) for T in tr_elements[:12]]

tr_elements = doc.xpath('//tr')

#Create empty list

col=[]

i=0

#For each row, store each first element (header) and an empty list

for t in tr_elements[0]:
    i+=1

name=t.text_content()

print ('%d:"%s"'%(i,name))
col.append((name,[]))
