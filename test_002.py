import requests


url = "http://192.168.1.111:10050/product/skuFiles/productInfo/add"

payload={'seriesnameId': '708',
'sku' : 'kk789789',
'tag': '',
'codeNumber': '101010100088',
'changes': '',
'nameRule': '',
'country': '',
'picture': '',
'designer': '',
'notes': '',
'memo': ''}
files=[

]
headers = {
  'Cookie': 'JSESSIONID=62ab10d3-09ae-4df6-ba05-3fdd60528201'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
