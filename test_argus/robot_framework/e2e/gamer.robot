*** Settings ***
Documentation  巴哈姆特測試案例
Library  String
Library  SeleniumLibrary
Variables  ../../config/environment_variable.py
Test Setup  前往：巴哈首頁
Test Teardown  Close All Browsers


*** Test Cases ***
開啟並瀏覽巴哈首頁
  瀏覽：首頁

會員登入
  點選：登入
  輸入：帳號
  輸入：密碼
  點擊：登入按鈕
  檢查：登入完成
  點選：登出

進行會員簽到
  點選：登入
  輸入：帳號
  輸入：密碼
  點擊：登入按鈕
  前往：每日簽到按鈕
  點選：簽到

搜尋哈拉版
  輸入：關鍵字搜尋哈拉版  ${SEARCH_BOARD_NAME}
  點選：搜尋結果
  點選：進板圖


*** Keywords ***
前往：巴哈首頁
  Open Browser  ${GAMER_HOST}  Chrome
  Wait Until Element Is Visible  //div[@class="TOP-my TOP-nologin"]//li/a[text()="我要登入"]

瀏覽：首頁
  Scroll Element Into View  //div[@id="BA-center-id"]//div[contains(@class,"gnn-allnews-block")]
  Click Element  //div[contains(@class,"gnn-allnews-block")]//div[contains(@class,"is-right is-show")]  # TODO 切換後驗證是否已換頁
  Scroll Element Into View  //div[@id="BA-center-id"]//div[@id="buyContainer"]
  Scroll Element Into View  //div[@id="BA-center-id"]//div[@id="hotboardContainer"]
  Scroll Element Into View  //div[@id="BA-center-id"]//div[@id="hothalaContainer"]
  Click Element  //div[@id="hothalaContainer"]//li/a[@id="hothala_other"]

點選：登入
  Wait Until Element Is Visible  //div[@class="TOP-my TOP-nologin"]//li/a[text()="我要登入"]
  Click Element  //div[@class="TOP-my TOP-nologin"]//li/a[text()="我要登入"]
  Wait Until Element Is Visible  //form[@id="form-login"]

輸入：帳號
  [Arguments]  ${username}=${GAMER USERNAME}
  Wait Until Element Is Visible  //input[@name="userid"]
  Input Text  //input[@name="userid"]  ${username}

輸入：密碼
  [Arguments]  ${password}=${GAMER PASSWORD}
  Wait Until Element Is Visible  //div/input[@name="password"]
  Input Text  //div/input[@name="password"]  ${password}

點擊：登入按鈕
  Wait Until Element Is Visible  //div/a[@id="btn-login"]
  Wait Until Keyword Succeeds  5x  1s  確認：登入按鈕被點選

確認：登入按鈕被點選
  Click Element  //div/a[@id="btn-login"]
  Wait Until Element Is Visible  //a[@id="topBar_member"]

檢查：登入完成
  點選：勇者捷徑
  ${login name}=  Get Text  //div[@id="topBarMsg_member"]//a[@class="userid"]
  ${login name}=  Convert To Lowercase  ${login name}
  Should Be Equal As Strings  ${login name}  ${GAMER USERNAME}

點選：勇者捷徑
  Wait Until Element Is Visible  //div[@class="TOP-my"]//a[@id="topBar_member"]/i
  Click Element  //div[@class="TOP-my"]//a[@id="topBar_member"]/i
  Wait Until Element Is Visible  //div[@id="topBarMsg_member"]

點選：登出
  ${is visable}=  Run Keyword And Return Status  Wait Until Element Is Visible  //div[@id="topBarMsg_member"]

  IF  not ${is visable}
    點選：勇者捷徑
  END

  Wait Until Element Is Visible  //div[@id="topBarMsg_member"]//i[contains(@class,"sign-out")]  # //div[@id="topBarMsg_member"]/p//i
  Click Element  //div[@id="topBarMsg_member"]//i[contains(@class,"sign-out")]
  Wait Until Element Is Visible  //div[@class="form__buttonbar"]/button
  Click Element  //div[@class="form__buttonbar"]/button
  Wait Until Element Is Visible  //div[@class="TOP-my TOP-nologin"]//li/a[text()="我要登入"]

前往：每日簽到按鈕
  Scroll Element Into View  //div[@class="BA-left"]//a[@id="signin-btn"]

點選：簽到
  ${is signin}=  Run Keyword And Return Status  確認：是否已簽到

  IF  not ${is signin}
    進行：簽到
  END

確認：是否已簽到
  Wait Until Element Is Visible  //a[@id="signin-btn"]
  # 寫法1
  # ${signin text}=  Get Text  //a[@id="signin-btn"]
  # Should Contain  ${signin text}  每日簽到已達成
  # 寫法2
  # ${signin text}=  Get WebElement  //a[@id="signin-btn"]
  # Should Contain  ${signin text.text}  每日簽到已達成
  # 寫法3
  ${all text}=  Get Text  //a[@id="signin-btn"]
  ${sub text}=  Get Text  //a[@id="signin-btn"]/i
  ${signin text}=  Replace String  ${all text}  ${sub text}  ${EMPTY}
  Should Be Equal As Strings  ${signin text}  每日簽到已達成

進行：簽到
  Click Element  //div[@class="BA-left"]//a[@id="signin-btn"]/i
  Wait Until Element Is Visible  //dialog[contains(@id,"dialogify")]
  Wait Until Element Is Visible  //dialog[contains(@id,"dialogify")]/a/img
  Click Element  //dialog[contains(@id,"dialogify")]/a/img

輸入：關鍵字搜尋哈拉版
  [Arguments]  ${search text}
  Wait Until Element Is Visible  //td[@id="gs_tti50"]
  Input Text  //td[@id="gs_tti50"]/input  ${search text}
  Wait Until Element Is Visible  //td[contains(@class,"search-button")]
  Click Element  //td[contains(@class,"search-button")]
  Wait Until Element Is Visible  //div[@class="gsc-wrapper"]

點選：搜尋結果
  Wait Until Element Is Visible  //div[@class="gsc-wrapper"]
  ${elements}=  Get WebElements  //div[@class="gs-title"]/a[@class="gs-title"]

  FOR  ${element}  IN  @{elements}
    IF  "${element.text}" == "${SEARCH_BOARD_NAME}哈啦板- 巴哈姆特"
      Click Element  ${element}
    END
  END
  # ${element}=  Evaluate  [element.text for element in @{elements}]  # 似乎不能這樣用？

  Switch Window  NEW
  Wait Until Element Is Visible  //div[contains(@class,"FM-abox1")]

  # 方法2
  # 可以用css selector 實現
  # document.querySelectorAll("a.gs-title")

點選：進板圖
  Wait Until Element Is Visible  //div[contains(@class,"FM-abox1")]/a/img
  Click Element  //div[contains(@class,"FM-abox1")]/a/img
  # 切換討論區分類
  Wait Until Element Is Visible  //ul[@class="b-tags"]/li
  ${count}=  Get Element Count  //ul[@class="b-tags"]/li
  ${index}=  Evaluate  random.randint(1, ${count})
  Click Element  //ul[@class="b-tags"]/li[${index}]
  # 點選非置頂的討論文章
  Wait Until Element Is Visible  //tr[contains(@class, 'b-list-item')][not(contains(@class, 'is-del'))][not(contains(@class,'b-list__row--sticky'))]
  Click Element  //tr[contains(@class, 'b-list-item')][not(contains(@class, 'is-del'))][not(contains(@class,'b-list__row--sticky'))][1]//td[2]//p[@href]
