#coding=utf-8

import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import BaiduHomePage

class TestBaiduSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp代码，主要是测试的前提准备工作
        :return:
        """
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，基本为关闭浏览器
        :return:
        """
        cls.driver.quit()

    def Atest_baidu_search(self):
        """
        一定要test开头，把测试逻辑代码封装到一个test开头的方法里
        :return:
        """
        homepage = BaiduHomePage(self.driver)
        homepage.type_search('selenium')
        homepage.send_submit_btn()
        time.sleep(3)
        homepage.take_screenshot()
        try:
            assert 'selenium' in homepage.get_page_title()
            print  ('Test Pass.')
        except Exception as e:
            print ('Test Failed.', format(e))

    def Atest_search2(self):
        homepage = BaiduHomePage(self.driver)
        homepage.type_search('python')
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.take_screenshot()


if __name__ == '__main__':
    unittest.main()