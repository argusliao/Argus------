import sys
import os
cwd = os.getcwd()
sys.path.insert(1, cwd)
import random
from test_argus.python_selenium.pages.base_page import *
from test_argus.python_selenium.utils.locators import *


class BoardPage(BasePage):
    def click_board_image(self):
        self.wait_element_and_click(HalaPageLocaters.BOARD_IMG)
        self.wait_element_visibility(HalaPageLocaters.TAB_ICON)

    def click_board_tags_by_random(self):
        elements = self.get_elements(HalaPageLocaters.TAB_ICON)
        num = len(elements)
        index = random.randint(1,num)
        elements[index-1].click()

    def click_forum_item_in_not_sticky(self):
        self.wait_element_and_click(HalaPageLocaters.FORUM_LIST_NOT_STICKY + "[1]")
        self.wait_element_visibility(HalaPageLocaters.FORUM_TITLE)
        self.wait_element_visibility(HalaPageLocaters.FORUM_POST_BODY)
