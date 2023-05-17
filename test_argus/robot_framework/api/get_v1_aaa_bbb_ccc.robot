# *** Settings ***
# Documentation  API > CreateEntryBlock > 取得使用者狀態 > /api/trade/v2/c/create/entry/block/user/check
# Default Tags  API  Public
# Resource  ../../resources/login.resource
# Resource  ../../resources_api/create_entry_block.resource
# Test Setup  前置：取得相對應參數
# Test Teardown  Delete All Sessions


# *** Test Cases ***
# 正常取得使用者存款封鎖狀態
#   [Tags]  Success  GET
#   執行：取得使用者狀態

# 正常取得使用者存款封鎖狀態-全部參數
#   [Tags]  Success  GET
#   設定：帶入全部參數
#   執行：取得使用者狀態  ${params}

# 未登入成功請求
#   設定：建立未登入Session  client  ${CLIENT HOST}
#   Set To Dictionary  ${params}  username=${PLAYER USERNAME}
#   執行：取得使用者狀態  ${params}

# 未登入失敗請求
#   設定：建立未登入Session  client  ${CLIENT HOST}
#   GET：取得使用者狀態  ${params}
#   檢查：未登入錯誤回傳  400  TM020058

# 使用者帳號參數檢查(已登入)
#   [Template]  帶入：使用者帳號參數(已登入)
#   ${NULL}
#   ${EMPTY}
#   ${SPACE*3}
#   abcd
#   ${1234}
#   9999999999999999999
#   ${0}
#   ${12.34}
#   9999999999999999999.99999
#   ${-1}
#   false
#   ,

# 使用者帳號參數檢查(未登入)
#   [Documentation]  ${error code}=${1500190094}  ${status code}=400
#   [Template]  帶入：使用者帳號參數(未登入)
#   ${NULL}  TM020058
#   ${EMPTY}  TM020058
#   ${SPACE*3}
#   abcd
#   ${1234}
#   9999999999999999999
#   ${0}  ${1500010009}
#   ${12.34}
#   9999999999999999999.99999
#   ${-1}
#   false
#   ,


# *** Keywords ***
# 前置：取得使用者存款封鎖狀態相對應參數
#   會員登入
#   ${params}=  Create Dictionary
#   Set Suite Variable  ${params}

# 設定：帶入全部參數
#   Set To Dictionary  ${params}  username=argus

# 帶入：使用者帳號參數(已登入)
#   [Arguments]  ${value}  ${error code}=ok  ${status code}=200
#   Set To Dictionary  ${params}  username=${value}
#   檢查：執行API結果  ${error code}  ${status code}

# 帶入：使用者帳號參數(未登入)
#   [Arguments]  ${value}  ${error code}=${1500190094}  ${status code}=400
#   設定：建立未登入Session  client  ${CLIENT HOST}
#   Set To Dictionary  ${params}  username=${value}
#   檢查：執行API結果  ${error code}  ${status code}

# 檢查：執行API結果
#   [Arguments]  ${error code}  ${status code}
#   IF  "${error code}" == "ok"
#     執行：取得使用者狀態  ${params}
#   ELSE
#     GET：取得使用者狀態  ${params}

#     ${expected messages}=  Create Dictionary
#     ...  1500010009=请输入帐号
#     ...  1500190094=使用者不存在
#     ...  TM020058=请重新登入

#     ${expected response}=  Create Dictionary
#     ...  result=error
#     ...  msg=${expected messages['${error code}']}
#     ...  code=${error code}

#     Dictionaries Should Be Equal  ${expected response}  ${response.json()}
#     Status Should Be  ${status code}  ${response}
#   END
