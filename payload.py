import string
import time
import random
import json


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
          "cust_address_line1": "102 Parvati Premises Sunmill Compound Lower Parel Mumbai",
          "cust_address_line2": "lower Parel West, Mumbai, Maharashtra, 400013",
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

order_to_deliver_payload = '[{"callName":"processorder"},{"inputData":{"uName":"G156775","orderId":"{order_id}",' \
                    '"billNo":"AutomateDeliveryG5QLF","amount":"460","restaurantId":"7890",' \
                    '"uLat":"19.424388333333333","uLong":"72.82647166666668","status":"5","accept":' \
                    '"1587533552633","reached":"1587533584000","todeliver":"1587533584000","datetime":' \
                    '"1660893668764","appversion":"7.0.0.18","comment":"","packageId":"0",' \
                    '"deviceImei":"869184048593711","pickOtp":"","appSource":"2","isLastOrder":"0",' \
                    '"sid":"535ffc573b7077893363680c8860afb6374","customerInfo":' \
                    '{"add1":"Summit Bussiness Bay","add2":"Andheri","landmark":"PVR cinemas",' \
                    '"dareaId":"1233","dareaName":"Scindia Society Andheri East","name":"Nikita",' \
                    '"phone":"9029668326,32148071","clientId":"2460"}}}]'

order_to_deliver_header = {"X-Public": "a9b6886626ca9b4f5dc2391378e5a19dd0615e05369e9cba670ad20f1958086d",
                           "X-Hash": "f296245ca97594d9245c76d0e7656b6916e26584b14cb833643ed12a2150a8ce",
                           "Content-Type": "application/json"}

order_full_delivery_prepaid_payload = '[{"callName":"processorder"},{"inputData":{"uName":"G156775","appversion":' \
                             '"7.0.0.18","datetime":"1587534066000","deviceImei":"869184048593711","status":' \
                             '"6","orderId":"{order_id}","billNo":"jio-12","amount":"460","uLat":"19.4245536",' \
                             '"uLong":"72.8262403","accept":"1587533995000","reached":"1587534001000",' \
                             '"todeliver":"1587534001000","delivered":"1587534066000","toReturn":"",' \
                             '"returnedToDC":"","partialDeliver":"","packageId":"0","opDetails":' \
                             '"Washing Powder Nirma - 5 kg Pouch,Paras Royal Rice- 25 kg,Paras Royal Rice- 25 ' \
                             'kg","ohc":"","simdata":"","geofence_delivered":"0","receivingcustomerName":"",' \
                             '"receivingcustomerPhone":"","ideaMobileNo":"","orderItemDetails":' \
                             '"[{\"category\":\"Detergent Powder\",\"item_id\":\"100\",\"grab_item_id\":\"\",' \
                             '\"is_food\":\"0\",\"item_name\":\"Washing Powder Nirma - 5 kg Pouch\",\
                             "unit_price\":\"20.00\",\"quantity\":\"3\",\"isChecked\":\"1\",\"reasonId\":\"\"' \
                             ',\"reasonDesc\":\"\",\"deliverCount\":\"3\",\"rejectCount\":\"0\"},' \
                             '{\"category\":\"Rice\",\"item_id\":\"101\",\"grab_item_id\":\"\",\"is_food\":' \
                             '\"0\",\"item_name\":\"Paras Royal Rice- 25 kg\",\"unit_price\":\"50.00\",' \
                             '\"quantity\":\"4\",\"isChecked\":\"1\",\"reasonId\":\"\",\"reasonDesc\":\"\",' \
                             '\"deliverCount\":\"4\",\"rejectCount\":\"0\"},{\"category\":\"Rice\",\"item_id\
                             ":\"103\",\"grab_item_id\":\"\",\"is_food\":\"0\",\"item_name\":\
                             "Paras Royal Rice- 25 kg\",\"unit_price\":\"50.00\",\"quantity\":\"4\",' \
                             '\"isChecked\":\"1\",\"reasonId\":\"\",\"reasonDesc\":\"\",\"deliverCount\":' \
                             '\"4\",\"rejectCount\":\"0\"}]","relationShip":"","idProofType":"","idProofNo":' \
                             '"","modeType":"","modeId1":"","modeId2":"","mode1Amt":"","mode2Amt":"",' \
                             '"expiryDate":"","deliveryAt":"","empId":"","fmComment":"","reason":"0",' \
                             '"sorryCardNo":"","shipmentPickedCount":"","appSource":"2","isLastOrder":"0",' \
                             '"deliverOtpNotLandingReasonId":"0","isProcessingLastForwardOrderOfAWaypoint":' \
                             '"0","sid":"535ffc573b7077893363680c8860afb6374","clientId":"2460"}}]'

order_full_delivery_prepaid_header = {"X-Public": "a9b6886626ca9b4f5dc2391378e5a19dd0615e05369e9cba670ad20f1958086d",
                               "X-Hash": "ef438b10f1b70211b580c7bbcffc031efc998452d43a57a1262ca619b016e3eb",
                               "Content-Type": "application/json"}

shipsy_create_order_payload = """{
    "TripId": "{order_id}",
    "TripDetails": [
        {
            "SequenceNo": 0,
            "Activity": "O",
            "Loc": "13456",
            "LocationName": "QWIK Supply Chain Private Ltd,Warehouse At Gd Logi Ring Rd No3 Nr Rail",
            "contactNo": null,
            "Name1": null,
            "Address1": "QWIK Supply Chain Private Ltd,Warehouse At Gd Logi Ring Rd No3 Nr Rail",
            "Address2": "Bridge Vlg Giroud Industrial Area Sil,",
            "Address3": null,
            "Pincode": "492001",
            "Phone": "9029668326",
            "Latitude": 21.2917,
            "Longitude": 81.7036
        },
        {
            "SequenceNo": 1,
            "Activity": "P",
            "Loc": "RPR001",
            "LocationName": "Unnamed Road, Musra Khurd, Chh",
            "contactNo": "7738847497",
            "Name1": "Faishon house",
            "Address1": "Unnamed Road, Musra Khurd, Chh",
            "Address2": "null,India",
            "Address3": null,
            "Pincode": "491445",
            "Phone": "9029668326",
            "Latitude": 0,
            "Longitude": 0,
            "DirectDispatch":1,
            "StageData": [
                {
                    "SequenceNo": 1,
                    "ConsignmentNo": "CN001",
                    "NumberOfHU": [
                        "ITEM00",
                        "ITEM01"
                    ],
                    "EwaybillFlag": null,
                    "Netvalue": "2000",
                    "amountToCollect": "1000",
                    "BUTag": "NETMEDS",
                    "EwaybillExpirationDate": "2021-05-24",
                    "OriginStateCode": "HR",
                    "DestinationStateCode": "CT",
                    "ConsignorCode": "R812",
                    "ConsigneeCode": "9424115815",
                    "MovementType": "CON",
                    "LegType": "JTC",
                    "CNDIRECTION": "R"
                }
            ]
        },
        {
            "SequenceNo": 2,
            "Activity": "D",
            "Loc": "RPR001",
            "LocationName": "Unnamed Road, Musra Khurd, Chh",
            "contactNo": "7738847497",
            "Name1": "Faishon house",
            "Address1": "Unnamed Road, Musra Khurd, Chh",
            "Address2": "null,India",
            "Address3": null,
            "Pincode": "491445",
            "Phone": "9029668326",
            "Latitude": 0,
            "Longitude": 0,
            "DirectDispatch":0,
            "StageData": [
                {
                    "SequenceNo": 2,
                    "ConsignmentNo": "CN002",
                    "NumberOfHU": [
                        "ITEM02",
                        "ITEM03"
                    ],
                    "EwaybillFlag": null,
                    "Netvalue": "2000",
                    "amountToCollect": "1000",
                    "BUTag": "NETMEDS",
                    "EwaybillExpirationDate": "2021-05-24",
                    "OriginStateCode": "HR",
                    "DestinationStateCode": "CT",
                    "ConsignorCode": "R812",
                    "ConsigneeCode": "9424115815",
                    "MovementType": "CON",
                    "LegType": "JTC",
                    "CNDIRECTION": "R"
                }
            ]
        }
        
      
    ],
    "VehicleNumber": "CG13AB88066",
    "public_hash": "076033ae5d25193a15bcfeb7cc2b7351a18ebdf49f6bf478c6343b3338430211",
    "content_hash": "asdasdasdasd",
    "req_id": "testkafkaup0025_C"
}"""

shipsy_create_order_body = shipsy_create_order_payload.replace("{order_id}", trip_id)

shipsy_create_order_header = {"X-Public": "076033ae5d25193a15bcfeb7cc2b7351a18ebdf49f6bf478c6343b3338430211",
                              "X-Hash": "ef8bd3b64421b59322a55f3d861dd72b3c8552c3166da3ef63f5e8b68a2aa64a",
                              "Content-Type": "application/json"}

shipsy_update_order_payload = """{
    "TripId": "{order_id}",
    "TripDetails": [
        {
            "SequenceNo": 0,
            "Activity": "O",
            "Loc": "13456",
            "LocationName": "QWIK Supply Chain Private Ltd,Warehouse At Gd Logi Ring Rd No3 Nr Rail",
            "contactNo": null,
            "Name1": null,
            "Address1": "QWIK Supply Chain Private Ltd,Warehouse At Gd Logi Ring Rd No3 Nr Rail",
            "Address2": "Bridge Vlg Giroud Industrial Area Sil,",
            "Address3": null,
            "Pincode": "492001",
            "Phone": "9029668326",
            "Latitude": 21.2917,
            "Longitude": 81.7036
        },
        {
            "SequenceNo": 1,
            "Activity": "P",
            "Loc": "RPR001",
            "LocationName": "Unnamed Road, Musra Khurd, Chh",
            "contactNo": "7738847497",
            "Name1": "Faishon house",
            "Address1": "Unnamed Road, Musra Khurd, Chh",
            "Address2": "null,India",
            "Address3": null,
            "Pincode": "491445",
            "Phone": "9029668326",
            "Latitude": 0,
            "Longitude": 0,
            "DirectDispatch":1,
            "StageData": [
                {
                    "SequenceNo": 1,
                    "ConsignmentNo": "CN001",
                    "NumberOfHU": [
                        "ITEM00",
                        "ITEM01"
                    ],
                    "EwaybillFlag": null,
                    "Netvalue": "2000",
                    "amountToCollect": "1000",
                    "BUTag": "NETMEDS",
                    "EwaybillExpirationDate": "2021-05-24",
                    "OriginStateCode": "HR",
                    "DestinationStateCode": "CT",
                    "ConsignorCode": "R812",
                    "ConsigneeCode": "9424115815",
                    "MovementType": "CON",
                    "LegType": "JTC",
                    "CNDIRECTION": "R"
                }
            ]
        },
        {
            "SequenceNo": 2,
            "Activity": "D",
            "Loc": "RPR001",
            "LocationName": "Unnamed Road, Musra Khurd, Chh",
            "contactNo": "7738847497",
            "Name1": "Faishon house",
            "Address1": "Unnamed Road, Musra Khurd, Chh",
            "Address2": "null,India",
            "Address3": null,
            "Pincode": "491445",
            "Phone": "9029668326",
            "Latitude": 0,
            "Longitude": 0,
            "DirectDispatch":0,
            "StageData": [
                {
                    "SequenceNo": 2,
                    "ConsignmentNo": "CN002",
                    "NumberOfHU": [
                        "ITEM02",
                        "ITEM03"
                    ],
                    "EwaybillFlag": null,
                    "Netvalue": "2000",
                    "amountToCollect": "1000",
                    "BUTag": "NETMEDS",
                    "EwaybillExpirationDate": "2021-05-24",
                    "OriginStateCode": "HR",
                    "DestinationStateCode": "CT",
                    "ConsignorCode": "R812",
                    "ConsigneeCode": "9424115815",
                    "MovementType": "CON",
                    "LegType": "JTC",
                    "CNDIRECTION": "R"
                }
            ]
        },
      {
            "Activity": "D",
            "Address1": "Unnamed Road, Musra Khurd, Chh",
            "Address2": "null,India",
            "Address3": null,
            "contactNo": "7738847497",
            "DirectDispatch": 0,
            "Latitude": 0,
            "Loc": "RPR001",
            "LocationName": "Unnamed Road, Musra Khurd, Chh",
            "Longitude": 0,
            "Name1": "Faishon house",
            "Phone": "9029668326",
            "Pincode": "491445",
            "SequenceNo": 3,
            "StageData": [
                {
                    "amountToCollect": "1000",
                    "BUTag": "NETMEDS",
                    "CNDIRECTION": "R",
                    "ConsigneeCode": "9424115815",
                    "ConsignmentNo": "CN003",
                    "ConsignorCode": "R812",
                    "DestinationStateCode": "CT",
                    "EwaybillExpirationDate": "2021-05-24",
                    "EwaybillFlag": null,
                    "LegType": "JTC",
                    "MovementType": "CON",
                    "Netvalue": "2000",
                    "NumberOfHU": [
                        "ITEM04",
                        "ITEM05"
                    ],
                    "OriginStateCode": "HR",
                    "SequenceNo": 3
                }
            ]
        }
      
    ],
    "VehicleNumber": "CG13AB88066",
    "public_hash": "076033ae5d25193a15bcfeb7cc2b7351a18ebdf49f6bf478c6343b3338430211",
    "content_hash": "asdasdasdasd",
    "req_id": "testkafkaup0025_C"
}"""

shipsy_update_order_body = shipsy_update_order_payload.replace("{order_id}", trip_id)

shipsy_update_order_header = {"X-Public": "076033ae5d25193a15bcfeb7cc2b7351a18ebdf49f6bf478c6343b3338430211",
                              "X-Hash": "ef8bd3b64421b59322a55f3d861dd72b3c8552c3166da3ef63f5e8b68a2aa64a",
                              "Content-Type": "application/json"}

get_order_payload = '[{"callName":"pullOrders"},{"inputData":{"uName":"G157227","orderCategory":"1",' \
                    '"merchant_id":"49050","bill_no":"AutomateDeliveryLICMV","appversion":"7.0.0.18",' \
                    '"datetime":"1660904492074","runsheet":"0","areaid":"0","deviceImei":"27e72087721c16f3",' \
                    '"manualPull":"1","uLat":"19.1605471","uLong":"73.2428719","appSource":"2",' \
                    '"isBillWiseSearch":"0","isFilterTypeId":"3","sid":"c7fb6fc13126abf9c7d1d2c112cd2dac2af",' \
                    '"clientId":"2460","bundleId":"com.grab.grabrider"}}]'

get_order_header = {"X-Public": "a9b6886626ca9b4f5dc2391378e5a19dd0615e05369e9cba670ad20f1958086d",
                    "X-Hash": "f39209496712d4764bcaba581444f17dc9e48bfbb3058ab02d15d01a64412a52",
                    "Content-Type": "application/json"}
