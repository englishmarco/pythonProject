import requests
from locust import HttpUser,TaskSet,task,constant
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import django
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class productselect(TaskSet):
  @task(1)
  def post_list(self):
    url = "http://192.168.1.111:10050/product/skuFiles/productInfo/list"

    payload='seriesnameId=&sku=&state=&tag=&isBarCodeFlag=&pageSize=20&pageNum=1&orderByColumn=&isAsc=asc'
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Cookie': 'JSESSIONID=ec6ae203-f379-48ef-bdda-740004cca21f'
      }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

class websitUser(HttpUser):
    tasks = [productselect]
    min_wait = 3000  # 单位为毫秒
    max_wait = 6000  # 单位为毫秒


if __name__ == "__main__":
  import os
  os.system("locust -f productlist_001.py --host=https://192.168.1.111:10050")