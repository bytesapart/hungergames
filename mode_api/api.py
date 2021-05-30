import requests
import json
import hashlib
import datetime
from secret import encrypt

# For states - https://cdn-api.co-vin.in/api/v2/admin/location/states
# For distrcits - https://cdn-api.co-vin.in/api/v2/admin/location/districts/21

_password = "CoWIN@$#&*(!@%^&".encode()
_username = "b5cab167-7977-4df1-8027-a63aa144f04e".encode()

_secret = encrypt(_username, _password).decode()
_api_mode = 'protected'
http_proxy = ''
https_proxy = ''


def _today():
    return "{}-{}-{}".format(datetime.date.today().day, datetime.date.today().month, datetime.date.today().year)


def _tomorrow():
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    return "{}-{}-{}".format(tomorrow.day, tomorrow.month, tomorrow.year)


def days_past(number_of_days):
    tomorrow = datetime.date.today() - datetime.timedelta(days=number_of_days)
    return "{}-{}-{}".format(tomorrow.day, tomorrow.month, tomorrow.year)


def days_future(number_of_days):
    tomorrow = datetime.date.today() + datetime.timedelta(days=number_of_days)
    return "{}-{}-{}".format(tomorrow.day, tomorrow.month, tomorrow.year)


is_saturday = True if datetime.datetime.today().weekday() == 5 else False
if is_saturday:
    function_to_call = days_future(2)
else:
    function_to_call = _tomorrow()


def _get_response(method, header_append={}, **kwargs):
    with open("apis.json", "r") as f:
        api_json = json.load(f)[_api_mode]
        request = {**api_json[method], "header": {**api_json["genericHeaders"], **header_append},
                   'proxies': {'http': https_proxy, "https": https_proxy}}

    for key, value in kwargs.items():
        try:
            if type(request[key]) == str:
                request[key] = request[key].format(**value)
        except Exception as e:
            print(e)

    if request["type"] == "POST":
        request["json"] = kwargs["json"]

    if request["type"] == "POST":
        return requests.post(url=request['url'], json=request['json'], headers=request['header'],
                             proxies=request['proxies'])
    elif request["type"] == "GET":
        return requests.get(url=request['url'], headers=request['header'], proxies=request['proxies'])


def generate_otp(mobile):
    response = _get_response("generateMobileOTP", json={
        "mobile": mobile,
        "secret": _secret
    })
    if response.status_code == 401:
        raise ConnectionError("Session Expired, logging in again!")
    if response.status_code == 429:
        raise ConnectionError(
            f'Response Exception occurred in generate_otp! The response code was {response.status_code}.'
            f' The content is {response.content}')
    if response.status_code != 200:
        raise Exception(f'Response Exception occurred in generate_otp! The response code was {response.status_code}.'
                        f' The content is {response.content}')
    return response


def validate_otp(otp, trxn_resp):
    otp_hash = hashlib.sha256(otp.encode()).hexdigest()
    print(otp, otp_hash)

    response = _get_response("validateMobileOTP", json={
        "otp": otp_hash,
        "txnId": trxn_resp.json()['txnId']
    })
    if response.status_code == 401:
        raise ConnectionError("Session Expired, logging in again!")
    if response.status_code == 429:
        raise ConnectionError(
            f'Response Exception occurred in validate_otp! The response code was {response.status_code}.'
            f' The content is {response.content}')
    if response.status_code != 200:
        raise Exception(f'Response Exception occurred in validate_otp! The response code was {response.status_code}.'
                        f' The content is {response.content}')
    bearer_token = response.json()['token']
    return bearer_token


def calendar_by_district(district_id, bearer_token):
    response = _get_response("calendarByDistrict", header_append={
        "authorization": "Bearer {}".format(bearer_token)
    }, url={
        "district_id": district_id,
        "date": function_to_call
    })
    if response.status_code == 401:
        raise ConnectionError("Session Expired, logging in again!")
    if response.status_code == 429:
        raise ConnectionError(
            f'Response Exception occurred in calendar_by_district! The response code was {response.status_code}.'
            f' The content is {response.content}')
    if response.status_code != 200:
        raise Exception(
            f'Response Exception occurred in calendar_by_district! The response code was {response.status_code}.'
            f' The content is {response.content}')
    return response


def find_by_district(district_id, bearer_token):
    response = _get_response("findByDistrict", header_append={
        "authorization": "Bearer {}".format(bearer_token)
    }, url={
        "district_id": district_id,
        "date": function_to_call
    })
    if response.status_code == 401:
        raise ConnectionError("Session Expired, logging in again!")
    if response.status_code == 429:
        raise ConnectionError(
            f'Response Exception occurred in find_by_district! The response code was {response.status_code}.'
            f' The content is {response.content}')
    if response.status_code != 200:
        raise Exception(
            f'Response Exception occurred in find_by_district! The response code was {response.status_code}.'
            f' The content is {response.content}')
    return response


def calendar_by_pin(pin, bearer_token):
    response = _get_response("calendarByPIN", header_append={
        "authorization": "Bearer {}".format(bearer_token)
    }, url={
        "pincode": pin,
        "date": function_to_call
    })
    if response.status_code == 401:
        raise ConnectionError("Session Expired, logging in again!")
    if response.status_code == 429:
        raise ConnectionError(
            f'Response Exception occurred in calendar_by_pin! The response code was {response.status_code}.'
            f' The content is {response.content}')
    if response.status_code != 200:
        raise Exception(
            f'Response Exception occurred in calendar_by_pin! The response code was {response.status_code}.'
            f' The content is {response.content}')
    return response


def find_by_pin(pin, bearer_token):
    response = _get_response("findByPIN", header_append={
        "authorization": "Bearer {}".format(bearer_token)
    }, url={
        "pincode": pin,
        "date": function_to_call
    })
    if response.status_code == 401:
        raise ConnectionError("Session Expired, logging in again!")
    if response.status_code == 429:
        raise ConnectionError(
            f'Response Exception occurred in find_by_pin! The response code was {response.status_code}.'
            f' The content is {response.content}')
    if response.status_code != 200:
        raise Exception(
            f'Response Exception occurred in find_by_pin! The response code was {response.status_code}.'
            f' The content is {response.content}')
    return response


def get_all_beneficiaries(bearer_token):
    response = _get_response("beneficiaries", header_append={
        "authorization": "Bearer {}".format(bearer_token)
    })
    if response.status_code == 401:
        raise ConnectionError("Session Expired, logging in again!")
    if response.status_code == 429:
        raise ConnectionError(
            f'Response Exception occurred in get_all_beneficiaries! The response code was {response.status_code}.'
            f' The content is {response.content}')
    if response.status_code != 200:
        raise Exception(
            f'Response Exception occurred in get_all_beneficiaries! The response code was {response.status_code}.'
            f' The content is {response.content}')
    return response


def get_state_id(state):
    response = _get_response('getAllStates')
    if response.status_code == 401:
        raise ConnectionError("Session Expired, logging in again!")
    if response.status_code == 429:
        raise ConnectionError(
            f'Response Exception occurred in get_state_id! The response code was {response.status_code}.'
            f' The content is {response.content}')
    if response.status_code != 200:
        raise Exception(
            f'Response Exception occurred in get_state_id! The response code was {response.status_code}.'
            f' The content is {response.content}')
    states = response.json()['states']
    for the_state in states:
        if state.title() == the_state['state_name']:
            return the_state['state_id']


def get_district_id(state_id, district):
    response = _get_response('getAllDistricts', url={'state_id': state_id})
    if response.status_code == 401:
        raise ConnectionError("Session Expired, logging in again!")
    if response.status_code == 429:
        raise ConnectionError(
            f'Response Exception occurred in get_district_id! The response code was {response.status_code}.'
            f' The content is {response.content}')
    if response.status_code != 200:
        raise Exception(
            f'Response Exception occurred in get_district_id! The response code was {response.status_code}.'
            f' The content is {response.content}')
    districts = response.json()['districts']
    for the_districts in districts:
        if district.title() == the_districts['district_name']:
            return the_districts['district_id']


def schedule_appointment(dose, session_id, slot, beneficiary_id, captcha, bearer_token):
    response = _get_response("schedule", header_append={
        "authorization": "Bearer {}".format(bearer_token)
    }, json={
        "dose": dose,
        "session_id": session_id,
        "slot": slot,
        "captcha": captcha,
        "beneficiaries": beneficiary_id
    })
    if response.status_code == 401:
        raise ConnectionError("Session Expired, logging in again!")
    if response.status_code == 429:
        raise ConnectionError(
            f'Response Exception occurred in schedule_appointment! The response code was {response.status_code}.'
            f' The content is {response.content}')
    if response.status_code != 200:
        raise Exception(
            f'Response Exception occurred in schedule_appointment! The response code was {response.status_code}.'
            f' The content is {response.content}')
    return response


def get_captcha(bearer_token):
    response = _get_response("getRecaptcha", header_append={
        "authorization": "Bearer {}".format(bearer_token)
    }, json={})
    if response.status_code == 401:
        raise ConnectionError("Session Expired, logging in again!")
    if response.status_code == 429:
        raise ConnectionError(
            f'Response Exception occurred in get_captcha! The response code was {response.status_code}.'
            f' The content is {response.content}')
    if response.status_code != 200:
        raise Exception(
            f'Response Exception occurred in get_captcha! The response code was {response.status_code}.'
            f' The content is {response.content}')
    return response
