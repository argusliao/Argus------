from selenium import webdriver


class Browser():
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()    # 開啟瀏覽器
    #     self.driver.maximize_window()

    def close_browser(self):
        # self.driver.close()
        self.driver.quit()
