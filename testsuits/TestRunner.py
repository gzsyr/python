#coding=utf-8

import HTMLTestRunner
import os
import unittest
import time

from test_rent_list import TestRentList

#设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
#获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime((time.time())))

#设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = file(HtmlFile, 'wb')

#构建suite, 添加所有test用例
suite = unittest.TestLoader().discover("testsuits")

# 添加指定test用例
# suite = unittest.TestSuite()
# suite.addTest(TestRentList("test_zc_dh_help_close"))
# suite.addTest(TestRentList("test_click_map_find"))

if __name__ == '__main__':
    #初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream = fp, title = u"房源列表页面测试报告", description = u"用例执行结果")
    #开始执行测试套件
    runner.run(suite)