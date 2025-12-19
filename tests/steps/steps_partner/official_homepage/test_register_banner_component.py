import pytest
from playwright.sync_api import Playwright,Page
from allure_commons import fixture
from pytest_bdd import given, when, then, scenarios, parsers
from tests.pages.partners_page.official_homepage.register_banner_component_page import register_baner_component
from tests.pages.partners_page.official_homepage.register_common_component_page import register_common_component
scenarios("../../../features/partners/official_homepage/register_banner_component.feature")
@pytest.fixture
def register_common_component_page(page:Page):
    return register_common_component(page)
@pytest.fixture
def registe_banner_component_page(page: Page):
    return register_common_component(page)
@given("User goes to Page component management")
def selectOfficialHomepage(register_common_component_page):

    register_common_component_page.select_official_homepage()

@when(parsers.cfparse('User selects country "{country}" and clicks Register Component button'))
def selectCountry_Register(register_common_component_page,country:str):
    register_common_component_page.choose_country(country)
    register_common_component_page.click_register_btn()

@then(parsers.cfparse('I select "{component_type}" component type'))
def select_component_type(register_common_component_page,component_type:str):
    register_common_component_page.select_component_type_page(component_type)

@then (parsers.cfparse('I can see "{component_type}" register form'))
def see_component_type_detail(register_common_component_page,component_type:str):
    register_common_component_page.see_component_type_detail(component_type)

@when(parsers.parse('I input all information fields include "{display_order}" and input "{link}"'))
def input_all_fields(register_common_component_page,display_order:str,link:str):
    register_common_component_page.input_all_fields(display_order,link)


