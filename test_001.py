# coding=utf-8
import requests
from locust import HttpUser,TaskSet,task,constant
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import django
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



class HangOutTaskSet(TaskSet):

    @task
    def hang_out(self):
        print("the player is hanging out")


class PlayGameTaskSet(TaskSet):

    @task
    def play(self):
        print("the player is playing game")


class PlayerOwn(HttpUser):
    weight = 10
    task_set = HangOutTaskSet
    host = "http://www.baidu.com"
    min_wait = 10000
    max_wait = 10000


class PlayerTwo(HttpUser):
    weight = 90
    task_set = PlayGameTaskSet
    host = "http://www.baidu.com"
    min_wait = 10000
    max_wait = 10000


def play_one(self):
    print("play_one")


def play_two(self):
    print("play_two")


class PlayGameTaskSet(TaskSet):
    tasks = [(play_one, 5), play_two]

    @task
    def play(self):
        print("the player is playing game")


class PlayerTwo(HttpUser):
    weight = 90
    task_set = PlayGameTaskSet
    host = "http://www.baidu.com"
    min_wait = 100
    max_wait = 100