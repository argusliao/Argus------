import sys
import os
cwd = os.getcwd()
sys.path.insert(1, cwd)
from test_argus.python_selenium.pages.base_page import *
from test_argus.python_selenium.utils.locators import *


"""
繼承BasePage後只有方法要加self，呼叫時不用
"""
class HomePage(BasePage):
    def review_allnews(self):
        self.scroll_element_to_view(HomePageLocators.SECTION_ALLNEWS)
        self.scroll_element_to_view_and_click(HomePageLocators.ALLNEWS_RIGHT_ICON)

    def review_hotboard(self):
        self.scroll_element_to_view(HomePageLocators.SECTION_BUYCONTAINER)

    def review_hothalatopic(self):
        self.scroll_element_to_view(HomePageLocators.SECTION_HOTBOARDCONTAINER)

    def review_hothalatopic_other(self):
        self.scroll_element_to_view(HomePageLocators.SECTION_HOTHALACONTAINER)
        self.scroll_element_to_view(HomePageLocators.SECTION_HOTHALA_OTHER)

    def click_login_button(self):
        self.wait_element_and_click(HomePageLocators.LOGIN)

    def open_topbar_userinfo(self):
        self.wait_element_and_click(HomePageLocators.LOGIN_TOP_MYINFO_ANGLE_DOWN)
        self.wait_element_visibility(HomePageLocators.LOGIN_TOP_MYINFO_MSG)
