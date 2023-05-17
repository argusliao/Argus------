# 各頁面Xpath
class HomePageLocators():
    LOGIN = "//div[@class='TOP-my TOP-nologin']//li/a[text()='我要登入']"
    SECTION_ALLNEWS = "//div[@id='BA-center-id']//div[contains(@class,'gnn-allnews-block')]"
    ALLNEWS_RIGHT_ICON = "//div[contains(@class,'gnn-allnews-block')]//div[contains(@class,'is-right is-show')]"
    SECTION_BUYCONTAINER = "//div[@id='BA-center-id']//div[@id='buyContainer']"
    SECTION_HOTBOARDCONTAINER = "//div[@id='BA-center-id']//div[@id='hotboardContainer']"
    SECTION_HOTHALACONTAINER = "//div[@id='BA-center-id']//div[@id='hothalaContainer']"
    SECTION_HOTHALA_OTHER = "//div[@id='hothalaContainer']//li/a[@id='hothala_other']"
    SECTION_HOTHALA_LIST = "//div[@id='hothala']"
    LOGIN_TOP_MYINFO_ANGLE_DOWN = "//div[@class='TOP-my']//a[@id='topBar_member']/i"
    LOGIN_TOP_MYINFO_MSG = "//div[@id='topBarMsg_member']"
    LOGIN_TOP_MYINFO_MSG_USERNAME = LOGIN_TOP_MYINFO_MSG + "//a[@class='userid']"
    TOP_SEARCH_TEXT = "//td[@id='gs_tti50']/input"
    TOP_SEARCH_BUTTON = "//td[contains(@class,'search-button')]"

class LoginPageLocators():
    LOGIN_FORM = '//form[@id="form-login"]'
    ACCOUNT = '//input[@name="userid"]'
    PASSWORD = '//div/input[@name="password"]'
    SUBMIT = '//div/a[@id="btn-login"]'

class SearchPageLocaters():
    SEARCH_RESULT_WRAPPER = "//div[@class='gsc-wrapper']"
    SEARCH_RESULT_LIST = "//div[@class='gs-title']/a[@class='gs-title']"

class HalaPageLocaters():
    BOARD_IMG = "//div[contains(@class,'FM-abox1')]"
    TAB_ICON = "//ul[@class='b-tags']/li"
    FORUM_LIST = "//tr[contains(@class, 'b-list-item')][not(contains(@class, 'is-del'))]"
    FORUM_LIST_NOT_STICKY = FORUM_LIST + "[not(contains(@class,'b-list__row--sticky'))]"
    FORUM_TITLE = "//div[@class='c-post__header']/h1"
    FORUM_POST_BODY = "//div[@class='c-post__body']"
