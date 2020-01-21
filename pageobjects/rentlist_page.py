#coding=utf-8

from framework.basepage import BasePage


class RentListPage(BasePage):

    # 以下是页眉的元素
    # 当前城市的位置
    city_name = "xpath=>//div[contains(@class,'adress fl pre do-hover')]//span"
    # 全部城市的悬浮框
    all_city = "xpath=>//div[@class='city-con']"
    # 联系客服
    service = u"xpath=>//span[contains(text(),'联系客服')]"
    # 微信客服图片
    wxpic = "xpath=>//img[@class='telUl-lt']"
    # 个人用户热线：
    hotline = u"xpath=>//div[contains(text(),'个人用户热线：')]"
    # 租售宝产品咨询热线：
    zsbhotline = u"xpath=>//div[contains(text(),'租售宝产品咨询热线：')]"
    # 首页
    index = "link_text=>首页"
    # 新房
    newhouse = "link_text=>新房"
    # 二手房
    sell = u"xpath=>//div[@class='fl']//a[@target='_blank'][contains(text(),'二手房')]"
    # 租房
    rent = u"xpath=>//div[@class='fl']//a[@target='_blank'][contains(text(),'租房')]"
    # 家居
    jiaju = "link_text=>家居"
    # 装修
    zhuangxiu = "link_text=>装修"
    # 华侨路茶坊
    bbs = "link_text=>华侨路茶坊"
    # 经纪人平台
    zsb = "link_text=>经纪人平台"
    # 注册
    register = "link_text=>注册"
    # 登录
    login = "link_text=>登录"
    # 手机淘房
    app = "link_text=>手机淘房"

    # 以下是导航栏的元素
    # 淘房logo
    logo = "xpath=>//a[@class='logo fl']"
    # 导航栏的二手房
    dh_sell = u"xpath=>//div[@class='navigation fl ml20']//a[@target='_blank'][contains(text(),'二手房')]"
    # 导航栏的小区
    dh_community = "link_text=>小区"
    # 导航栏的学区
    dh_school = "link_text=>学区"
    # 按揭服务
    loan = "link_text=>按揭服务"
    # 公寓
    aizuna = "link_text=>公寓"
    # 商铺
    shop = "xpath=>//div[@onclick=\"window.open('http://nj.sell.house365.com/district/x4.html')\"]"
    # 写字楼
    building = "link_text=>写字楼"
    # 发布房源
    publish = "link_text=>发布房源"
    # 修改删除房源
    modify = "link_text=>修改删除房源"
    # 问答
    ask = "link_text=>问答"
    # 论坛
    dh_bbs = "link_text=>论坛"


    #以下是右侧栏的icon
    # 发布出租
    yc_dh_pulish_rent = "xpath=>//a[@class='side-icon side-cz do-side']"
    # 发布求租
    yc_dh_pulish_rentQ = "xpath=>//a[@class='side-icon side-qz do-side']"
    # app下载页
    yc_dh_app = "xpath=>//a[@class='side-icon side-app do-side']"
    # 反馈页
    yc_dh_feedback = "xpath=>//a[@class='side-icon side-yj do-side']"


    #以下是左侧的icon
    # 帮你租房
    zc_help_rent = "xpath=>//div[@class='helpSlideT-msg']"
    # 帮你租房的大图
    zc_show_help_pic = "xpath=>//div[@class='helpSlideB-help jummto_publish']"
    # 帮你租房大图的关闭按钮
    zc_close_help_pic = "xpath=>//div[@class='helpSlideB-close']"

    # 关键词输入框
    search_input = u"xpath=>//div[@class='headSearch__box fl']//input[@placeholder='请输入小区名、位置或房源特征']"
    # 搜索按钮
    search_btn = "xpath=>//div[@class='headSearch__box fl']//div[@class='headSearch__btn fr']"
    # 搜索结果展示内容
    search_key = "xpath=>//div[@class='fliterBar_item']"

    # 地图找房按钮
    map_find = "xpath=>//a[@class='mapBtn fl']"

    # 个人房源的tab
    personal_tab = "xpath=>//div[contains(text(),'个人房源')]"

    def get_city_name(self):
        ele = self.fine_element(self.city_name)
        return ele

    def get_all_city(self):
        ele = self.fine_element(self.all_city)
        return ele

    #打开首页链接
    def click_shouye(self):
        self.click(self.index)

    #打开二手房链接
    def click_sell(self):
        self.click(self.sell)

    #打开租房链接
    def click_rent(self):
        self.click(self.rent)
        self.sleep(3)

    #打开新房链接
    def click_newhouse(self):
        self.click(self.newhouse)

    #打开家居链接
    def click_jiaju(self):
        self.click(self.jiaju)

    #打开装修链接
    def click_zhuangxiu(self):
        self.click(self.zhuangxiu)
        self.sleep(2)

    #打开华侨路茶坊链接
    def click_bbs(self):
        self.click(self.bbs)

    #打开经纪人平台链接
    def click_zsb(self):
        self.click(self.zsb)

    # 打开注册
    def click_register(self):
        self.click(self.register)

    # 打开登录
    def click_login(self):
        self.click(self.login)

    # 显示联系客服
    def get_service(self):
        return self.fine_element(self.service)

    # 是否存在微信图片
    def is_show_wxpic(self):
        return self.is_display(self.wxpic)

    # 是否存在个人客服热线
    def is_show_hotline(self):
        return self.is_display(self.hotline)

    # 是否存在租售宝热线
    def is_show_zsbhotline(self):
        return self.is_display(self.zsbhotline)

    # 打开手机淘房
    def click_app(self):
        self.click(self.app)

    # 打开淘房logo
    def click_logo(self):
        self.click(self.logo)

    # 打开导航栏的二手房
    def click_dh_sell(self):
        self.click(self.dh_sell)

    # 打开导航栏的小区
    def click_dh_community(self):
        self.click(self.dh_community)

    # 打开导航栏的学区
    def click_dh_school(self):
        self.click(self.dh_school)

    # 打开导航栏的按揭服务
    def click_dh_loan(self):
        self.click(self.loan)

    # 打开导航栏的公寓
    def click_dh_aizuna(self):
        self.click(self.aizuna)

    # 打开导航栏的商铺
    def click_dh_shop(self):
        self.click(self.shop)

    # 打开导航栏的写字楼
    def click_dh_building(self):
        self.click(self.building)

    # 打开导航栏的发布房源
    def click_dh_publish(self):
        self.click(self.publish)

    # 打开导航栏的修改删除房源
    def click_dh_modify(self):
        self.click(self.modify)

    # 打开导航栏的问答
    def click_dh_ask(self):
        self.click(self.ask)

    # 打开导航栏的论坛
    def click_dh_bbs(self):
        self.click(self.dh_bbs)

    # 打开右侧发布出租
    def click_yc_dh_publish(self):
        self.click(self.yc_dh_pulish_rent)

    # 打开右侧发布求租
    def click_yc_dh_publishQ(self):
        self.click(self.yc_dh_pulish_rentQ)

    # 打开右侧app下载页
    def click_yc_dh_app(self):
        self.click(self.yc_dh_app)

    # 打开右侧意见反馈页面
    def click_yc_dh_feedback(self):
        self.click(self.yc_dh_feedback)

    # 输入小区名称
    def send_community(self, text):
        self.type(self.search_input, text)

    # 点击搜索按钮
    def click_search_btn(self):
        self.click(self.search_btn)

    # 点击地图找房
    def click_map(self):
        self.click(self.map_find)

    # 点击个人房源tab
    def click_personal_tab(self):
        self.click(self.personal_tab)

    # 点击左侧帮你租房icon
    def click_help_rent(self):
        self.click(self.zc_help_rent)

    # 查看帮你租房的大图
    def show_help_rent(self):
        self.move_to_element(self.fine_element(self.zc_help_rent))

    # 点击租房的大图
    def click_help_pic(self):
        self.click(self.zc_show_help_pic)

    # 关闭帮你租房的大图
    def close_help_pic(self):
        self.click(self.zc_close_help_pic)