import pytest
from playwright.sync_api import Page
from pytest_bdd import given, when, then, parsers, scenarios
from pytest_bdd.gherkin_parser import Scenario
from tests.lib.common_functions import commonFunctions
from tests.pages.partners_page.ugc_managerment_page.mod_managerment_page.mod_register_page import mod_register
from tests.pages.partners_page.ugc_managerment_page.mod_managerment_page.navigate_mod_management_page import navigate_mod_managementPage
scenarios("../../../../features/partners/ugc_management/mod_management/register_official_mod.feature")
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
@then('I input information to create a new mod with "{package_version}" and "{ingame_display_order}" and "{eng_oneline_description}" and "{eng_description}"')
def official_mod_register(mod_register_page,package_version:str,ingame_display_order:str,eng_oneline_description:str,eng_description:str):
    mod_register_page.register_official_mod(package_version,ingame_display_order,eng_oneline_description,eng_description)
@then('I click add screenshot button')
def click_add_screenshot_btn(mod_register_page,screenshot_image:str,filepath_image:str):
    mod_register_page.click_screenshot_btn(screenshot_image,filepath_image)
@then('I upload "{screenshot_image}" with "{filepath_image}"')
def upload_screenshot_image(commonFunctions_page,screenshot_image:str,filepath_image:str):
    commonFunctions_page.upload_image(screenshot_image,filepath_image)
@then('I upload "{android_file}" with "{filepath_android}" and "{iOs_file}" with "{filepath_iOS}" and "{windowns_file}" with "{filepath_windowns}" and "{server_file}" with "{filepath_server}"')
def upload_file(commonFunctions_page,android_file:str,filepath_android:str,iOs_file:str,filepath_iOS:str,windowns_file:str,filepath_windowns:str,server_file:str,filepath_server:str):
    commonFunctions_page.upload_image(android_file,filepath_android,iOs_file,filepath_iOS,windowns_file,filepath_windowns,server_file,filepath_server)
@then('I click register button')
def click_register_button(mod_register_page):
    mod_register_page.click_register_btn()

@then('I can see new official mod')
def verify_new_official_mod(commonFunctions_page):
    commonFunctions_page.verify_register_new_mod_successful(commonFunctions_page.mod_name)


