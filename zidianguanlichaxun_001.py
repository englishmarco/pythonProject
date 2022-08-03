import requests
from locust import HttpUser,TaskSet,task,constant
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import django
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class chaxunzidian(TaskSet):
    @task(1)
    def post_list(self):

        #url = "http://192.168.1.111:10050/system/dict/list"

        payload='pageSize=20&pageNum=&orderByColumn=createTime&isAsc=desc&dictName=%20&dictType=%20&status=%20&params%5BbeginTime%5D=%20&params%5BendTime%5D='
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'JSESSIONID=c19db686-d55d-4e21-b2d7-335f62d7ec1e'
        }

        response = self.client.post("/system/dict/list", headers=headers, data=payload, verify = False)
        print(response.text)

    @task(2)
    def post_list1(self):
        # url = "http://192.168.1.111:10050/product/skuFiles/productInfo/list"
        payload1 = 'seriesnameId=&sku=&state=&tag=&isBarCodeFlag=&pageSize=20&pageNum=1&orderByColumn=&isAsc=asc'
        headers1 = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'JSESSIONID=c19db686-d55d-4e21-b2d7-335f62d7ec1e'
        }

        response1 = self.client.post("/product/skuFiles/productInfo/list", headers=headers1, data=payload1, verify=False)

        print(response1.text)

class websitUser(HttpUser):
    tasks = [chaxunzidian]
    min_wait = 3000  # 单位为毫秒
    max_wait = 6000  # 单位为毫秒



if __name__ == "__main__":
  import os
  os.system("locust -f zidianguanlichaxun_001.py --host=http://192.168.1.111:10050")