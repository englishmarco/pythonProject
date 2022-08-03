from hashlib import new
from webdriver import selenium
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert


class a():
    name = "ceshi"


options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
b = webdriver.Chrome(chrome_options=options)
b.maximize_window()
b.get("http://erp-dev.geekbuy.cn/Home/Index")
b.find_element_by_name("username").send_keys("1456")
b.find_element_by_name("password").send_keys("a123456#")
b.find_element_by_id("btnLogin").click()
time.sleep(2)

#鼠标悬停到订单管理页面
move = b.find_element_by_xpath("//*[@id='navbar-container']/div[3]/ul/li[3]/font")
ActionChains(b).move_to_element(move).perform()
b.find_element_by_xpath("//*[@id='navbar-container']/div[3]/ul/li[3]/ul/li[2]/dl/dd[5]/a/span").click()
time.sleep(2)
b.find_element_by_class_name("fa-refresh").click()
#鼠标悬停到订单录入页面
move = b.find_element_by_xpath("//*[@id='navbar-container']/div[3]/ul/li[3]/font")
ActionChains(b).move_to_element(move).perform()
b.find_element_by_xpath("//*[@id='navbar-container']/div[3]/ul/li[3]/ul/li[1]/dl/dd[1]/a/span").click()
time.sleep(1)
#打开新的标签页
js = 'window.open("https://pc-dev.geekbuy.cn:4431/dist/InputOrder.html#/UnSplitPackage")'
b.execute_script(js)
handles = b.window_handles
b.switch_to.window(handles[1])
#切换标签页
handles = b.window_handles
b.switch_to.window(handles[0])
b.switch_to.window(handles[1])

time.sleep(2)

#选择销售平台
b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[2]/div[1]/div[2]/div/p/div/div[1]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/input').send_keys("geekbuying")
b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[2]/div[1]/div[2]/div/p/div/div[1]/div/div/div[1]/div[1]/div[2]/div/div[2]/ul[2]/li[1]').click()
#选择店铺
b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[2]/div[1]/div[2]/div/p/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/input').send_keys("geekbuying01")
b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[2]/div[1]/div[2]/div/p/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[2]/ul[2]/li[1]').click()
#选择销售类型
b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[2]/div[1]/div[2]/div/p/div/div[1]/div/div/div[1]/div[3]/div[2]/div/div[1]/div/input').click()
b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[2]/div[1]/div[2]/div/p/div/div[1]/div/div/div[1]/div[3]/div[2]/div/div[2]/ul[2]').click()
b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[2]/div[1]/div[2]/div/p/div/div[1]/div/div/div[1]/div[3]/div[2]/div/div[2]/ul[2]/li[1]').click()
#输入订单号
b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[2]/div[1]/div[2]/div/p/div/div[1]/div/div/div[1]/div[4]/div[2]/div/input').send_keys("asdjdsahkh123qzxc")
#币种
b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[2]/div[1]/div[2]/div/p/div/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/div/input').click()

b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[2]/div[1]/div[2]/div/p/div/div[1]/div/div/div[2]/div[1]/div[2]/div/div[2]/ul[2]/li[1]').click()
#输入订单金额
b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[2]/div[1]/div[2]/div/p/div/div[1]/div/div/div[2]/div[2]/div[2]/div/input').send_keys("100.65")
#输入运费
b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[2]/div[1]/div[2]/div/p/div/div[1]/div/div/div[2]/div[3]/div[2]/div/input').click()
#选择线上线下
b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[2]/div[1]/div[2]/div/p/div/div[1]/div/div/div[3]/div[3]/div[2]/div/div[1]/div/input').click()
b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[2]/div[1]/div[2]/div/p/div/div[1]/div/div/div[3]/div[3]/div[2]/div/div[2]/ul[2]').click()
b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[2]/div[1]/div[2]/div/p/div/div[1]/div/div/div[3]/div[3]/div[2]/div/div[2]/ul[2]/li[2]').click()
#收件人
b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[2]/div[2]/div[2]/div/p/div/div[1]/div[2]/div/input').send_keys(1)
#详细地址
b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[2]/div[2]/div[2]/div/p/div/div[2]/div[2]/div/input').send_keys(2)
#门牌号
b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[2]/div[2]/div[2]/div/p/div/div[3]/div[2]/div/input').send_keys(3)
#税号
b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[2]/div[2]/div[2]/div/p/div/div[4]/div[2]/div/input').send_keys(4)
#城市
b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[2]/div[2]/div[2]/div/p/div/div[5]/div[2]/div/input').send_keys(5)
#州省
b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[2]/div[2]/div[2]/div/p/div/div[6]/div[2]/div/input').send_keys(6)
#邮编
b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[2]/div[2]/div[2]/div/p/div/div[7]/div[2]/div/input').send_keys(7)
#国别
b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[2]/div[2]/div[2]/div/p/div/div[9]/div[2]/div/div[1]/div/input').click()

b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[2]/div[2]/div[2]/div/p/div/div[9]/div[2]/div/div[2]/ul[2]/li[1]').click()
#电话
b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[2]/div[2]/div[2]/div/p/div/div[10]/div[2]/div/input').send_keys(8)
#数量
b.find_element_by_xpath('//*[@id="productTBL"]/div/div[2]/table/tbody/tr/td[8]/div/div/input').send_keys("2")
#销售单价
b.find_element_by_xpath('//*[@id="productTBL"]/div/div[2]/table/tbody/tr/td[12]/div/div/input').send_keys("10")
#sku
b.find_element_by_xpath('//*[@id="productTBL"]/div/div[2]/table/tbody/tr/td[1]/div/div/input').send_keys("235566")
#起运地
b.find_element_by_xpath('//*[@id="productTBL"]/div/div[2]/table/tbody/tr/td[2]/div/div/div[1]/div/input').send_keys("波兰华沙 | PLWS")
b.find_element_by_xpath('//*[@id="productTBL"]/div/div[2]/table/tbody/tr/td[2]/div/div/div[2]/ul[2]').click()

#点击添加
b.find_element_by_xpath('//*[@id="productTBL"]/div/div[2]/table/tbody/tr/td[14]/div/div/button[1]/span').click()
b.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(2)
#选择邮路
b.find_element_by_xpath('//*[@id="SplitPackage"]/div[1]/div[2]/div/button[1]/span').click()
time.sleep(2)
b.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[1]').click()

time.sleep(2)
#选择快捷申报
b.find_element_by_xpath('//*[@id="SplitPackage"]/div[2]/div[2]/div/div/div[2]/div/div/button[1]').click()
#保存并下单
b.find_element_by_xpath('//*[@id="app"]/div/div/content/div/div/div[3]/div/div/div[2]/button[2]').click()

time.sleep(5)
#对弹出框进行操作
ale=Alert(b)
print(ale.text) #打印 弹出框文本内容
ale.accept()

