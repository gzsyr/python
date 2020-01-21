# coding=utf-8

import ConfigParser
import os

class ReadConfigFile(object):

    def get_value(self):
        root_dir = os.path.dirname(os.path.abspath('.'))    # 获取根目录的相对路径
        print root_dir

        config = ConfigParser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/pythonRent/config/config.ini'
        config.read(file_path)

        browser = config.get("browserType", "browserName")
        url = config.get("testServer", "URL")

        return (browser, url)   # 返回一个元组


#trcf = ReadConfigFile()
#print trcf.get_value()