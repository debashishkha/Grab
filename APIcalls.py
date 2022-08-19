import requests
import payload
import datetime as datetime
import database



def check_create_order():
    create_order_api = 'https://jiograbsitqueue.queue.core.windows.net/createordersit/messages?sv=2018-03-28&si=createord' \
                     'ersit-a&sig=nCKI4o4FFhzSx5Qa4n2ZqZaVvY9ny9lEEx%2BBIZ9LNVM%3D'
    requests.post(create_order_api, data=payload.create_body, headers=payload.create_headers)
    return payload.trip_id

def check_update_order():
    update_order_api = 'https://jiograbsitqueue.queue.core.windows.net/updateordersit/messages?sv=2018-03-28&si' \
                 '=updateordersit-a&sig=LAG2HxuitPcZbuhMKv/U6CRpUq8Y0LHHyHa%2BzvqL364%3D'
    requests.post(update_order_api, data=payload.update_body, headers=payload.update_headers)
    return payload.trip_id

def read_create_order_logs(username, password):
    url = 'https://sit.grab.in/web_service_log/' + str(datetime.date.today()) + '_' + datetime.datetime.now().strftime(
        "%H") + '_CreateOrderQueueDetails.txt'
    r = requests.get(url, auth=(username, password))
    page = r.content
    return [page, url]


def read_update_order_logs(username, password):
    url = 'https://sit.grab.in/web_service_log/' + str(datetime.date.today()) + '_' + datetime.datetime.now().strftime(
        "%H") + '_updateOrderItemQueue.txt'
    r = requests.get(url, auth=(username, password))
    page = r.content
    return [page, url]

def string_contains(first, second):
    flag = False

    if str(second) in str(first):
        flag = True

    return bool(flag)

def check_login():
    login_api = "https://sit.grab.in/grabriderapp"
    print("Entering payload and calling the login API")
    response_login = requests.post(login_api, data=payload.login_payload, headers=payload.login_header).json()
    return [response_login["response"], response_login]

def check_checkin():
    checkin_api = "https://sit.grab.in/grabriderapp"
    print("Entering payload and calling the checkin API")
    response_checkin = requests.post(checkin_api, data=payload.checkin_payload, headers=payload.checkin_header).json()
    return [response_checkin["response"], response_checkin]

def check_order_allocated_api():
    order_allocated_api = "https://sit.grab.in/grabriderapp"
    print("Entering payload and calling the Order Allocated API")
    oid = database.B2C_execute_query("SELECT OID FROM tbl_order_main WHERE pos_order_id like '%" + payload.trip_id + "%'")
    # print(oid[0][0])
    order_allocated_body = payload.order_allocated_payload.replace("{order_id}", str(oid[0][0]))
    response_order_allocated = requests.post(order_allocated_api, data=order_allocated_body,
                                             headers=payload.order_allocated_header).json()
    return [response_order_allocated["response"], response_order_allocated]

def check_order_status_in_DB():
    response = database.B2C_execute_query("SELECT order_status FROM tbl_order_main WHERE pos_order_id like '%" + payload.trip_id + "%'")
    return str(response[0][0])

def check_order_reached_api():
    order_reached_api = "https://sit.grab.in/grabriderapp"
    print("Entering payload and calling the Order Reached API")
    oid = database.B2C_execute_query("SELECT OID FROM tbl_order_main WHERE pos_order_id like '%" + payload.trip_id + "%'")
    # print(oid[0][0])
    order_reached_body = payload.order_reached_payload.replace("{order_id}", str(oid[0][0]))
    response_order_reached = requests.post(order_reached_api, data=order_reached_body,
                                             headers=payload.order_reached_header).json()
    return [response_order_reached["response"], response_order_reached]
