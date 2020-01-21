#coding=utf-8

from selenium import webdriver
import ConfigParser
import os.path
from framework.logger import Logger

logger = Logger(logger = "BrowserEngine").getlog()

class BrowserEngine(object):
    """
    定义一个浏览器引擎类，根据browser_type来控制启动不同的浏览器，支持ie、firefox、chrome
    """

    dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'
    firefox_driver_path = dir + '/tools/geckobject.exe'

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):
        config = ConfigParser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        #config.read(file_path, encoding='utf-8')

        browser = config.get("browserType", "browserName")
        logger.info("you had select %s browse."% browser)
        url = config.get("testServer", "URL")
        logger.info("the test server url is : %s" % url)

        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("Start Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("Start IE browser.")

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds")
        return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser")
        self.driver.quit()