# FUCKING HUNGER GAMES WHEN SUPREME LEADER ENJOYS WATCHING PEOPLE BATTLE IT OUT FOR VACCINE.

# Selenium imports
import cgi
import datetime

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Other imports
import api
from time import sleep
from pathlib import Path
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import sys
import time
import socket
import logging
import json
from tabulate import tabulate
import svg_decode

PHONE_NUMBER = None
USER_STATE = None
USER_DISTRICT = None
AGE = None
NAME = None
COVISHIELD = None
COVAXIN = None
SPUTNIK = None
PAID = None
FREE = None
HOSPITAL = None
PIN_CODE = None
SLOT = None
DOSE = 1
MODE = 'Normal'
DEVICE = "Android"
REFRESH_TIMES = 1
BROWSER = 'Chrome'
OTP = 'Auto'
DRY = None
# ===== iOS Specefic Configs =====
_IOS_PREVIOUS_IP = ''
_IOS_OTP = ''

# create logger
logger = logging.getLogger('hungergames')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


def setup():
    logger.info("Warning: Application is still in beta, has pointed edges. Very stabby. Much wow.")
    logger.info(
        "\nWelcome to Hunger Games!\nOnly technologists who can code can get the vaccine, therfore, leading to a selection bias in the population! Wohoo!\n\n")
    global PHONE_NUMBER
    global USER_STATE
    global USER_DISTRICT
    global AGE
    global NAME
    global COVISHIELD
    global COVAXIN
    global SPUTNIK
    global PAID
    global FREE
    global HOSPITAL
    global PIN_CODE
    global SLOT
    global DOSE
    global DEVICE
    global REFRESH_TIMES
    global BROWSER
    global OTP
    global DRY
    global MODE
    settings = os.path.join(os.getcwd(), "settings.txt")
    if os.path.exists(settings):
        with open(settings, 'r') as the_file:
            lines = the_file.readlines()
            if len(lines) < 4:
                raise ValueError(
                    "Please make sure that there are at least 3 fields in the settings.txt file, that is, Phone, State, District and Age")
            for line in lines:
                if line.split(':')[0].lower() == 'phone':
                    PHONE_NUMBER = line.split(':')[1].strip()
                if line.split(':')[0].lower() == 'state':
                    USER_STATE = line.split(':')[1].strip()
                if line.split(':')[0].lower() == 'district':
                    USER_DISTRICT = line.split(':')[1].strip()
                if line.split(':')[0].lower() == 'age':
                    AGE = int(line.split(':')[1].strip())
                if line.split(':')[0].lower() == 'name':
                    NAME = line.split(':')[1].strip()
                if line.split(':')[0].lower() == 'covishield':
                    COVISHIELD = line.split(':')[1].strip()
                if line.split(':')[0].lower() == 'covaxin':
                    COVAXIN = line.split(':')[1].strip()
                if line.split(':')[0].lower() == 'sputnik':
                    SPUTNIK = line.split(':')[1].strip()
                if line.split(':')[0].lower() == 'paid':
                    PAID = line.split(':')[1].strip()
                if line.split(':')[0].lower() == 'free':
                    FREE = line.split(':')[1].strip()
                if line.split(':')[0].lower() == 'hospital':
                    HOSPITAL = line.split(':')[1].strip()
                if line.split(':')[0].lower() == 'pin':
                    PIN_CODE = line.split(':')[1].strip()
                if line.split(':')[0].lower() == 'slot':
                    SLOT = line.split(':')[1].strip()
                if line.split(':')[0].lower() == 'dose':
                    DOSE = int(line.split(':')[1].strip())
                if line.split(':')[0].lower() == 'device':
                    DEVICE = line.split(':')[1].strip()
                if line.split(':')[0].lower() == 'refresh':
                    REFRESH_TIMES = float(line.split(':')[1].strip())
                if line.split(':')[0].lower() == 'browser':
                    BROWSER = line.split(':')[1].strip()
                if line.split(':')[0].lower() == 'otp':
                    OTP = line.split(':')[1].strip()
                if line.split(':')[0].lower() == 'dry':
                    DRY = line.split(':')[1].strip()
                if line.split(':')[0].lower() == 'mode':
                    MODE = line.split(':')[1].strip()
    else:
        PHONE_NUMBER = input("Your Number: ")
        USER_STATE = input("Your State: ").lower()
        USER_DISTRICT = input("Your District: ").lower()
        AGE = int(input("Your Age (Enter either 18 or 45): ").lower())
        NAME = input("Your Name: ").lower()
        COVISHIELD = input("Covishield? (Press Enter to not apply this filter): ").lower()
        if COVISHIELD == '':
            COVISHIELD = None
        COVAXIN = input("Covaxin? (Press Enter to not apply this filter): ").lower()
        if COVAXIN == '':
            COVAXIN = None
        SPUTNIK = input("Sputnik? (Press Enter to not apply this filter): ").lower()
        if SPUTNIK == '':
            SPUTNIK = None
        PAID = input("Paid? (Press Enter to not apply this filter): ").lower()
        if PAID == '':
            PAID = None
        FREE = input("Free? (Press Enter to not apply this filter): ").lower()
        if FREE == '':
            FREE = None
        HOSPITAL = input("Hospital? (Press Enter to not search via preferred hospital): ").lower()
        if HOSPITAL == '':
            HOSPITAL = None
        PIN_CODE = input(
            "Pin Code? (Press Enter to leave blank): ").lower()
        if PIN_CODE == '':
            PIN_CODE = None
        DOSE = input(
            "Enter Dose Number. It is either 1 or 2. (Press Enter to leave blank): ").lower()
        if DOSE == '':
            DOSE = 1
        else:
            DOSE = int(DOSE)
        DEVICE = input(
            "Enter Enter Mobile Device. It is either Android or iOS. (Press Enter to leave blank, default is Android): ").lower()
        if DEVICE == '':
            DEVICE = "Android"
        REFRESH_TIMES = input("Enter Refresh Times: ").lower()
        if REFRESH_TIMES == '':
            REFRESH_TIMES = 1
        else:
            REFRESH_TIMES = int(REFRESH_TIMES)
        BROWSER = input("Enter Browser (Values are Chrome or Firefox, defaults to Chrome): ").lower()
        if BROWSER == '':
            BROWSER = 'Chrome'
        OTP = input("Enter OTP Mode (Values are Auto or Manual, defaults to Auto): ").lower()
        if OTP == '':
            OTP = 'Auto'
        MODE = input("Enter Mode (Values are Normal or Ultra, defaults to Normal): ").lower()
        if MODE == '':
            MODE = 'Normal'

    if HOSPITAL is not None:
        HOSPITAL = [hosp.strip() for hosp in HOSPITAL.split(',')]

    if PIN_CODE is not None:
        PIN_CODE = [pin.strip() for pin in PIN_CODE.split(',')]


def get_ip():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        sock.connect(('10.255.255.255', 1))
        ip = sock.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        sock.close()
    return ip


class RequestHandler(BaseHTTPRequestHandler):

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        global _IOS_OTP
        # logger.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        output = ''
        output += '<html><body>'
        output += '<h1>IP Address is </h1>'
        output += '<h3>' + str(get_ip()) + '</h3>' + '</br>'
        output += '</body></html>'
        self.wfile.write(output.encode())

        # self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        global _IOS_OTP
        if self.path.endswith('/' + PHONE_NUMBER):
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            if ctype != 'application/json':
                self.send_response(400)
                self.end_headers()

            length = int(self.headers.get('content-length'))
            body = json.loads(self.rfile.read(length))
            _IOS_OTP = body['message'].split(' ')[6].strip('.')

            self._set_response()
            raise KeyboardInterrupt


def launch_browser():
    """

    Returns
    -------
    WebDriver
        Returns the Selenium Chrome Webdriver Handler

    """
    global _IOS_PREVIOUS_IP
    global BROWSER

    if BROWSER.lower() == 'firefox':
        options = webdriver.FirefoxOptions()
    else:
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
    script_directory = Path().absolute()
    options.add_argument(os.path.join(f"--user-data-dir={script_directory}", "cd"))
    if sys.platform == 'win32':
        if BROWSER.lower() == 'firefox':
            driver = webdriver.Firefox(
                executable_path=os.path.join(os.getcwd(), 'dependencies', 'windows', 'geckodriver.exe'),
                options=options)
        else:
            driver = webdriver.Chrome(os.path.join(os.getcwd(), 'dependencies', 'windows', 'chromedriver.exe'),
                                      options=options)
    elif sys.platform == 'darwin':
        if BROWSER.lower() == 'firefox':
            driver = webdriver.Firefox(
                executable_path=os.path.join(os.getcwd(), 'dependencies', 'mac', 'geckodriver'),
                options=options)
        else:
            driver = webdriver.Chrome(os.path.join(os.getcwd(), 'dependencies', 'mac', 'chromedriver'),
                                      options=options)
    elif 'linux' in sys.platform:
        if BROWSER.lower() == 'firefox':
            driver = webdriver.Firefox(
                executable_path=os.path.join(os.getcwd(), 'dependencies', 'linux', 'geckodriver'),
                options=options)
        else:
            driver = webdriver.Chrome(os.path.join(os.getcwd(), 'dependencies', 'linux', 'chromedriver'),
                                      options=options)
    else:
        raise Exception("Unsupported Platform! Please use either a Windows, Linux or Mac OS system!")
    return driver


def open_website(driver):
    driver.maximize_window()
    driver.get(r'https://www.cowin.gov.in/')
    if DEVICE.lower() == "android":
        driver.execute_script("window.open('" + "https://messages.google.com/web/authentication" + "', '_blank')")
    elif DEVICE.lower() == 'ios':
        ip = get_ip()
        if _IOS_PREVIOUS_IP != ip:
            logger.info(
                'Your IP Address is --> ' + str(ip) + '. Please enter this IP in your iPhone, as shown in the Manual.')
            input('After you have entered this IP address, press any key to continue')
            driver.execute_script("window.open('" + "https://localhost:1337" + "', '_blank')")
    else:
        raise Exception("Device should be either iOS or Android!")
    sleep(.5)
    driver.execute_script("window.open('" + "https://selfregistration.cowin.gov.in/" + "', '_blank')")
    sleep(.5)


def open_messages(driver):
    if DEVICE.lower() == 'android':
        driver.switch_to.window(driver.window_handles[2])
        logger.info("\n>> Waiting for authentication from Google Messages")
        sleep(.5)
        while driver.current_url != r"https://messages.google.com/web/conversations":
            driver.get(r"https://messages.google.com/web/conversations")
            sleep(1)
            if driver.current_url == "https://messages.google.com/web/authentication":
                toggle = WebDriverWait(driver, 30).until(
                    ec.presence_of_element_located((By.CLASS_NAME, "mat-slide-toggle-thumb")))
                toggle.click()
            sleep(20)
    elif DEVICE.lower() == 'ios':
        pass
    else:
        raise Exception("Device should be either iOS or Android!")


def get_otp(driver):
    """

    Parameters
    ----------
    driver : WebDriver
             The Selenium ChromeDriver handlebar

    Returns
    -------
    list
        Returns the OTP in the form of a list

    """
    if DEVICE.lower() == 'android':
        driver.switch_to.window(driver.window_handles[2])
        driver.get('https://messages.google.com/web/conversations')
        sleep(5)
        wait = WebDriverWait(driver, 15)
        wait.until(ec.presence_of_all_elements_located((By.TAG_NAME, r"mws-conversation-list-item")))
        msg_container = driver.find_elements_by_tag_name(r"mws-conversation-list-item")[0]
        msg_container.find_element_by_tag_name("a").click()
        query = "//div[contains(@class, 'text-msg') and contains(@class, 'ng-star-inserted')]"
        logger.info(">> Found OTP!")
        driver.get('https://messages.google.com/web/conversations')
        wait.until(ec.presence_of_all_elements_located((By.TAG_NAME, r"mws-conversation-list-item")))
        msg_container = driver.find_elements_by_tag_name(r"mws-conversation-list-item")[0]
        msg_container.find_element_by_tag_name("a").click()
        wait.until(ec.presence_of_all_elements_located((By.XPATH, query)))
        all_msg_txt = driver.find_elements_by_xpath(query)

        unfiltered_otp = all_msg_txt[len(all_msg_txt) - 1].text
        otp = []
        for word in unfiltered_otp:
            if word.isdigit():
                otp.append(word)
        otp.pop()
        logger.info(">> Received OTP")
        return ''.join(otp)
    elif DEVICE.lower() == 'ios':
        run()
        return _IOS_OTP
    else:
        raise Exception("Device should be either iOS or Android!")


def run(server_class=HTTPServer, handler_class=RequestHandler, port=1337):
    """
    Launches server

    Returns
    -------
    None
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logger.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logger.info('Stopping httpd...\n')


def login(driver):
    """

    Parameters
    ----------
    driver : WebDriver
             The Selenium ChromeDriver handlebar

    Returns
    -------
    str
        bearer_token: The authentication token

    """
    global OTP
    bearer_token = ''
    if OTP.lower() == 'auto':
        open_messages(driver)
        driver.switch_to.window(driver.window_handles[2])
        trxn_resp = api.generate_otp(PHONE_NUMBER)
        sleep(1)
        otp = get_otp(driver)
        bearer_token = api.validate_otp(otp, trxn_resp)
    elif OTP.lower() == 'manual':
        trxn_resp = api.generate_otp(PHONE_NUMBER)
        otp = input("Enter OTP:")
        bearer_token = api.validate_otp(otp, trxn_resp)
    sleep(1)
    return bearer_token


def find_vaccines(centers):
    global SLOT
    vaccines = ['COVISHIELD' if COVISHIELD is not None else None,
                'COVAXIN' if COVAXIN is not None else COVAXIN,
                'SPUTNIK' if SPUTNIK is not None else SPUTNIK]
    if all([vaccine_type is None for vaccine_type in vaccines]) is True:
        vaccines = ['COVISHIELD', 'COVAXIN', 'SPUTNIK']
    payment = ['FREE' if FREE is not None else None,
               'PAID' if PAID is not None else None]
    if all([payment_type is None for payment_type in payment]) is True:
        payment = ['FREE', 'PAID']
    age_range = range(AGE, AGE + 27)
    hospitals = [hospital.lower() for hospital in HOSPITAL]
    logger.info(f'Filters are {vaccines} and {payment}')

    for center in centers:
        sessions = center['sessions']
        if HOSPITAL is not None:
            if center['name'].lower() not in hospitals:
                continue
        for session in sessions:
            with open(f"{datetime.datetime.now().strftime('%Y%m%d')}_{os.getpid()}.log.json", 'w') as outfile:
                json.dump(center, outfile, indent=4)
            logger.info('==================================================================')
            logger.info(f"Center name is: {center['name']}")
            logger.info(f"Center Date is: {session['date']}")
            if session['min_age_limit'] not in age_range:
                logger.info(f"Age is {AGE}. Center {center['name']} minimum age is {session['min_age_limit']}")
                logger.info('==================================================================')
                continue
            if session['vaccine'] not in vaccines:
                logger.info(f"Center vaccine is {session['vaccine']}. Filter is {vaccines}")
                logger.info('==================================================================')
                continue
            if session.get('vaccine_fees', None) is not None and 'PAID' not in payment:  # Want only free
                logger.info(f"No FREE vaccine at {center['name']}. Filter is {payment}")
                logger.info('==================================================================')
                continue
            if session.get('vaccine_fees', None) is None and 'FREE' not in payment:  # Want only paid
                logger.info(f"No PAID vaccine at {center['name']}. Filter is {payment}")
                logger.info('==================================================================')
                continue
            logger.info(f'Available capacity for Dose {DOSE}: {session["available_capacity_dose" + str(DOSE)]}')
            logger.info('==================================================================')
            if session['available_capacity_dose' + str(DOSE)] > 0:
                logger.info("Bingo, we have a hit!")
                logger.info('==================================================================')
                if int(SLOT) > len(session['slots']):
                    SLOT = 1
                return session['session_id'], session['slots'][int(SLOT) - 1]


def find_vaccines_by_sessions(sessions):
    global SLOT
    vaccines = ['COVISHIELD' if COVISHIELD is not None else None,
                'COVAXIN' if COVAXIN is not None else COVAXIN,
                'SPUTNIK' if SPUTNIK is not None else SPUTNIK]
    if all([vaccine_type is None for vaccine_type in vaccines]) is True:
        vaccines = ['COVISHIELD', 'COVAXIN', 'SPUTNIK']
    payment = ['FREE' if FREE is not None else None,
               'PAID' if PAID is not None else None]
    if all([payment_type is None for payment_type in payment]) is True:
        payment = ['FREE', 'PAID']
    age_range = range(AGE, AGE + 27)
    hospitals = [hospital.lower() for hospital in HOSPITAL]
    logger.info(f'Filters are {vaccines} and {payment}')

    for session in sessions:
        if HOSPITAL is not None:
            if session['name'].lower() not in hospitals:
                continue
        with open(f"{datetime.datetime.now().strftime('%Y%m%d')}_{os.getpid()}.log.json", 'w') as outfile:
            json.dump(session, outfile, indent=4)
        logger.info('==================================================================')
        logger.info(f"Center name is: {session['name']}")
        logger.info(f"Center Date is: {session['date']}")
        if session['min_age_limit'] not in age_range:
            logger.info(f"Age is {AGE}. Center {session['name']} minimum age is {session['min_age_limit']}")
            logger.info('==================================================================')
            continue
        if session['vaccine'] not in vaccines:
            logger.info(f"Center vaccine is {session['vaccine']}. Filter is {vaccines}")
            logger.info('==================================================================')
            continue
        if session.get('vaccine_fees', None) is not None and 'PAID' not in payment:  # Want only free
            logger.info(f"No FREE vaccine at {session['name']}. Filter is {payment}")
            logger.info('==================================================================')
            continue
        if session.get('vaccine_fees', None) is None and 'FREE' not in payment:  # Want only paid
            logger.info(f"No PAID vaccine at {session['name']}. Filter is {payment}")
            logger.info('==================================================================')
            continue
        logger.info(f'Available capacity for Dose {DOSE}: {session["available_capacity_dose" + str(DOSE)]}')
        logger.info('==================================================================')
        if session['available_capacity_dose' + str(DOSE)] > 0:
            logger.info("Bingo, we have a hit!")
            logger.info('==================================================================')
            if int(SLOT) > len(session['slots']):
                SLOT = 1
            return session['session_id'], session['slots'][int(SLOT) - 1]


def book_vaccine(session_id, slot, bearer_token):
    beneficiary_id = []
    beneficiaries = api.get_all_beneficiaries(bearer_token).json()
    for beneficiary in beneficiaries['beneficiaries']:
        if NAME.lower() == 'all':
            logger.info(f"Using Beneficiary: {beneficiary['name']}")
            beneficiary_id.append(beneficiary['beneficiary_reference_id'])
        elif beneficiary['name'].lower() in [name.lower().strip() for name in NAME.split(',')]:
            logger.info(f"Using Beneficiary: {beneficiary['name']}")
            beneficiary_id.append(beneficiary['beneficiary_reference_id'])
    if DRY is None:
        captcha = svg_decode.crack_captcha(api.get_captcha(bearer_token).json()['captcha'])
    else:
        captcha = svg_decode.crack_captcha(api.get_captcha(bearer_token).json()['captcha']) + 'SPARTA'
    logger.info(tabulate([['Dose', 1], ['session_id', session_id], ['slot', slot], ['beneficiary_id', beneficiary_id],
                          ['captcha', captcha], ['bearer_token', bearer_token]]))
    final = api.schedule_appointment(DOSE, session_id, slot, beneficiary_id, captcha, bearer_token)
    logger.info(f"Final Response is: {final}")
    if final.status_code == 200:
        return True
    else:
        return False


def check_beneficiary(bearer_token):
    beneficiaries = api.get_all_beneficiaries(bearer_token).json()
    for beneficiary in beneficiaries['beneficiaries']:
        if NAME.lower() == 'all':
            logger.info(f"Using Beneficiary: {beneficiary['name']}")
            logger.info(f"Beneficiary ID: {beneficiary['beneficiary_reference_id']}")
        elif beneficiary['name'].lower() in [name.lower().strip() for name in NAME.split(',')]:
            logger.info(f"Using Beneficiary: {beneficiary['name']}")
            logger.info(f"Beneficiary ID: {beneficiary['beneficiary_reference_id']}")


def main():
    """

    Returns
    -------
    int
        If the program executes successfully, it returns a 0, else, will return a 1

    """
    # ===== Step 1: Read the configuration file =====
    global REFRESH_TIMES
    global MODE
    setup()

    # ===== Step 2: Launch chrome and the websites =====
    if OTP.lower() != 'manual':
        driver = launch_browser()
        open_website(driver)
    else:
        driver = None

    # ===== Step 3: Do your Thang! =====
    vaccine_found = False
    proxy_counter = 0

    proxies = {
        "proxies": [
            "13.232.190.195:1234",
            "65.1.135.89:1234",
            "15.206.169.114:1234",
            "13.233.237.248:1234",
            "3.108.61.77:1234"

        ],
        "proxies2": [
            "3.108.42.239:1234",
            "15.206.145.158:1234",
            "52.66.204.246:1234",
            "13.233.113.252:1234",
            "13.127.218.137:1234"

        ],
        "proxies3": [
            "65.2.9.243:1234",
            "13.233.167.94:1234",
            "15.206.117.200:1234",
            "13.126.226.62:1234",
            "15.206.125.233:1234"

        ],
        "proxies4": [
            "13.232.190.195:1234",
            "65.1.135.89:1234",
            "15.206.169.114:1234",
            "13.233.237.248:1234",
            "3.108.61.77:1234",
            "3.108.42.239:1234",
            "15.206.145.158:1234",
            "52.66.204.246:1234",
            "13.233.113.252:1234",
            "13.127.218.137:1234"
            "65.2.9.243:1234",
            "13.233.167.94:1234",
            "15.206.117.200:1234",
            "13.126.226.62:1234",
            "15.206.125.233:1234",
            "13.126.33.199:1234",
            "3.6.92.15:1234",
            "3.6.38.116:1234",
            "13.235.246.134:1234",
            "13.233.132.11:1234"
        ]
    }

    proxies = proxies['proxies4']
    proxy_index = 0
    api.http_proxy = proxies[-1]
    api.https_proxy = proxies[-1]

    bearer_token = login(driver)

    while vaccine_found is False:
        try:

            # Check beneficiary before hand because people put wrong names!
            if proxy_counter == 0:
                check_beneficiary(bearer_token)

            if proxy_counter % 100 == 0:
                logger.info('Switching proxy!')
                previous_proxy_index = proxy_index
                if previous_proxy_index == len(proxies) - 1:
                    proxy_index = 0
                else:
                    proxy_index = previous_proxy_index + 1

                api.http_proxy = proxies[proxy_index]
                api.https_proxy = proxies[proxy_index]
                logger.info(f"Proxy: {proxies[proxy_index]}")
                logger.info(f"Proxy Index: {proxy_index}")

            proxy_counter += 1
            logger.info(f"while count: {proxy_counter}")

            centers = {}
            if PIN_CODE is not None:
                if MODE.lower() == 'ultra':
                    centers['sessions'] = []
                    for pin in PIN_CODE:
                        centers['sessions'].extend(api.find_by_pin(pin, bearer_token).json()['sessions'])
                    centers['sessions'] = list(filter(None, centers['sessions']))
                else:
                    centers['centers'] = []
                    for pin in PIN_CODE:
                        centers['centers'].extend(api.calendar_by_pin(pin, bearer_token).json()['centers'])
                    centers['centers'] = list(filter(None, centers['centers']))
            else:
                state_id = api.get_state_id(USER_STATE)
                district_id = api.get_district_id(state_id, USER_DISTRICT)
                if MODE.lower() == 'ultra':
                    centers = api.find_by_district(district_id, bearer_token).json()
                else:
                    centers = api.calendar_by_district(district_id, bearer_token).json()
            if MODE.lower() == 'ultra':
                if len(centers['sessions']) == 0:
                    logger.info('No centers found!')
                    continue
            else:
                if len(centers['centers']) == 0:
                    logger.info('No centers found!')
                    sleep(REFRESH_TIMES)
                    continue

            logger.info('Centers found!')
            logger.info('Prepping Find Vaccines')
            if MODE.lower() == 'ultra':
                session_id_and_slot = find_vaccines_by_sessions(centers['sessions'])
            else:
                session_id_and_slot = find_vaccines(centers['centers'])
            logger.info(f"session_id_and_slot is {session_id_and_slot}")
            if session_id_and_slot is not None:
                logger.info('Prepping to book vaccine')
                try:
                    vaccine_booking = book_vaccine(session_id_and_slot[0], session_id_and_slot[1], bearer_token)
                    if vaccine_booking is True:
                        logger.info("WooHooo!")
                        break
                    else:
                        logger.info('Response code was not 200 while booking vaccine! Something went wrong! Retrying!')
                        continue
                except Exception as e:
                    logger.info(e)
                    continue
            sleep(REFRESH_TIMES)
        except ConnectionError as ce:
            logger.info(ce)
            bearer_token = login(driver)
            continue


if __name__ == '__main__':
    sys.exit(main())
