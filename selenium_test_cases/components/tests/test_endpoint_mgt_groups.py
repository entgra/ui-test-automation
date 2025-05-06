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
from selenium_test_cases.components.endpoint_mgt.group import create_group


@pytest.fixture()
def driver():
    driver = generalUtils.chrome_driver()
    yield driver
    driver.close()
    driver.quit()


def test_create_parent_group_1(driver):
    create_group.create_parent_group(driver, constants.GROUP_NAME_1, constants.GROUP_DESCRIPTION_1, constants.ADMIN)


def test_create_sub_group(driver):
    create_group.create_sub_group(driver, constants.GROUP_NAME_1, constants.SUB_GROUP_NAME_1, constants.GROUP_DESCRIPTION_1, constants.ADMIN)


