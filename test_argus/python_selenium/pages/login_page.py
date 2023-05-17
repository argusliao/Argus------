import sys
import os
cwd = os.getcwd()
sys.path.insert(1, cwd)
from test_argus.python_selenium.pages.base_page import *
from test_argus.python_selenium.utils.locators import *


class LoginPage(BasePage):
    def input_account(self, account):
        self.input_text(LoginPageLocators.ACCOUNT, account)

    def input_password(self, password):
        self.input_text(LoginPageLocators.PASSWORD, password)

    def click_login_button(self):
        self.scroll_element_to_view_and_click(LoginPageLocators.SUBMIT)

    def user_login(self, account, password):
        self.input_account(account)
        self.input_password(password)
        self.click_login_button()
