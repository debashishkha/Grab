*** Settings ***

Library     APIcalls.py
Library     database.py



*** Test Cases ***


01. To check the working of Create Order API
    log to console      \n Entering payload and calling the Create Order API
    ${order_id} =       APIcalls.check_create_order
    log to console      ${order_id}
    Sleep   60 seconds
    @{create_order_logs}=    read_create_order_logs     webber     Pass@123
    ${flag}     APIcalls.string_contains    ${create_order_logs}[0]    Success Order Details : [{"res":{"message":"success","errorCode":"0","bulk_order_id":1,"pos_order_id":["${order_id}
    Should be equal 	${flag}  ${true} 	The Create API is failed, please see the below logs \n${create_order_logs}[1]

02. To check the working of Update Order API
    log to console      \n Entering payload and calling the Update Order API
    ${order_id} =       APIcalls.check_update_order
    log to console      ${order_id}
    Sleep   60 seconds
    @{update_order_logs}=    read_update_order_logs     webber     Pass@123
    ${flag}     APIcalls.string_contains    ${update_order_logs}[0]    {"success":"true","errorCode":"0","errorDescription":"","order_id":"${order_id}
    Should be equal 	${flag}  ${true} 	The Update API is failed, please see the below logs \n${update_order_logs}[1]

03. To check the working of Login API
    log to console      \n Entering payload and calling the login API
    @{response_login} =  APIcalls.check_login
    Should Be Equal     ${response_login}[0]     success     Login API Failed, request response is ${response_login}[1]

04. To check the working of Checkin API
    log to console      \n Entering payload and calling the checkin API
    @{response_checkin} =  APIcalls.check_checkin
    Should Be Equal     ${response_checkin}[0]     success     Checkin API Failed, request response is ${response_checkin}[1]

# 05. get order

07. To check working of Order Allocated API
    log to console      \n Entering payload and calling the Order Allocated API
    @{response_order_allocated} =   APIcalls.check_order_allocated_api
    Should Be Equal     ${response_order_allocated}[0]     success     Order Allocated API Failed, request response is ${response_order_allocated}[1]

08. To check the order status in DB after allocating the order
    ${order_status_in_DB} =         APIcalls.check_order_status_in_DB
    log to console      \n checking the order status after allocating the order
    Should Be Equal     ${order_status_in_DB}     3     The order_status in the DB after allocating the order is not 3 but ${order_status_in_DB}

09. To check working of Order Reached API
    log to console      \n Entering payload and calling the Order Reached API
    @{response_order_reached} =   APIcalls.check_order_reached_api
    Should Be Equal     ${response_order_reached}[0]     success     Order Allocated API Failed, request response is ${response_order_reached}[1]

10. To check the order status in DB after the order Reaches (Order Reach API)
    log to console      \n checking the order status after the order Reaches (Order Reach API)
    ${order_status_in_DB} =         APIcalls.check_order_status_in_DB
    Should Be Equal     ${order_status_in_DB}     4     The order_status in the DB after the order reaches is not 4 but ${order_status_in_DB}
