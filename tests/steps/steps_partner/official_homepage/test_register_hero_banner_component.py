import pytest
from playwright.sync_api import Playwright,Page
from allure_commons import fixture
from pytest_bdd import given, when, then, scenarios, parsers
from tests.pages.partners_page.official_homepage.register_hero_banner_component_page import register_hero_banner_component
from tests.pages.partners_page.official_homepage.register_common_component_page import register_common_component
from tests.pages.official_website.main_display_page import main_display_page
from tests.lib.common_functions import commonFunctions
scenarios("../../../features/partners/official_homepage/register_hero_banner_component.feature")
@pytest.fixture
def register_common_component_page(page:Page,base_url):
    return register_common_component(page,base_url)
@pytest.fixture
def register_hero_banner_component_page(page: Page):
    return register_hero_banner_component(page)
@pytest.fixture
def commonFunctions_page(page:Page):
    return commonFunctions(page)
@pytest.fixture
def main_displayed_page(page:Page,main_display_url):
    return main_display_page(page,main_display_url)

@given("I go to Page component management")
def selectOfficialHomepage(register_common_component_page):

    register_common_component_page.select_official_homepage()

@when(parsers.cfparse('I selects country "{country}" and clicks Register Component button'))
def selectCountry_Register(register_common_component_page,country:str):
    register_common_component_page.choose_country(country)
    register_common_component_page.click_register_btn()

@then(parsers.cfparse('I select "{component_type}" component type'))
def select_component_type(register_common_component_page,component_type:str):
    register_common_component_page.select_component_type_page(component_type)

@then (parsers.cfparse('I can see "{component_type}" register form'))
def see_component_type_detail(register_common_component_page,component_type:str):
    register_common_component_page.see_component_type_detail(component_type)

@when(parsers.parse('I input all information fields include {display_order} and input {link} and {upload_locator_PC} and {filepath_PC} and {upload_locator_mobile} and {filepath_mobile} for image type'))
def input_all_fields(register_hero_banner_component_page,commonFunctions_page,display_order:str,link:str,upload_locator_PC:str,filepath_PC:str,upload_locator_mobile:str,filepath_mobile:str):
    register_hero_banner_component_page.input_register_hero_banner_field_image(display_order,link)
    commonFunctions_page.upload_image(upload_locator_PC,filepath_PC)
    commonFunctions_page.upload_image(upload_locator_mobile,filepath_mobile)
    register_hero_banner_component_page.component_name_created=register_hero_banner_component_page.component_name
@then('I register new Hero Banner component successful')
def register_banner_component_successful(register_hero_banner_component_page):
    register_hero_banner_component_page.register_banner_button()
    pytest.component_name=register_hero_banner_component_page.component_name
@then('I can see New component in list')
def verify_register_banner_component(commonFunctions_page,register_hero_banner_component_page):
    commonFunctions_page.verify_register_new_component_successful(register_hero_banner_component_page.component_name)
@then('I can see New component in main displayed')
def verify_register_banner_component_displayed(main_displayed_page,register_hero_banner_component_page):
    main_displayed_page.open_main_page()
    main_displayed_page.verify_register_banner_component_displayed(register_hero_banner_component_page.component_name)





