#coding=utf-8
import time

from framework.basepage import BasePage
from framework.browser_engine import BrowserEngine
from read_config_file import ReadConfigFile

class GetSubString(object):

    def get_search_result(self):

        rcf = ReadConfigFile()
        brow_url = rcf.get_value()
        browsertype = brow_url[0]
        browserurl = brow_url[1]
        print browsertype, browserurl

        browserengine = BrowserEngine(self)
        driver = browserengine.get_browser()

        basepage = BasePage(driver)
        basepage.open_url(browserurl)

        driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(1)
        search_result_string = driver.find_element_by_xpath("//span[@class='nums_text']").text
        print (search_result_string)

        new_string = search_result_string.split(u'约')[1]    #第一次切割得到  xxxx个， [1]代表切割右边部分
        print (new_string)
        last_result = new_string.split(u'个')[0]     #第二次切割，得到想要的数字 [0]代表切割参照数的左边部分
        print (last_result)


getstring = GetSubString()
getstring.get_search_result()