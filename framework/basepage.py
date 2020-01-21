#coding=utf-8

import os
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from framework.logger import Logger

logger = Logger(logger='BasePage').getlog()


class BasePage(object):
    """
    讲Selenium方法封装到该类
    """

    def __init__(self, driver):
        """
        构造函数，参数为driver
        :param driver:
        :param driver:
        """
        self.driver = driver

    def back(self):
        """
        浏览器后退
        :return:
        """
        self.driver.back()
        logger.info("back on the page.")

    def forward(self):
        """
        浏览器前进
        :return:
        """
        self.driver.forward()
        logger.info("forward on the page")

    def wait(self, seconds):
        """
        隐式等待
        :param seconds:
        :return:
        """
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds" % seconds)

    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the broser with %s"%e)


    def open_url(self, url):
        """
        打开浏览器url
        :param url:
        :return:
        """
        self.driver.get(url)

    def quit_browser(self):
        """
        退出浏览器
        :param:
        :return:
        """
        self.driver.quit()

    def take_screenshot(self):
        """
        截图并保存在根目录下的screenshots文件夹下
        :return:
        """
        file_path = os.path.dirname(os.getcwd()) + '/Screenshots/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("take screenshot and save to folder : /Screenshots")
        except Exception as e:
            logger.error("Failed to take screenshot! %s" %e)
            #self.take_screenshot()


    def fine_element(self, selector):
        """
        定位元素
        形如：
        submit_btn = "id => su"
        login_link = "xpath => //*[id='u1']/a[7]"
        :param selector:
        :return:
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("Had find the element \' %s\' sucessful "
                            "by %s via value: %s"%(element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("No Such Element Exception: %s"% e)
                self.take_screenshot()
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value : %s" %(element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("No Such Element Exception: %s" %e)
                self.take_screenshot()
        elif selector_by == "s" or selector_by == "selector_selector":
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    def type(self, selector, text):
        """
        输入文本内容
        :param selector:
        :param text:
        :return:
        """
        el = self.fine_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inutBox " % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.take_screenshot()

    def clear(self,selector):
        """
        清除文本
        :return:
        """
        el = self.fine_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.take_screenshot()

    def click(self, selector):
        """
        点击元素
        :param selector:
        :return:
        """
        el = self.fine_element(selector)
        try:
            el.click()
            logger.info("The element \' %s \' was clicked." %el.text)
        except NameError as e:
            logger.error("Failed to click the element with %s " % e)
            self.take_screenshot()

    def is_display(self, selector):
        """
        是否存在seletor
        :param selector:
        :return:
        """
        try:
            el = self.fine_element(selector)
            logger.info("The element \' %s \' display."%el.text)
            return True
        except NameError as e:
            logger.error("Failed display the element %s " % e)
            self.take_screenshot()
            return False

    def get_page_title(self):
        """
        获取网页标题
        :return:
        """
        tle = self.driver.title
        logger.info("Get the Current page title %s "%tle)
        return tle

    def move_to_element(self, element):
        """
        鼠标悬浮于某个元素之后的内容
        :param element:
        :return:
        """
        actionchain = ActionChains(self.driver)
        actionchain.move_to_element(element).perform()
        self.take_screenshot()
        logger.info("show the element pop ")

    def switch_widows(self, isclose = False):
        """
        切换到新打开的tab页面,#同时关闭原有的tab
        :param:isclose
        :return:
        """
        print("current_window_handle:", self.driver.current_window_handle)
        handles = self.driver.window_handles
        print("all handles:", handles)

        for handle in handles:
            if handle != self.driver.current_window_handle:
                print("switch to second window:", handle)
                #self.driver.close()
                if isclose == True:
                    self.driver.close()

                self.driver.switch_to.window(handle)
                break
        time.sleep(2)

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)
