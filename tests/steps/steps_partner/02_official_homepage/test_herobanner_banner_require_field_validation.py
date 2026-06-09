import pytest
from allure_commons import fixture
from playwright.sync_api import Page, Playwright
from pytest_bdd import given, when, then, scenarios, parsers, scenario
from tests.locators.Partner.official_homepage.common_locators import component_common_locators
from tests.pages.partners_page.official_homepage.register_common_component_page import register_common_component
from tests.locators.Partner.official_homepage.Herobanner_banner_locators import component_hero_banner_locators
from tests.locators.Partner.official_homepage.mod_component_locators import register_mod_component
from tests.helper.field_assertions import assert_locator_visible, fill_validation,get_error_locator
from tests.helper.common_functions import commonFunctions
from tests.steps.steps_partner.ingame_notice_steps.test_ingame_notice_steps import select_send_type

scenarios("../../../features/partners/official_homepage/checking_register_validation.feature" )
# def test_create_hero_banner_validation():
#     pass
@pytest.fixture
def register_common_component_page(page: Page,base_url):
    return register_common_component(page,base_url)
@pytest.fixture
def com_loc(page: Page):
    return component_common_locators(page)
@pytest.fixture
def banner_loc(page: Page):
    return component_hero_banner_locators(page)
@pytest.fixture
def mod_loc(page: Page):
    return register_mod_component(page)
@pytest.fixture
def filed_assertions_page():
    return assert_locator_visible
@pytest.fixture
def commonFunctions_page(page: Page):
    return commonFunctions(page)
@pytest.fixture (scope="session")
def component_type_state():
    return {"value": None}
# ===============Background steps==============
@given("I go to Page component management")
def selectOfficialHomepage(register_common_component_page):
    register_common_component_page.select_official_homepage()
@given(parsers.cfparse('I selects country "{country}" and clicks Register Component button'))
def selectCountry_Register(register_common_component_page,country:str):
    register_common_component_page.choose_country(country)
    register_common_component_page.click_register_btn()
#================scenario steps=============
@given(parsers.parse('I select "{component_type}" component type'))
def selectComponent(register_common_component_page,component_type,component_type_state):
    register_common_component_page.select_component_type_page(component_type)
    component_type_state["value"]= component_type

@when(parsers.cfparse('I click Register button without filling any fields'))
def clickRegister(com_loc):
    com_loc.register_btn.click()

#==============================Banner Image mobile require=============
@then(parsers.cfparse('I input valid "{field}"'))
def fill_validation_filed(com_loc,banner_loc,mod_loc,field:str):
    fill_validation(com_loc,banner_loc,mod_loc,field)
@then('I click Add banner button')
def clickAddBanner(banner_loc):
    banner_loc.banner_btn.click()
@then(parsers.cfparse('I input invalid "{field}"'))
def fill_validation_filed(com_loc,banner_loc,mod_loc,field:str):
    fill_validation(com_loc,banner_loc,mod_loc,field)
@then(parsers.cfparse('I upload valid image to PC image'))
def upload_image_PC(commonFunctions_page,com_loc,banner_loc,component_type_state):
    value = component_type_state["value"].strip().strip('"')
    print(f"repr: {repr(value)}")
    print(f"bytes: {value.encode('utf-8')}")
    print(f"== Hero Banner: {value == 'Hero Banner'}")
    if (value=="Hero Banner"):
        commonFunctions_page.upload_image(banner_loc.upload_locator_PC, banner_loc.filepath_PC)
    else:
        commonFunctions_page.upload_image(banner_loc.upload_locator_PC, banner_loc.filepath_PC_banner)
@when(parsers.cfparse('I click Register button'))
def clickRegister(com_loc):
    com_loc.register_btn.click()
@then(parsers.cfparse('I can see required error alert for "{field}" field'))
def verify_error_alert(filed_assertions_page,com_loc,banner_loc,mod_loc,field):
    locator=get_error_locator(com_loc,banner_loc,mod_loc,field)
    filed_assertions_page(locator)
@then(parsers.cfparse('I upload valid image to mobile image'))
def upload_image_PC(commonFunctions_page,com_loc,banner_loc,component_type_state):
    value = component_type_state["value"].strip().strip('"')
    if (value=="Hero Banner"):
        commonFunctions_page.upload_image(banner_loc.upload_locator_PC, banner_loc.filepath_mobile)
    else:
        commonFunctions_page.upload_image(banner_loc.upload_locator_PC, banner_loc.filepath_mobile_banner)
# @given("I go to Page component management")
# def selectOfficialHomepage(register_common_component_page):
#     register_common_component_page.select_official_homepage()
# @given(parsers.cfparse('I selects country "{country}" and clicks Register Component button'))
# def selectCountry_Register(register_common_component_page,country:str):
#     register_common_component_page.choose_country(country)
#     register_common_component_page.click_register_btn()
#================scenario steps=============
# @given(parsers.cfparse('I select {component_type} component type'))
# def selectComponent(register_common_component_page,component_type):
#     register_common_component_page.select_component_type_page(component_type)




