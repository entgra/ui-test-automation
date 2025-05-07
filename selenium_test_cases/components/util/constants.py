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

import selenium_test_cases.root_dir

# Configurations
# if is_headless set to True this will run in headless, otherwise(False) this will run in chrome browser
is_headless = False
# if is_remote is set to True this will run in remote host, otherwise(False) it will run locally
is_remote = True

PASSWORD_LOCAL = "admin"
PASSWORD_REMOTE_USER = "admin"

# common
HOST_LOCALHOST = "https://localhost:9443"
HOST_REMOTE = "https://uem.mgt.entgra.net"
ROOT_DIR = selenium_test_cases.root_dir.ROOT_DIR
ADMIN = "admin"
ADMIN_SUB_TENANT = "admin@automation.io"
URL_ENDPOINT_MGT = "/endpoint-mgt/devices"
URL_APP_PUBLISHER = "/app-publisher/apps"
URL_APP_STORE = "/store/android/applications"
RESOURCES_DIR = ROOT_DIR + "/components/resources"
RESOURCES_FILES_DIR = RESOURCES_DIR + "/files"
RESOURCES_ICONS_DIR = RESOURCES_DIR + "/icons"
RESOURCES_CERTIFICATES_DIR = RESOURCES_FILES_DIR + "/certificates"
RESOURCES_APK_DIR = RESOURCES_FILES_DIR + "/apk"
RESOURCES_ICONS_ENTGRA_DIR = RESOURCES_ICONS_DIR + "/entgra"
ENTGRA = "entgra"
AUTOMATION = "Automation"
ENTGRA2 = "entgra2"
EMAIL_ENTGRA = "automation@entgra.io"
MAC_ADDRESS = "A0:B0:CD:0E:FG:00"
MAC_ADDRESS2 = "A1:B1:CD:1E:FG:11"
ENTGRA_PARTIAL = "entg"
SERVICE_PROVIDER_1 = "Service Provider"
SERVICE_PROVIDER_2 = "Service Provider 2"


# Group
GROUP_NAME_1 = "Parent Group 1"
GROUP_DESCRIPTION_1 = "Parent Group Description 1"
GROUP_NAME_2 = "Parent Group 2"
GROUP_DESCRIPTION_2 = "Parent Group Description 2"
GROUP_NAME_EDITED = "Parent Group Edited"
GROUP_DESCRIPTION_EDITED = "Parent Group Description Edited"

SUB_GROUP_NAME_1 = "Sub Group 1"
SUB_GROUP_DESCRIPTION_1 = "Sub Group Description 1"

GROUP_EDIT_COMPONENT_NAME = "Group Name"
GROUP_EDIT_COMPONENT_DESCRIPTION = "Group Description"


# Icons and files
ENTGRA_IMAGE = RESOURCES_ICONS_ENTGRA_DIR + "/Entgra.jpeg"

# Sample certificate
SAMPLE_CERTIFICATE = RESOURCES_CERTIFICATES_DIR + "/sample.crt"
