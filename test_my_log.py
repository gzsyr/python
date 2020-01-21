#coding=utf-8

import time
from selenium import webdriver
from framework.logger import Logger

mylogger = Logger(logger = 'TestMyLogger').getlog()

class TestMyLog(object):

    def print_log(self):
        driver = webdriver.Firefox()
        mylogger.info("打开浏览器")

        driver.maximize_window()
        mylogger.info("最大化浏览器窗口")

        driver.get("https://www.baidu.com")
        mylogger.info("打开百度首页")

        time.sleep(1)
        mylogger.info("暂停一秒")

        driver.quit()
        mylogger.info("关闭并退出浏览器")

testlog = TestMyLog()
testlog.print_log()
