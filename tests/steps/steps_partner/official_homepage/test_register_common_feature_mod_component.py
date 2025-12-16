import pytest
from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import sync_playwright
from pytest_bdd.types import GIVEN
from pytest_bdd import parsers

from tests.pages.partners_page.official_homepage.register_common_component_page import register_common_component
scenarios("../../../features/partners/official_homepage/register_feature_mod_component.feature")
@pytest.fixture
def register_common_component_page(page,base_url):
    return register_common_component(page,base_url)
@given("User goes to Page component management")
def selectOfficialHomepage(register_common_component_page):

    register_common_component_page.select_official_homepage()

@when(parsers.cfparse('User selects country "{country}" and clicks Register Component button'))
def selectCountry_Register(register_common_component_page,country:str):
    register_common_component_page.choose_country(country)
    register_common_component_page.click_register_btn()

@then(parsers.cfparse('I select "{component_type}" mod type'))
def select_component_type(register_common_component_page,component_type:str):
    register_common_component_page.select_component_type_page(component_type)

@then ('I can see "Feature Mod" register form')
def see_component_type_detail(register_common_component_page):
    register_common_component_page.see_component_type_detail()

