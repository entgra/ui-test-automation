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
import pytest
import selenium_test_cases.components.util.generalUtils as generalUtils
import selenium_test_cases.components.util.constants as constants


@pytest.fixture()
def driver():
    driver = generalUtils.chrome_driver()
    yield driver
    driver.close()
    driver.quit()


def test_1_initial_endpoint_mgt_login(driver):
    generalUtils.initial_endpoint_mgt_login(driver)


def test_2_initial_app_publisher_login(driver):
    generalUtils.initial_app_publisher_login(driver)


def test_3_initial_app_store_login(driver):
    generalUtils.initial_app_store_login(driver)


def test_4_login(driver):
    generalUtils.login(driver)