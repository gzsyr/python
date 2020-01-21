#coding=utf-8

from pageobjects.rentlist_page import RentListPage
import unittest
from framework.browser_engine import BrowserEngine
import time

class TestRentList(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        brower = BrowserEngine(cls)
        cls.driver = brower.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    """以下是页眉栏目的相关点击"""

    def test_common_get_city(self):
        """
        查看当前城市是否为：南京
        :return:
        """
        rlpage = RentListPage(self.driver)
        name = rlpage.get_city_name().text
        if (name == u'南京'):
            print ('Test Pass.')
        else:
            print ('Test Fail.')

    def test_common_show_all_city(self):
        """
        查看全部城市
        :return:
        """
        rlpage = RentListPage(self.driver)
        ele = rlpage.get_city_name()
        rlpage.move_to_element(ele)
        rlpage.sleep(2)

        hot_name = rlpage.get_all_city()
        try:
            assert u"热门城市" in hot_name.text
            print ('Test Pass.')
        except Exception as e:
            print ("Test Fail.", format(e))
            raise e

    def test_common_open_index(self):
        """
        点击首页并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_shouye()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"南京房地产家居门户网站" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切换回原来的tab, 并关闭原来的tab
            raise e

    def test_common_open_sell(self):
        """
        点击二手房并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_sell()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"南京二手房网" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切换回原来的tab, 并关闭原来的tab
            raise e

    def test_common_open_rent(self):
        """
        点击租房，并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_rent()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"南京房屋出租信息" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
            raise e

    def test_common_open_newhouse(self):
        """
        点击新房，并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_newhouse()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"南京新房" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切换回原来的tab, 并关闭原来的tab
            raise e

    def test_common_open_jiaju(self):
        """
        点击家居，并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_jiaju()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"南京家居装修" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切换回原来的tab, 并关闭原来的tab
            raise e

    def test_common_open_zhuangxiu(self):
        """
        点击装修，并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_zhuangxiu()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"南京家居首页" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切换回原来的tab, 并关闭原来的tab
            raise e

    def test_common_open_bbs(self):
        """
        点击华侨路茶坊，并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_bbs()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"南京业主论坛" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切换回原来的tab, 并关闭原来的tab
            raise e

    def test_common_open_zsb(self):
        """
        点击经纪人平台，并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_zsb()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"租售宝登录页" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切换回原来的tab, 并关闭原来的tab
            raise e

    def test_common_open_register(self):
        """
        点击注册，并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_register()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"用户注册" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切换回原来的tab, 并关闭原来的tab
            raise e

    def test_common_open_login(self):
        """
        点击登录，并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_login()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"登录" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切换回原来的tab, 并关闭原来的tab
            raise e

    def test_common_show_service(self):
        """
        鼠标滑动联系方式，悬浮显示内容
        :return:
        """
        rlpage = RentListPage(self.driver)
        ele = rlpage.get_service()
        rlpage.move_to_element(ele)

        if(False == rlpage.is_show_wxpic()):
            print ("Test Failed.- no weixin pic ")
        elif (False == rlpage.is_show_hotline()):
            print ("Test Failed.- no person hotline ")
        elif (False == rlpage.is_show_zsbhotline()):
            print ("Test Failed.- no zsb hotline ")
        else:
            print ("Test Pass.")


    def test_common_open_phone(self):
        """
        点击鼠标滑动悬浮显示联系方式手机淘房，并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_app()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"365淘房APP官网下载" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切换回原来的tab, 并关闭原来的tab
            raise e


    """以下是导航栏的内容点击"""

    def test_index_open_sell(self):
        """
        点击二手房，并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_dh_sell()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"南京二手房买卖" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
            raise e

    def test_index_open_community(self):
        """
        点击小区，并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_dh_community()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"南京二手房买卖" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
            raise e

    def test_index_open_school(self):
        """
        点击学校，并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_dh_school()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"南京学区房" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
            raise e

    def test_index_open_loan(self):
        """
        点击按揭，并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_dh_loan()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"南京二手房贷款" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
            raise e

    def test_index_open_aizuna(self):
        """
        点击出租，并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_dh_aizuna()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"南京公寓出租" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
            raise e

    def test_index_open_shop(self):
        """
        点击商铺，并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_dh_shop()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"南京商铺投资" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
            raise e

    def test_index_open_building(self):
        """
        点击写字楼，并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_dh_building()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"南京写字楼投资" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
            raise e

    def test_index_open_publish(self):
        """
        点击发布，并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_dh_publish()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"南京二手房交易" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
            raise e

    def test_index_open_modify(self):
        """
        点击修改删除房源，并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_dh_modify()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"南京二手房交易" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
            raise e

    def test_index_open_ask(self):
        """
        点击租房，并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_dh_ask()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"南京房产信息咨询" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
            raise e

    def test_index_open_bbs(self):
        """
        点击论坛，并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_dh_bbs()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"二手房交易-365淘房华侨路茶坊" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
            raise e

    def test_yc_dh_open_publish(self):
        """
        点击右侧发布出租iocn，并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_yc_dh_publish()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"二手房交易-365淘房华侨路茶坊" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
            raise e

    def test_yc_dh_open_publishQ(self):
        """
        点击右侧发布求租iocn，并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_yc_dh_publishQ()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"二手房交易-365淘房华侨路茶坊" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
            raise e

    def test_yc_dh_open_app(self):
        """
        点击右侧app应用下载iocn，并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_yc_dh_app()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"二手房交易-365淘房华侨路茶坊" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
            raise e

    def test_yc_dh_open_feedback(self):
        """
        点击右侧意见反馈iocn，并打开
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_yc_dh_feedback()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        print rlpage.get_page_title()
        try:
            assert u"二手房交易-365淘房华侨路茶坊" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print ('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
            raise e

    def test_search_community(self):
        """
        搜索，关键词为“小区”
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.send_community(u"凤凰和美")
        rlpage.sleep(10)
        rlpage.click_search_btn()
        rlpage.sleep(10)
        try:
            assert rlpage.fine_element(rlpage.search_key)
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))
            raise e

    def test_click_map_find(self):
        """
        点击“地图找房”
        :return: 
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_map()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        try:
            assert u"南京地图找房" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
            raise e

    def test_click_personal_tab(self):
        """
        点击“个人房源”
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_personal_tab()

        try:
            assert u"个人" in rlpage.fine_element(rlpage.search_key)
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))
            raise e

    def test_zc_dh_help_rent(self):
        """
        点击左侧“帮你租房”
        :return:
        """
        rlpage = RentListPage(self.driver)
        rlpage.click_help_rent()

        rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
        try:
            assert u"南京出租房" in rlpage.get_page_title()
            print ('Test Pass.')
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
        except Exception as e:
            print('Test Fail.', format(e))
            rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
            raise e

    def test_zc_dh_help_close(self):
        """
        鼠标滑过“帮你租房”
        :return:
        """
        f = False

        rlpage = RentListPage(self.driver)
        rlpage.show_help_rent()

        try:
            assert u"365租房助手" in rlpage.fine_element(rlpage.zc_show_help_pic).text
            print ('Show PIC Test Pass.')
            f = True
        except Exception as e:
            print ('Test Fail.', format(e))
            raise e

        if f == True:
            rlpage.click_help_pic()
            rlpage.switch_widows()  # 切换到新打开的tab，去check打开的页面正确与否
            try:
                assert u"南京出租房" in rlpage.get_page_title()
                print ('Open PIC Test Pass.')
                rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
            except Exception as e:
                print('Test Fail.', format(e))
                rlpage.switch_widows(isclose=True)  # 切 换回原来的tab, 并关闭原来的tab
                raise e

            rlpage.close_help_pic()
            rlpage.sleep(2)

