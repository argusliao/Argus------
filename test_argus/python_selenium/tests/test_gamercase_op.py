import unittest
import os
import sys
cwd = os.getcwd()
sys.path.insert(1, cwd)
from test_argus.config.environment_variable import *
from test_argus.python_selenium.pages.board_page import *
from test_argus.python_selenium.pages.browser import *
from test_argus.python_selenium.pages.home_page import *
from test_argus.python_selenium.pages.login_page import *
from test_argus.python_selenium.pages.search_page import *

class TestGamercase(unittest.TestCase):
    def setUp(self):
        self.browser = Browser()
        self.driver = self.browser.driver
        """
        1.繼承初始化後用變數homepage接起來，這樣之後不用在建page，省記憶體與效能，之後就用self.homepage
        2.沒初始化城市不知道你寫的屬性
        """
        self.homepage = HomePage(self.driver)
        self.homepage.open(GAMER_HOST)

    def tearDown(self):
        self.browser.close_browser()
        # self.homepage = None

    def test_view_homepage(self):
        self.homepage.review_allnews()
        self.homepage.review_hotboard()
        self.homepage.review_hothalatopic()
        self.homepage.review_hothalatopic_other()

    def test_user_login(self):
        self.homepage.click_login_button()
        self.loginpage = LoginPage(self.driver)
        self.loginpage.user_login(GAMER_USERNAME, GAMER_PASSWORD)
        self.homepage.open_topbar_userinfo()
        username = self.homepage.get_element(HomePageLocators.LOGIN_TOP_MYINFO_MSG_USERNAME).text.lower()
        self.assertEqual(username, GAMER_USERNAME)

    def test_search_halaboard(self):
        self.homepage.input_text(HomePageLocators.TOP_SEARCH_TEXT, SEARCH_BOARD_NAME)
        self.homepage.wait_element_and_click(HomePageLocators.TOP_SEARCH_BUTTON)
        self.searchpage = SearchPage(self.driver)
        self.searchpage.wait_search_list_visibility()
        self.searchpage.click_result_with_halaboard(SEARCH_BOARD_NAME)
        self.boardpage = BoardPage(self.driver)
        self.boardpage.click_board_image()
        self.boardpage.click_board_tags_by_random()
        list_title = self.boardpage.get_element(
            HalaPageLocaters.FORUM_LIST_NOT_STICKY + "[1]//td[2]//p[@href]").text
        self.boardpage.click_forum_item_in_not_sticky()
        forum_title = self.boardpage.get_element(HalaPageLocaters.FORUM_TITLE).text
        self.assertEqual(list_title, forum_title)


if __name__ == '__main__':
    unittest.main()
