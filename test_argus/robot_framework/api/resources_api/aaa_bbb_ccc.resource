# *** Settings ***
# Documentation  CreateEntryBlock
# Resource  ./external.resource
# Resource  ../resources/common.resource


# *** Keywords ***
# GET：取得使用者狀態
#   [Arguments]  ${params}=${EMPTY}
#   IF  "${params}" == "${EMPTY}"
#     ${params}=  Create Dictionary
#   END

#   Set To Dictionary  ${params}  api_uri=/api/trade/v2/c/create/entry/block/user/check
#   客端導向第三方API  GET  ${params}

# 執行：取得使用者狀態
#   [Arguments]  ${params}=${EMPTY}
#   GET：取得使用者狀態  ${params}
#   Schema檢查  ${response}  test/api/client/schema/get_trade_v2_c_create_entry_block_user_check.json
