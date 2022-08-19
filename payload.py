import string
import time
import random


random_word = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

trip_id = 'AutomateDelivery' + str(random_word)

milliseconds = int(round(time.time() * 1000))

create_headers = {'Content-Type': 'application/xml'}

create_payload = """<QueueMessage>  
    <MessageText><![CDATA[
    {
      "clientId": "2460",
      "order_details": [
        {
          "order_id": "{order_id}",
          "invoice_id": "{order_id}",
          "order_value": "146.0",
          "amount_to_collect": "0",
          "payment_type": "Prepaid",
          "sodexo_prepaid_amount": "100",
          "merchant_id": "7890",
          "order_mode": null,
          "cust_name": "Debashish Kha",
          "cust_address_line1": "The Summit Business Bay (Omkar)Andheri - Kurla Rd, Adjacent to Cinemax, Chakala,",
          "cust_address_line2": "Andheri East, Mumbai, Maharashtra 400069",
          "cust_landmark": "",
          "cust_contact": "9029668326",
          "cust_lat": "0",
          "cust_long": "0",
          "pincode": "400069",
          "order_category": "Batch"
        }
      ],
      "dttm": "2021-03-13 12:00:41 AM"
    }
    ]]></MessageText>
    </QueueMessage>"""

create_body = create_payload.replace("{order_id}", trip_id)

update_payload = """<QueueMessage>  
    <MessageText><![CDATA[
    {
      "clientId": "2460",
      "order_id": "{order_id}",
      "merchant_id": "7890",
      "items": [
        {
          "category": "FruitsVegetables",
          "item_id": "8902901001754",
          "is_food": "",
          "item_name": "SOOJI RAWA 500 g PP",
          "unit_price": 100,
          "quantity": 1,
          "item_weight": "0",
          "itemWiseTotal": 0
        },
        {
          "category": "FruitsVegetables",
          "item_id": "8906006783331",
          "is_food": "",
          "item_name": "SR TKETCLSIC 1 kg PC",
          "unit_price": 200,
          "quantity": 1,
          "item_weight": "0",
          "itemWiseTotal": 0
        },
        {
          "category": "FruitsVegetables",
          "item_id": "8901595862740",
          "is_food": "",
          "item_name": "CHG RCHISU 200 g BTL",
          "unit_price": 50,
          "quantity": 2,
          "item_weight": "0",
          "itemWiseTotal": 0
        },
        {
          "category": "Test",
          "item_id": "8901595862733",
          "is_food": "",
          "item_name": "CHG GNCHSU 190 g BTL",
          "unit_price": 200,
          "quantity": 2,
          "item_weight": "0",
          "itemWiseTotal": 0
        }
      ],
      "amount_to_collect": "700.00",
      "order_value": "1000.00",
      "payment_type": "COD",
      "sodexo_prepaid_amount": "300.00"
    }
      ]]></MessageText>
    </QueueMessage>"""

update_headers = {'content-type': 'application/xml',
                      'x-public': '9243c401b52141fdae266bdbd5be63cca6e8398be85716128b15dc338a7913a2',
                      'cookie': 'PHPSESSID=a9giqcb9ev726qvjl6lc07d864; PHPSESSID=a9giqcb9ev726qvjl6lc07d864'}

update_body = update_payload.replace("{order_id}", trip_id)

login_payload = '[{"callName":"loginservice"},{"inputData":{"deviceToken":"fuApXIw7RGuw_3FdXTKIgs:APA91bFgKFNq_' \
                'V5CtLm8rN5dLGHAhZwliW9HJiW-Va58-NcuVg6f-kum6dF3n8VInGFlGxV0-0c2bBr8RtJIR9ff_A7Ik5dBp0La5250' \
                'C8AvtoCG6dtvs2HTI7FloV8_2vzgxpALXaYn","deviceImei":"37191a634a5186e3",' \
                '"uName":"G156775","uPassword":"Test@123","uLat":"19.1551442","uLong":"72.8326861",' \
                '"appversion":"7.0.0.18","uIPAddress":"192.168.0.102","manufacturer":"motorola",' \
                '"model":"moto g(9)","appSource":"2","software_version":"11"}}]'

login_header = {"X-Public": "a9b6886626ca9b4f5dc2391378e5a19dd0615e05369e9cba670ad20f1958086d",
                "Content-Type": "application/json",
                "X-Hash": "b4b1705c6611af7d6af04292731dff45291edc17c4823cb46debd115d349b9ad"}

checkin_payload = '[{"callName":"checkin"},{"inputData":{"uName":"G156775","uLat":"19.2985868",' \
                  '"uLong":"72.8499434","datetime":' + str(milliseconds) + ',' \
                  '"appversion":"7.0.0.18","miscData":"1628225953000,27,0,0,1628227513000,0,0",' \
                  '"dutyTimeVal":"0","inactiveDuration":"0.0","deviceImei":"37191a634a5186e3",' \
                  '"appSource":"2","sid":"089ab853a7b36e74af69111dafbbd00855a"}}]'

checkin_header = {"X-Public": "a9b6886626ca9b4f5dc2391378e5a19dd0615e05369e9cba670ad20f1958086d",
                  "Content-Type": "application/json",
                  "X-Hash": "b4b1705c6611af7d6af04292731dff45291edc17c4823cb46debd115d349b9ad"}

order_allocated_header = {"X-Public": "a9b6886626ca9b4f5dc2391378e5a19dd0615e05369e9cba670ad20f1958086d",
                          "X-Hash": "e4794400b3fb4eee74e266a04bf27fa35a3a7eba77f63fd5366e651ee58c9cd3",
                          "Content-Type": "application/json"}

order_allocated_payload = '[{"callName":"processorder"},{"inputData":{"uName":"G156775","status":"3",' \
                          '"orderId":"{order_id}","uLat":"19.1034834","uLong":"72.8602084",' \
                          '"accept":"1596703392443","datetime":"1596703392476","orderIntimationType":"3",' \
                          '"appversion":"7.0.0.18","deviceImei":"358995091982297","appSource":"2",' \
                          '"orderBroadcastType":"0","sid":"089ab853a7b36e74af69111dafbbd00855a",' \
                          '"clientId":"2460"}}]'

order_reached_header = {"X-Public": "a9b6886626ca9b4f5dc2391378e5a19dd0615e05369e9cba670ad20f1958086d",
                        "X-Hash": "67afc80b0fde36559dc36e38054c342df4bf6864c6ddf66202aa3f7e3123cc8d",
                        "Content-Type": "application/json"}

order_reached_payload = '[{"callName":"processorder"},{"inputData":{"uName":"G156775","orderId":"{order_id}",' \
                        '"status":"4","uLat":"19.424353333333332","uLong":"72.82656999999999",' \
                        '"accept":"1587533552633","reached":"1587533584000","datetime":"1587533598000",' \
                        '"passedQRCriteria":"","appversion":"7.0.0.18","appSource":"2","deviceImei":' \
                        '"869184048593711","sid":"535ffc573b7077893363680c8860afb6374","clientId":"2460"}}]'




