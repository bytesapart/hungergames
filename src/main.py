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
import time
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
MODE = None
DOSE = 1


def setup():
    print("Warning: Application is still in beta, has pointed edges. Very stabby. Much wow.")
    print(
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
    global MODE
    global DOSE
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
                    AGE = line.split(':')[1].strip()
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
                if line.split(':')[0].lower() == 'mode':
                    MODE = line.split(':')[1].strip()
                if line.split(':')[0].lower() == 'dose':
                    DOSE = int(line.split(':')[1].strip())

    else:
        PHONE_NUMBER = input("Your Number: ")
        USER_STATE = input("Your State: ").lower()
        USER_DISTRICT = input("Your District: ").lower()
        AGE = input("Your Age (Enter either 18+ or 45+): ").lower()
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
        PIN_CODE = input(
            "Enter Dose Number. It is either 1 or 2. (Press Enter to leave blank): ").lower()
        if DOSE == '':
            DOSE = 1


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
        print('Exception occurred in select_state() function! Retrying...')
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
        print("Exception occurred! Retrying in function select_district()")
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
    try:
        sleep(.5)
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

        vaccine_hyperlink = None
        for vaccine_row in vaccine_rows:
            vaccine_center = vaccine_row
            vaccine_center_name = vaccine_center.find_element_by_xpath(
                ".//h5[@class='center-name-title']").get_attribute(
                'textContent')
            if HOSPITAL is not None:
                if HOSPITAL.lower() not in vaccine_center_name.lower():
                    continue
            vaccine_slot_avail_ul = vaccine_center.find_element_by_xpath(".//ul[@class='slot-available-wrap']")
            vaccine_info_about_slots = []
            vaccine_slot_li = vaccine_slot_avail_ul.find_elements_by_tag_name("li")
            for vaccine_slot in vaccine_slot_li:
                vaccine_info_about_slots.append(vaccine_slot.find_element_by_tag_name("a").get_attribute('textContent'))
                # sleep(.1)
                if vaccine_slot.find_element_by_tag_name("a").get_attribute('textContent').strip().isnumeric():
                    vaccine_hyperlink = vaccine_slot.find_element_by_tag_name("a")
                    break
            final_info_grabbed = f"      >>> Vaccine Centre: {vaccine_center_name} -> Info(+7) "
            for vaccine_slot in vaccine_info_about_slots:
                final_info_grabbed += vaccine_slot + " "
            all_vaccine_info.append((vaccine_center_name, vaccine_info_about_slots))
            print(final_info_grabbed)
            if HOSPITAL is not None:
                break
            if vaccine_hyperlink is not None:
                break

        return all_vaccine_info, vaccine_hyperlink
    except Exception:
        print("Exception occurred! Retrying in function find_vaccines()")
        vaccine_info, vaccine_hyperlink = find_vaccines(driver)
        return vaccine_info, vaccine_hyperlink


def check_vaccines(vaccine_info):
    """

    Parameters
    ----------
    vaccine_info : list
                   A list of vaccine information

    Returns
    -------

    """
    list_of_vaccines = []
    for i in range(len(vaccine_info)):
        for x in range(len(vaccine_info[i][1])):
            vaccine_info_fetched_text = vaccine_info[i][1][x]
            txt = str("" + vaccine_info_fetched_text).strip()
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
    options.add_argument(os.path.join(f"--user-data-dir={script_directory}", "cd"))
    if 'win' in sys.platform:
        driver = webdriver.Chrome(os.path.join(os.getcwd(), 'dependencies', 'windows', 'chromedriver.exe'),
                                  options=options)
    elif 'linux' in sys.platform:
        driver = webdriver.Chrome(os.path.join(os.getcwd(), 'dependencies', 'linux', 'chromedriver'),
                                  options=options)
    elif 'darwin' in sys.platform:
        driver = webdriver.Chrome(os.path.join(os.getcwd(), 'dependencies', 'mac', 'chromedriver'),
                                  options=options)
    else:
        raise Exception("Unsupported Platform! Please use either a Windows, Linux or Mac OS system!")
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
    sleep(1)
    while driver.current_url != r"https://messages.google.com/web/conversations":
        driver.get(r"https://messages.google.com/web/conversations")
        sleep(2)
        if driver.current_url == "https://messages.google.com/web/authentication":
            toggle = WebDriverWait(driver, 30).until(
                ec.presence_of_element_located((By.CLASS_NAME, "mat-slide-toggle-thumb")))
            toggle.click()
        sleep(40)


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
    sleep(.5)
    wait.until(ec.presence_of_element_located((By.TAG_NAME, "ion-button")))
    button = driver.find_element_by_tag_name("ion-button")
    sleep(.5)
    button.click()
    sleep(.5)
    if driver.current_url == "https://selfregistration.cowin.gov.in/dashboard":
        print(">> Successfully Logged in!")


def switch_to_district(driver, counting_entities):
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
        if MODE is not None and MODE.lower() == 'ultra' and counting_entities != 1:
            return None
        sleep(.5)
        driver.find_element_by_class_name(r'status-switch').click()
        sleep(.5)
    except Exception:
        print("Exception occurred! Retrying in function switch_to_district()")
        switch_to_district(driver, counting_entities)


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
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(ec.presence_of_element_located(
            (By.XPATH, "//ul[contains(@class, 'navigation') and contains(@class, 'logout-text')]")))
        driver.find_element_by_xpath(
            "//ul[contains(@class, 'navigation') and contains(@class, 'logout-text')]/li").click()
        driver.get('https://messages.google.com/web/authentication')
        return None
    except Exception:
        print("Exception occurred! Retrying in function logout()")
        logout(driver)


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
    if DOSE == 1:
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


def schedule_for_candidate(driver):
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
        if DOSE == 1:
            schedule_button = driver.find_elements_by_xpath(
                "//h3[contains(., '" + NAME + "')]/ancestor::ion-grid[contains(concat(' ', @class, ' '), ' cardblockcls ')]//ion-row[contains(concat(' ', @class, ' '), ' dose-data ')]//ul//a")[
                0]
        else:
            schedule_button = driver.find_elements_by_xpath(
                "//h3[contains(., '" + NAME + "')]/ancestor::ion-grid[contains(concat(' ', @class, ' '), ' cardblockcls ')]//ion-row[contains(concat(' ', @class, ' '), ' dose-data ')]//ul//a")[
                1]
        schedule_button.click()
    except Exception:
        print("Exception occurred! Retrying in function schedule_for_candidate()")
        schedule_for_candidate(driver)


def search_using_pin(driver):
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
        wait.until(ec.presence_of_element_located((By.XPATH, "//input[@appinputchar='pincode']")))
        driver.find_element_by_xpath("//input[@appinputchar='pincode']").click()
        box = driver.find_element_by_xpath("//input[@appinputchar='pincode']")
        for char in PIN_CODE:
            box.send_keys(char)
        wait.until(ec.presence_of_element_located((By.TAG_NAME, "ion-button")))
        # button = driver.find_element_by_tag_name("ion-button")
        # button.click()
    except Exception:
        print("Exception occurred! Retrying in function search_using_pin()")
        search_using_pin(driver)


def book_vaccine(driver):
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
        wait.until(ec.presence_of_element_located((By.ID, "captchaImage")))
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, "time-slot-list")))
        time_slots = driver.find_elements_by_xpath("//ion-button[contains(@class, 'time-slot')]")
        if SLOT is not None:
            time_to_pick = time_slots[int(SLOT) - 1]
        else:
            time_to_pick = time_slots[-1]
        time_to_pick.click()
        sleep(.5)
        data = driver.find_element_by_id("captchaImage").get_attribute('src')
        captcha = svg_decode.crack_captcha(data)
        box = driver.find_element_by_xpath("//input[@placeholder='Enter Security Code']")
        box.click()

        for char in captcha:
            box.send_keys(char)
        wait.until(ec.presence_of_element_located((By.XPATH, "//ion-button[@type='submit']")))
        driver.find_element_by_xpath("//ion-button[@type='submit']").click()
    except Exception:
        print("Exception occurred! Retrying in function book_vaccine()")
        book_vaccine(driver)


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
    counting_entries = 0
    check_in_x_seconds = 1

    start = time.time()

    while vaccine_found is False:
        try:
            end = time.time()
            hours, rem = divmod(end - start, 3600)
            minutes, seconds = divmod(rem, 60)

            if MODE is None or MODE.lower() == 'normal':
                if int(minutes) > 13:
                    start = time.time()
                    logout(driver)
                    sleep(1.5)
                if driver.current_url != "https://selfregistration.cowin.gov.in/dashboard":
                    print(">> User is logged out!    Trying to log back in 5 seconds...")
                    sleep(1.5)
                    login(driver)
            elif MODE.lower() == 'ultra':
                if int(minutes) > 13:
                    counting_entries = 0
                    start = time.time()
                    logout(driver)
                    sleep(1.5)
                if driver.current_url != "https://selfregistration.cowin.gov.in/appointment":
                    print(">> User is logged out!    Trying to log back in 5 seconds...")
                    sleep(1.5)
                    login(driver)

            wait = WebDriverWait(driver, 30)
            print("\n>> Fetching fresh set of slots:")
            counting_entries += 1
            wait.until(ec.presence_of_element_located((By.CLASS_NAME, "btnlist")))

            if MODE.lower() == 'ultra' and counting_entries == 1:
                schedule_for_candidate(driver)
            elif MODE.lower() == 'normal':
                schedule_for_candidate(driver)
            elif MODE is None:
                schedule_for_candidate(driver)

            if PIN_CODE is not None:
                search_using_pin(driver)
            else:
                switch_to_district(driver, counting_entries)
                select_state(driver)
                sleep(.5)
                select_district(driver)
            driver.find_elements_by_tag_name("ion-button")[0].click()
            wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME, "form-check")))
            sleep(.5)
            filter_table(driver)
            vaccine_info, vaccine_hyperlink = find_vaccines(driver)
            list_of_vaccines_index = check_vaccines(vaccine_info)
            if len(list_of_vaccines_index) > 0:
                vaccine_found = True
                print("\n\n\nFound vaccine(s)!!!!")
                for index in list_of_vaccines_index:
                    print("      >>> " + vaccine_info[index][0])
                # play_alarm(vaccine_info)
                vaccine_hyperlink.click()
                book_vaccine(driver)
                sleep(20)
            else:
                print(f"Vaccine not found!     " + f"Retrying in {check_in_x_seconds} seconds..\n")
                if MODE.lower() == 'normal':
                    go_back_to_main_page(driver)
                elif MODE is None:
                    go_back_to_main_page(driver)
                sleep(check_in_x_seconds)
        except Exception:
            driver.quit()
            driver = launch_chrome()

            # ===== Step 3: Do your Thang! =====
            vaccine_found = False
            counting_entries = 0
            check_in_x_seconds = 1

            start = time.time()
            continue


if __name__ == '__main__':
    sys.exit(main())
