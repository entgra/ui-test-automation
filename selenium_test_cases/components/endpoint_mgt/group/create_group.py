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

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import selenium_test_cases.components.util.generalUtils as generalUtils
import selenium_test_cases.components.util.constants as constants


def create_group(driver, group_name, group_description, role_name):
    driver.find_element(By.ID, "basic_GroupName").send_keys(group_name)
    driver.find_element(By.ID, "basic_GroupDescription").send_keys(group_description)
    # those continue button are in the same code(DOM), therefore as we proceeding those continue buttons will accumulate
    # In here we capture the 3rd continue button
    driver.find_element(By.XPATH,
                        "//form[@id='basic']/descendant::button[@type='submit']/span[text()='Continue']").click()
    driver.find_element(By.CLASS_NAME, "ant-select-selection-overflow").click()

    # adding admin role to group
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
        By.XPATH, f"//div[text()='{role_name}'] [@class='ant-select-item-option-content']"))).click()
    driver.find_element(By.XPATH, "//p[text()='Select user roles']/ancestor-or-self::div["
                                  "@class='ant-card-body']/descendant::button[@type='submit']/span[text("
                                  ")='Continue']").click()
    generalUtils.verify_notification(driver, "Successfully added the group.")


def create_parent_group(driver, group_name, group_description, role_name):
    generalUtils.create_button_group(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
        By.XPATH, "//span[text()='Continue']"))).click()
    create_group(driver, group_name, group_description, role_name)


def create_sub_group(driver, parent_group_name, group_name, group_description, role_name):
    generalUtils.create_button_group(driver)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@value='hierarchical']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
        By.XPATH, f"//span[text()='{parent_group_name}'] [@class='ant-tree-title']"))).click()
    driver.find_element(By.XPATH, "//div[@id='generalGroupSubPanel']/../descendant::button[@type='submit']/span[text("
                                  ")='Continue']").click()
    create_group(driver, group_name, group_description, role_name)


