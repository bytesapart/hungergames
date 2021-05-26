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

    # print(json.dumps(request, indent=2))

    if request["type"] == "POST":
        return requests.post(url=request['url'], json=request['json'], headers=request['header'],
                             proxies=request['proxies'])
    elif request["type"] == "GET":
        return requests.get(url=request['url'], headers=request['header'], proxies=request['proxies'])


def _today():
    return "{}-{}-{}".format(datetime.date.today().day, datetime.date.today().month, datetime.date.today().year)


def _tomorrow():
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    return "{}-{}-{}".format(tomorrow.day, tomorrow.month, tomorrow.year)


def generate_otp(mobile):
    return _get_response("generateMobileOTP", json={
        "mobile": mobile,
        "secret": _secret
    })


def validate_otp(otp, trxn_resp):
    otp_hash = hashlib.sha256(otp.encode()).hexdigest()
    print(otp, otp_hash)

    response = _get_response("validateMobileOTP", json={
        "otp": otp_hash,
        "txnId": trxn_resp.json()['txnId']
    })

    bearer_token = response.json()['token']

    return bearer_token


def calendar_by_district(district_id, bearer_token):
    return _get_response("calendarByDistrict", header_append={
        "authorization": "Bearer {}".format(bearer_token)
    }, url={
        "district_id": district_id,
        "date": _tomorrow()
    })


def find_by_district(district_id, bearer_token):
    return _get_response("findByDistrict", header_append={
        "authorization": "Bearer {}".format(bearer_token)
    }, url={
        "district_id": district_id,
        "date": _tomorrow()
    })


def calendar_by_pin(pin, bearer_token):
    return _get_response("calendarByPIN", header_append={
        "authorization": "Bearer {}".format(bearer_token)
    }, url={
        "pincode": pin,
        "date": _tomorrow()
    })


def find_by_pin(pin, bearer_token):
    return _get_response("findByPIN", header_append={
        "authorization": "Bearer {}".format(bearer_token)
    }, url={
        "pincode": pin,
        "date": _tomorrow()
    })


def get_all_beneficiaries(bearer_token):
    return _get_response("beneficiaries", header_append={
        "authorization": "Bearer {}".format(bearer_token)
    })


def get_state_id(state):
    states = _get_response('getAllStates').json()['states']
    for the_state in states:
        if state.title() == the_state['state_name']:
            return the_state['state_id']


def get_district_id(state_id, district):
    districts = _get_response('getAllDistricts', url={'state_id': state_id}).json()['districts']
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


def get_captcha(bearer_token):
    return _get_response("getRecaptcha", header_append={
        "authorization": "Bearer {}".format(bearer_token)
    }, json={})
