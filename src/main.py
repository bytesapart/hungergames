# FUCKING HUNGER GAMES WHEN SUPREME LEADER ENJOYS WATCHING PEOPLE BATTLE IT OUT FOR VACCINE.

# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Other imports
from time import sleep
from pathlib import Path
from playsound import playsound
import os
import sys

PHONE_NUMBER = None
USER_STATE = None
USER_DISTRICT = None
AGE = None
COVISHIELD = None
COVAXIN = None
SPUTNIK = None
PAID = None
FREE = None
HOSPITAL = None
PIN_CODE = None


def setup():
    print("Warning: Application is still in beta, has pointed edges. Very stabby. Much wow.")
    print(
        "\nWelcome to Hunger Games!\nOnly technologists who can code can get the vaccine, therfore, leading to a selection bias in the population! Wohoo!\n\n")
    global PHONE_NUMBER
    global USER_STATE
    global USER_DISTRICT
    global AGE
    global COVISHIELD
    global COVAXIN
    global SPUTNIK
    global PAID
    global FREE
    global HOSPITAL
    global PIN_CODE
    settings = os.path.join(os.path.dirname(os.getcwd()), "settings.txt")
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
                    AGE = line.split(':')[1].strip()
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

    else:
        PHONE_NUMBER = input("Your Number: ")
        USER_STATE = input("Your State: ").lower()
        USER_DISTRICT = input("Your District: ").lower()
        AGE = input("Your Age (Enter either 18+ or 45+): ").lower()
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
        PIN_CODE = input("Pin Code? (Press Enter to leave blank. If you have entered a hospital, this is mandatory to enter): ").lower()
        if PIN_CODE == '':
            PIN_CODE = None

    if (HOSPITAL is not None and PIN_CODE is None) or (HOSPITAL is None and PIN_CODE is not None):
        raise ValueError("Please make sure that Hospital Name AND Pin BOTH are entered")


def select_state(driver):
    """

    Parameters
    ----------
    driver : WebDriver
             The Selenium ChromeDriver handlebar

    Returns
    -------
    None

    """
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(ec.presence_of_element_located((By.ID, "mat-select-0")))
        driver.find_element_by_id('mat-select-0').click()
        wait.until(ec.presence_of_element_located((By.ID, "cdk-overlay-0")))
        state_list = driver.find_elements_by_xpath("//div[@id='cdk-overlay-0']/div/div/mat-option/span")
        for state in state_list:
            if state.text.lower() == str(USER_STATE).lower():
                state.click()
                break
    except Exception:
        print('Exception occured in select_state() function! Retrying...')
        select_state(driver)


def select_district(driver):
    """

    Parameters
    ----------
    driver : WebDriver
             The Selenium ChromeDriver handlebar

    Returns
    -------
    None

    """
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(ec.presence_of_element_located((By.ID, "mat-select-2")))
        driver.find_element_by_id('mat-select-2').click()
        wait.until(ec.presence_of_element_located((By.ID, "cdk-overlay-1")))
        district_list = driver.find_elements_by_xpath("//div[@id='cdk-overlay-1']/div/div/mat-option/span")
        for district in district_list:
            if district.text.lower() == str(USER_DISTRICT).lower():
                district.click()
                break
    except Exception:
        print("Exception Occured! Retrying in function select_district()")
        select_district(driver)


def find_vaccines(driver):
    """

    Parameters
    ----------
    driver : WebDriver
             The Selenium ChromeDriver handlebar

    Returns
    -------
    list
        Returns a list of all the Vaccines information

    """
    sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    wait = WebDriverWait(driver, 20)
    query = "//div[contains(@class, 'mat-main-field') and contains(@class, 'center-main-field')]/mat-selection-list/div[contains(@class, 'ng-star-inserted')]"
    wait.until(ec.presence_of_all_elements_located((By.XPATH, query)))
    all_vaccine_info = []
    wait.until(ec.presence_of_all_elements_located((By.XPATH,
                                                    '//mat-list-option/div/div[2]/ion-row/ion-col[1]/div/h5')))
    wait.until(ec.presence_of_all_elements_located((By.XPATH,
                                                    '//mat-list-option/div/div[2]/ion-row/ion-col[2]/ul')))
    wait.until(ec.presence_of_all_elements_located((By.XPATH, "//li")))

    vaccine_rows = driver.find_elements_by_xpath(query)

    for vaccine_row in vaccine_rows:
        vaccine_center = vaccine_row
        vaccine_center_name = vaccine_center.find_element_by_xpath(".//h5[@class='center-name-title']").get_attribute(
            'textContent')
        vaccine_slot_avail_ul = vaccine_center.find_element_by_xpath(".//ul[@class='slot-available-wrap']")
        vaccine_info_about_slots = []
        vaccine_slot_li = vaccine_slot_avail_ul.find_elements_by_tag_name("li")
        for vaccine_slot in vaccine_slot_li:
            vaccine_info_about_slots.append(vaccine_slot.find_element_by_tag_name("a").get_attribute('textContent'))
        final_info_grabbed = f"      >>> Vaccine Centre: {vaccine_center_name} -> Info(+7) "
        for vaccine_slot in vaccine_info_about_slots:
            final_info_grabbed += vaccine_slot + " "
        all_vaccine_info.append((vaccine_center_name, vaccine_info_about_slots))
        print(final_info_grabbed)

    return all_vaccine_info


def check_vaccines(driver, vaccine_info):
    """

    Parameters
    ----------
    driver : Seleneium Webdriver
             The chromewebdriver handlebar
    vaccine_info : list
                   A list of vaccine information

    Returns
    -------

    """
    list_of_vaccines = []
    for i in range(len(vaccine_info)):
        for x in range(len(vaccine_info[i][1])):
            vaccine_info_fetched_text = vaccine_info[i][1][x]
            txt = "" + vaccine_info_fetched_text
            if vaccine_info_fetched_text == "NA" or vaccine_info_fetched_text == "Booked":
                continue
            elif txt.isnumeric():
                list_of_vaccines.append(i)
                break
    return list_of_vaccines


def play_alarm(vaccine_found):
    if vaccine_found is True:
        playsound(os.path.join(os.path.dirname(os.getcwd()), "alarm.mp3"))
        while True:
            sleep(0.17)
            playsound(os.path.join(os.path.dirname(os.getcwd()), "alarm.mp3"))


def launch_chrome():
    """

    Returns
    -------
    WebDriver
        Returns the Selenium Chrome Webdriver Handler

    """
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    script_directory = Path().absolute()
    options.add_argument(f"--user-data-dir={script_directory}\\cd")
    driver = webdriver.Chrome(os.path.join(os.getcwd(), 'dependencies', 'chromedriver.exe'), options=options)
    driver.maximize_window()
    driver.get(r'https://www.cowin.gov.in/')
    driver.execute_script("window.open('" + "https://messages.google.com/web/authentication" + "', '_blank')")
    sleep(1)
    driver.execute_script("window.open('" + "https://selfregistration.cowin.gov.in/" + "', '_blank')")
    sleep(1)
    return driver


def open_messages(driver):
    driver.switch_to.window(driver.window_handles[2])
    print("\n>> Waiting for authentication from Google Messages")
    sleep(2)
    if driver.current_url == "https://messages.google.com/web/authentication":
        toggle = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.CLASS_NAME, "mat-slide-toggle-thumb")))
        toggle.click()

    while driver.current_url != r"https://messages.google.com/web/conversations":
        driver.get(r"https://messages.google.com/web/conversations")
        sleep(3)
        pass


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
    driver.switch_to.window(driver.window_handles[2])
    driver.get('https://messages.google.com/web/conversations')
    sleep(7)
    wait = WebDriverWait(driver, 15)
    wait.until(ec.presence_of_all_elements_located((By.TAG_NAME, r"mws-conversation-list-item")))
    msg_container = driver.find_elements_by_tag_name(r"mws-conversation-list-item")[0]
    msg_container.find_element_by_tag_name("a").click()
    query = "//div[contains(@class, 'text-msg') and contains(@class, 'ng-star-inserted')]"
    print(">> Found OTP!")
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
            otp.append(int(word))
    otp.pop()
    print(">> Received OTP")
    return otp


def send_otp(driver):
    """
    Parameters
    ----------
    driver : WebDriver
             The Selenium ChromeDriver handlebar

    Returns
    -------
    None

    """
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://selfregistration.cowin.gov.in/')
    sleep(3)
    wait = WebDriverWait(driver, 15)
    wait.until(ec.presence_of_element_located((By.ID, "mat-input-0")))
    box = driver.find_element_by_id("mat-input-0")
    for n in str(PHONE_NUMBER):
        box.send_keys(n)
        # sleep(.3)
    wait.until(ec.presence_of_element_located((By.TAG_NAME, "ion-button")))
    button = driver.find_element_by_tag_name("ion-button")
    button.click()
    wait.until(ec.presence_of_element_located((By.ID, "mat-input-1")))
    sleep(5)
    print(">> Waiting for OTP")


def try_putting_otp(driver, otp):
    """

    Parameters
    ----------
    driver : Selenium WebDriver
             The ChromeDriver handlebar
    otp : list
          The one-time-password received on the mobile phone

    Returns
    -------
    bool
        Returns True if OTP is successfully put, else returns False
    """
    print(">> Now trying to put OTP")
    driver.switch_to.window(driver.window_handles[1])
    sleep(3)
    wait = WebDriverWait(driver, 30)
    wait.until(ec.presence_of_element_located((By.ID, "mat-input-1")))
    box = driver.find_element_by_id("mat-input-1")
    for char in otp:
        box.send_keys(char)
        # sleep(.6)
    sleep(1)
    wait.until(ec.presence_of_element_located((By.TAG_NAME, "ion-button")))
    button = driver.find_element_by_tag_name("ion-button")
    button.click()
    sleep(5)
    if driver.current_url == "https://selfregistration.cowin.gov.in/dashboard":
        print(">> Successfully Logged in!")


def switch_to_district(driver):
    """

    Parameters
    ----------
    driver : WebDriver
             The Selenium ChromeDriver handlebar

    Returns
    -------
    None

    """
    sleep(1)
    driver.find_element_by_class_name(r'status-switch').click()
    sleep(1)


def go_back_to_main_page(driver):
    driver.get("https://selfregistration.cowin.gov.in/dashboard")


def logout(driver):
    """

    Parameters
    ----------
    driver : WebDriver
             The Selenium ChromeDriver handlebar

    Returns
    -------
    None

    """
    wait = WebDriverWait(driver, 10)
    wait.until(ec.presence_of_element_located(
        (By.XPATH, "//ul[contains(@class, 'navigation') and contains(@class, 'logout-text')]")))
    driver.find_element_by_xpath("//ul[contains(@class, 'navigation') and contains(@class, 'logout-text')]/li").click()
    driver.get('https://messages.google.com/web/authentication')
    return


def login(driver):
    """

    Parameters
    ----------
    driver : WebDriver
             The Selenium ChromeDriver handlebar

    Returns
    -------
    None

    """
    open_messages(driver)
    driver.switch_to.window(driver.window_handles[2])
    send_otp(driver)
    otp = get_otp(driver)
    try_putting_otp(driver, otp)
    sleep(1)


def filter_table(driver):
    """

    Parameters
    ----------
    driver : WebDriver
             The Selenium ChromeDriver handlebar

    Returns
    -------
    None
    """
    filter_buttons = driver.find_elements_by_class_name("form-check")
    if AGE == '18+':
        filter_buttons[0].click()
    else:
        filter_buttons[1].click()
    if COVISHIELD is not None:
        filter_buttons[2].click()
    if COVAXIN is not None:
        filter_buttons[3].click()
    if SPUTNIK is not None:
        filter_buttons[4].click()
    if PAID is not None:
        filter_buttons[5].click()
    if FREE is not None:
        filter_buttons[6].click()


def main():
    """

    Returns
    -------
    int
        If the program executes successfully, it returns a 0, else, will return a 1

    """
    # ===== Step 1: Read the configuration file =====
    setup()

    # ===== Step 2: Launch chrome and the websites =====
    driver = launch_chrome()

    # ===== Step 3: Do your Thang! =====
    vaccine_found = False
    counting_entries = 1
    check_in_x_seconds = 2

    while vaccine_found is False:
        if driver.current_url != "https://selfregistration.cowin.gov.in/dashboard":
            print(">> User is logged out!    Trying to log back in 5 seconds...")
            sleep(5)
            login(driver)
        wait = WebDriverWait(driver, 30)
        print("\n>> Fetching fresh set of slots:")
        counting_entries += 1
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, "btnlist")))
        button_appointment_schedule = driver.find_element_by_class_name("btnlist").find_element_by_xpath("//li/a")
        button_appointment_schedule.click()
        # query_1 = "//ion-button[contains(@class, 'register-btn') and contains(@class, 'schedule-appointment') and contains(@class, 'md') and contains(@class, 'button') and contains(@class, 'button-solid') and contains(@class, 'ion-activatable') and contains(@class, 'ion-focusable') and contains(@class, 'hydrated')]"
        # wait.until(ec.presence_of_element_located((By.XPATH, query_1)))
        # button_appointment_schedule1 = driver.find_element_by_xpath(query_1)
        # button_appointment_schedule1.click()
        switch_to_district(driver)
        select_state(driver)
        sleep(.5)
        select_district(driver)
        driver.find_elements_by_tag_name("ion-button")[0].click()
        wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME, "form-check")))
        sleep(1)
        filter_table(driver)
        vaccine_info = find_vaccines(driver)
        list_of_vaccines_index = check_vaccines(driver, vaccine_info)
        if len(list_of_vaccines_index) > 0:
            vaccine_found = True
            print("\n\n\nFound vaccine(s)!!!!")
            for index in list_of_vaccines_index:
                print("      >>> " + vaccine_info[index][0])
            play_alarm(vaccine_info)
        else:
            print(f"Vaccine not found!     " + f"Retrying in {check_in_x_seconds} seconds..\n")
            # sleep(1)
            go_back_to_main_page(driver)
            sleep(check_in_x_seconds)


if __name__ == '__main__':
    sys.exit(main())
