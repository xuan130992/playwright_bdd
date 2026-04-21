import pytest
from pytest_bdd import when, parsers, then, parser,given, scenarios
from playwright.sync_api import Playwright,Page
from tests.pages.partners_page.ingame_notice_page.ingame_notice_management_page import ingame_notice_management_page
from tests.pages.partners_page.ingame_notice_page.ingame_notice_register_page import register_ingame_notice_page
from tests.helper.common_functions import commonFunctions
scenarios("../../../features/partners/ingame_notice/register_ingame_notice.feature")

@pytest.fixture
def ingame_notice_register(page:Page):
    return register_ingame_notice_page(page)
@pytest.fixture
def ingame_notice_management(page:Page,base_url:str):
    return ingame_notice_management_page(page,base_url)
@pytest.fixture
def commonFunctions_page(page:Page):
    return commonFunctions(page)
@given('I go to page In-game Notice Management')
def navigate_ingame_notice_management(ingame_notice_management):
    ingame_notice_management.navigate_notice_management()
@when('I click the Register button')
def click_register_button(ingame_notice_management):
    ingame_notice_management.click_register1_button()
@then(parsers.parse('I select Platform {platform}'))
def select_platform(ingame_notice_register,platform:str):
    ingame_notice_register.select_platform(platform)
@then(parsers.parse('I select Display Area {display_area}'))
def select_display_area(ingame_notice_register,display_area:str):
    ingame_notice_register.select_display_area(display_area)
@then(parsers.parse('I select send type {send_type}'))
def select_send_type(ingame_notice_register,send_type:str):
    ingame_notice_register.select_send_type(send_type)
@then('I select countries')
def select_countries(ingame_notice_register):
    ingame_notice_register.select_notice_country()
@then(parsers.parse('I input the notice content'))
def input_notice_content(ingame_notice_register):
    ingame_notice_register.input_notice_content()

@then('I click the Register button')
def click_register_button2(ingame_notice_register):
    ingame_notice_register.click_notice_register()
@then('I verify the notice register successfully')
def verify_notice_register(commonFunctions_page,ingame_notice_register):
    commonFunctions_page.verify_register_notice_successful(ingame_notice_register.notice_content)


