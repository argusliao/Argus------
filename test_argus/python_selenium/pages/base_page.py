from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, xpath: str) -> WebElement:    # 需要return才要註記 -> WebElement
        return self.driver.find_element(By.XPATH, xpath)

    def get_elements(self, xpath: str) -> WebElement:
        return self.driver.find_elements(By.XPATH, xpath)

    def open(self, url):
        self.driver.get(url)

    def scroll_element_to_view(self, xpath: str, timeout=5):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        ActionChains(self.driver).move_to_element(element).perform()

    def scroll_element_to_view_and_click(self, xpath: str, timeout=5):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        ActionChains(self.driver).move_to_element(element).click().perform()

    def wait_element_and_click(self, xpath: str, timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

    def input_text(self, xpath: str, input_str: str, timeout=5):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.clear()
        element.send_keys(input_str)

    def wait_element_visibility(self, xpath: str, timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))
