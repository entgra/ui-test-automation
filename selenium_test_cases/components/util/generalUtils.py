# Copyright (c) 2018 - 2025 Entgra (Pvt) Ltd. (http://www.entgra.io) All Rights Reserved.
#
# Unauthorised copying/redistribution of this file, via any medium is strictly prohibited.
#
# Entgra (Pvt) Ltd. licenses this file to you under the Apache License,
# Version 2.0 (the "License"); you may not use this file except
# in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_test_cases.components.util import constants


def chrome_driver_headless():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('window-size=1920x1080')
    options.add_argument('--allow-insecure-localhost')
    driver = webdriver.Chrome(options=options)
    return driver


def chrome_driver_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('window-size=1920x1080')
    driver = webdriver.Chrome(options=options)
    return driver


def chrome_driver():
    if constants.is_headless:
        driver = chrome_driver_headless()
    else:
        driver = chrome_driver_browser()
    return driver


def login_remote_form(driver):
    driver.maximize_window()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))).send_keys(constants.ADMIN_SUB_TENANT)
    driver.find_element(By.ID, "password").send_keys(constants.PASSWORD_REMOTE_USER)

    # Clicking on "Remember me on this computer" checkbox
    driver.find_element(By.ID, "chkRemember").click()
    driver.find_element(By.TAG_NAME, "button").click()


def login_local_form(driver):
    if not constants.is_headless:
        driver.maximize_window()
        driver.find_element(By.ID, "details-button").click()
        driver.find_element(By.ID, "proceed-link").click()

    username = driver.find_element(By.ID, "username")
    # username.send_keys(constants.ADMIN)
    username.send_keys(constants.ADMIN_SUB_TENANT)

    pwd = driver.find_element(By.ID, "password")
    pwd.send_keys(constants.PASSWORD_LOCAL)
    # Clicking on "Remember me on this computer" checkbox
    driver.find_element(By.ID, "chkRemember").click()

    login_button = driver.find_element(By.TAG_NAME, "button")
    login_button.click()


def login_local(driver):
    driver.get(constants.HOST_LOCALHOST + constants.URL_ENDPOINT_MGT)
    login_local_form(driver)


def login_remote(driver):
    driver.get(constants.HOST_REMOTE + constants.URL_ENDPOINT_MGT)
    login_remote_form(driver)


def login(driver):
    # Choose the test server whether the remote or local
    if constants.is_remote:
        login_remote(driver)
    else:
        login_local(driver)


def consent_button(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(By.ID, "rememberApproval").click()
    driver.find_element(By.ID, "approve").click()


def initial_endpoint_mgt_login(driver):
    if constants.is_remote:
        driver.get(constants.HOST_REMOTE + constants.URL_ENDPOINT_MGT)
        login_remote_form(driver)
        consent_button(driver)
    else:
        driver.get(constants.HOST_LOCALHOST + constants.URL_ENDPOINT_MGT)
        login_local_form(driver)
        consent_button(driver)


def initial_app_publisher_login(driver):
    if constants.is_remote:
        driver.get(constants.HOST_REMOTE + constants.URL_APP_PUBLISHER)
        login_remote_form(driver)
        consent_button(driver)
    else:
        driver.get(constants.HOST_LOCALHOST + constants.URL_APP_PUBLISHER)
        login_local_form(driver)
        consent_button(driver)


def app_publisher_login(driver):
    if constants.is_remote:
        driver.get(constants.HOST_REMOTE + constants.URL_APP_PUBLISHER)
        login_remote_form(driver)
    else:
        driver.get(constants.HOST_LOCALHOST + constants.URL_APP_PUBLISHER)
        login_local_form(driver)


def initial_app_store_login(driver):
    if constants.is_remote:
        driver.get(constants.HOST_REMOTE + constants.URL_APP_STORE)
        login_remote_form(driver)
        consent_button(driver)

    else:
        driver.get(constants.HOST_LOCALHOST + constants.URL_APP_STORE)
        login_local_form(driver)
        consent_button(driver)


def app_store_login(driver):
    if constants.is_remote:
        driver.get(constants.HOST_REMOTE + constants.URL_APP_STORE)
        login_remote_form(driver)

    else:
        driver.get(constants.HOST_LOCALHOST + constants.URL_APP_STORE)
        login_local_form(driver)


def skip_tour_guide(driver):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Skip')]")))
    button = driver.find_element(By.XPATH, "//span[text()='Skip']")
    driver.execute_script("arguments[0].click();", button)


def verify_notification(driver, notification_text):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//div[text()='{notification_text}'] ["
                                                  "@class='ant-notification-notice-description']")))


def create_button(driver):
    create = driver.find_element(By.XPATH, "//span[contains(text(), 'Create')]")
    driver.execute_script("arguments[0].scrollIntoView();", create)
    create.click()
    driver.find_element(By.XPATH, "//span[contains(text(), 'Create')]")
    time.sleep(1)

def create_button_group(driver):
    login(driver)
    skip_tour_guide(driver)
    time.sleep(1)
    create_button(driver)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Group']"))).click()


def single_device_view(driver, device_name):
    login(driver)
    skip_tour_guide(driver)

    # Clicking on the device
    driver.find_element(By.XPATH, "//span[text()='" + device_name + "']").click()

    window_single_device_view = driver.window_handles[1]
    driver.switch_to.window(window_single_device_view)