"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import sys
cwd = os.getcwd()
sys.path.insert(1, cwd)


# from utils.locators import *
from test_argus.python_selenium.utils.locators import *
# print(HomePageLocators())

# GAMER_HOST = 'https://www.gamer.com.tw'

driver = webdriver.Chrome()
driver.get(GAMER_HOST)
driver.close()

"""

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import sys
import random
cwd = os.getcwd()
sys.path.insert(1, cwd)
from test_argus.python_selenium.utils.locators import *
from selenium.webdriver.common.keys import Keys
from test_argus.config.environment_variable import *

# from time import sleep

class TestGamercase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(GAMER_HOST)
        self.driver.maximize_window()
        # return super().setUp()

    def tearDown(self):
        self.driver.close()
        # return super().tearDown()

    # def test_run1(self):
    #     self.assertEqual(1,1)

    # def test_run2(self):
    #     # self.assertEqual(1,10)
    #     self.assertNotEqual(1,10)

    # def test_run3(self):
    #     element = self.driver.find_element(By.XPATH, HomePageLocators.SECTION_HOTHALACONTAINER)
    #     # 1
    #     # act = ActionChains(self.driver)
    #     # act.move_to_element(element).perform()
    #     ActionChains(self.driver).move_to_element(element).perform()

    #     # 2
    #     self.driver.execute_script('arguments[0].scrollIntoView();',element)
    #     # 3
    #     # self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def test_view_homepage(self):
        element = self.driver.find_element(By.XPATH, HomePageLocators.SECTION_ALLNEWS)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

        gnn_text = self.driver.find_element(
            By.XPATH, HomePageLocators.SECTION_ALLNEWS + "//div[@class='gnn-secondnews-block']/a[1]").text

        element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, HomePageLocators.ALLNEWS_RIGHT_ICON)))
        ActionChains(self.driver).move_to_element(element).click().perform()

        gnn_new_text = self.driver.find_element(
            By.XPATH, HomePageLocators.SECTION_ALLNEWS + "//div[@class='gnn-secondnews-block']/a[1]").text
        self.assertNotEqual(gnn_text, gnn_new_text)

        element = self.driver.find_element(By.XPATH, HomePageLocators.SECTION_BUYCONTAINER)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
        element = self.driver.find_element(By.XPATH, HomePageLocators.SECTION_HOTBOARDCONTAINER)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
        element = self.driver.find_element(By.XPATH, HomePageLocators.SECTION_HOTHALACONTAINER)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

        hala_text = self.driver.find_element(
            By.XPATH, HomePageLocators.SECTION_HOTHALA_LIST + "//tr[td[span[text()='1']]]//td[3]/a").text
        # print(hala_text)

        element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, HomePageLocators.SECTION_HOTHALA_OTHER)))
        ActionChains(self.driver).move_to_element(element).perform()

        hala_new_text = self.driver.find_element(
            By.XPATH, HomePageLocators.SECTION_HOTHALA_LIST + "//tr[td[span[text()='1']]]//td[3]/a").text
        # print(hala_new_text)
        self.assertNotEqual(hala_text, hala_new_text)

    def test_user_login(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, HomePageLocators.LOGIN)))
        element.click()

        element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, LoginPageLocators.ACCOUNT)))
        element.clear()
        element.send_keys(GAMER_USERNAME)

        element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, LoginPageLocators.PASSWORD)))
        element.clear()
        element.send_keys(GAMER_PASSWORD)


        # element = WebDriverWait(self.driver, 5).until(
        #     EC.element_to_be_clickable((By.XPATH, LoginPageLocators.SUBMIT)))
        # element.send_keys(Keys.ENTER)
        element = self.driver.find_element(By.XPATH, LoginPageLocators.SUBMIT)
        ActionChains(self.driver).move_to_element(element).click().perform()
        print("SUBMIT")

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, HomePageLocators.LOGIN_TOP_MYINFO_ANGLE_DOWN))).click()
        print("LOGIN_TOP_MYINFO_ANGLE_DOWN")

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, HomePageLocators.LOGIN_TOP_MYINFO_MSG)))
        print("LOGIN_TOP_MYINFO_MSG")

        username = self.driver.find_element(
            By.XPATH, HomePageLocators.LOGIN_TOP_MYINFO_MSG + "//a[@class='userid']").text.lower()
        self.assertEqual(username, GAMER_USERNAME)

    def test_search_halaboard(self):
        print("start")
        element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, HomePageLocators.TOP_SEARCH_TEXT)))
        element.clear()
        element.send_keys(SEARCH_BOARD_NAME)
        print("TOP_SEARCH_TEXT")

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, HomePageLocators.TOP_SEARCH_BUTTON))).click()
        print("TOP_SEARCH_BUTTON")

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, SearchPageLocaters.SEARCH_RESULT_WRAPPER)))
        print("SEARCH_RESULT_WRAPPER")
        elements = self.driver.find_elements(By.XPATH, SearchPageLocaters.SEARCH_RESULT_LIST)
        print("SEARCH_RESULT_LIST")

        for element in elements:
            if element.text == SEARCH_BOARD_NAME + "哈啦板- 巴哈姆特":
                element.click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, HalaPageLocaters.BOARD_IMG))).click()
        print("BOARD_IMG")
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, HalaPageLocaters.TAB_ICON)))
        print("TAB_ICON")

        elements = self.driver.find_elements(By.XPATH, HalaPageLocaters.TAB_ICON)
        num = len(elements)
        index = random.randint(1,num)
        elements[index-1].click()
        print("click ok")


if __name__ == '__main__':
    unittest.main()
