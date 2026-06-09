import pytest
from playwright.sync_api import Page
from pytest_bdd import scenarios, when, parsers, then, given, scenario
from tests.pages.partners_page.official_homepage.register_common_component_page import register_common_component
from tests.helper.field_assertions import assert_field
scenarios("../../../features/partners/official_homepage/checking_default_fields.feature")
# def test_create_hero_banner_with_other_fields():
#     pass
@pytest.fixture
def register_common_component_page(page:Page,base_url):
    return register_common_component(page,base_url)
@given("I go to Page component management")
def selectOfficialHomepage(register_common_component_page):
    register_common_component_page.select_official_homepage()

@when(parsers.parse('I selects country "{country}" and clicks Register Component button'))
def selectCountry_Register(register_common_component_page,country:str):
    register_common_component_page.choose_country(country)
    register_common_component_page.click_register_btn()
@then(parsers.parse('I select "{component_type}" component type'))
def select_component_type(register_common_component_page,component_type:str):
    register_common_component_page.select_component_type_page(component_type)
@then(parsers.parse('the field "{field}" should be "{visibility}" with default "{defaultValue}"'))
def assert_field_default(field: str, visibility: str, defaultValue: str, register_common_component_page):
    assert_field(register_common_component_page, field, visibility, defaultValue)