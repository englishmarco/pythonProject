
# Python 3.9
import threading

import json
import requests

def fun_timer():  #打印输出
    global timer  #定义变量
    timer = threading.Timer(60,fun_timer)   #60秒调用一次函数
#定时器构造函数主要有2个参数，第一个参数为时间，第二个参数为函数名

    timer.start()    #启用定时器
# 你复制的webhook地址
    url = "https://open.feishu.cn/open-apis/bot/v2/hook/672c6ca3-2f3d-4129-9034-eee299cf38d2"

    payload_message = {

        "msg_type": "text",
        "content": {

            "text": "下班"
        }
    }
    headers = {

        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload_message))
    print(response.text)

timer = threading.Timer(1,fun_timer)  #首次启动
timer.start()