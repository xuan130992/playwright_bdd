import time

import pytest
from playwright.sync_api import Page
from pytest_bdd import when, parsers, then, given, scenarios
from tests.pages.partners_page.ugc_managerment_page.mod_managerment_page.mod_register_page import mod_register
from tests.pages.partners_page.ugc_managerment_page.mod_managerment_page.navigate_mod_management_page import navigate_mod_managementPage
from tests.lib.common_functions import commonFunctions
scenarios("../../../../features/partners/ugc_management/mod_management/register_mini_mod.feature")
@pytest.fixture
def commonFunctions_page(page:Page):
    return commonFunctions(page)
@pytest.fixture
def mod_register_page(page:Page):
    return mod_register(page)
@pytest.fixture
def navigate_mod_management_page(page:Page,base_url:str):
    return navigate_mod_managementPage(page,base_url)
@given('I go to page mod management')
def navigate_mod_management(navigate_mod_management_page):
    navigate_mod_management_page.navigate_mod_management()
@then('I click registration button')
def click_registration_button(navigate_mod_management_page):
    navigate_mod_management_page.click_registration_button()
@then(parsers.cfparse('I input information to create a new mod with {package_version} and {eng_description}'))
def mini_mod_register(mod_register_page,package_version:str,eng_description:str):
    mod_register_page.register_mini_mod(package_version,eng_description)
    mod_register_page.mod_name_created = mod_register_page.mod_name
@then('I click add screenshot button')
def click_add_screenshot_btn(mod_register_page):
    mod_register_page.click_screenshot_btn()
@then(parsers.cfparse('I upload {screenshot_image} with {filepath_image}'))
def upload_screenshot_image(commonFunctions_page,screenshot_image:str,filepath_image:str):
    commonFunctions_page.upload_image_mod(screenshot_image,filepath_image)
    print('upload screenshot')
    time.sleep(3)
@then(parsers.cfparse('I upload {android_file} with {filepath_android}'))
def upload_file_android(commonFunctions_page,android_file:str,filepath_android:str):
    commonFunctions_page.upload_image_mod(android_file,filepath_android)
    print('upload android')
    time.sleep(3)
@then(parsers.cfparse('I upload {iOs_file} with {filepath_iOS}'))
def upload_file_iOS(commonFunctions_page,iOs_file:str,filepath_iOS:str):
    commonFunctions_page.upload_image_mod(iOs_file,filepath_iOS)
    print('upload iOS')
    time.sleep(3)
@then(parsers.cfparse('I upload {windowns_file} with {filepath_windowns}'))
def upload_file_windowns(commonFunctions_page,windowns_file:str,filepath_windowns:str):
    commonFunctions_page.upload_image_mod(windowns_file,filepath_windowns)
    print('upload windowns')
    time.sleep(3)
@then(parsers.cfparse('I upload {server_file} with {filepath_server}'))
def upload_file_server(commonFunctions_page,server_file:str,filepath_server:str):
    commonFunctions_page.upload_image_mod(server_file,filepath_server)
    print('upload server')
    time.sleep(3)
@then('I click register button')
def click_register_button(mod_register_page):
    mod_register_page.click_register_btn()
    time.sleep(5)

@then('I can see new official mod')
def verify_new_mini_mod(commonFunctions_page,mod_register_page):
    commonFunctions_page.verify_register_new_mod_successful(mod_register_page.mod_name_created)