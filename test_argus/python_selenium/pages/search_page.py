import sys
import os
cwd = os.getcwd()
sys.path.insert(1, cwd)
from test_argus.python_selenium.pages.base_page import *
from test_argus.python_selenium.utils.locators import *


class SearchPage(BasePage):
    def wait_search_list_visibility(self):
        self.wait_element_visibility(SearchPageLocaters.SEARCH_RESULT_WRAPPER)

    def click_result_with_halaboard(self, board_name: str):
        elements = self.get_elements(SearchPageLocaters.SEARCH_RESULT_LIST)

        for element in elements:
            if element.text == board_name + "哈啦板- 巴哈姆特":
                element.click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

    # def click_result_with_forum(self):
    #     pass
