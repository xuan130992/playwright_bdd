import pytest
from playwright.sync_api import Playwright, Page
from pytest_bdd import given, when, then, scenarios, parsers
from tests.pages.partners_page.official_homepage.register_common_component_page import register_common_component
scenarios("../../../features/partners/official_homepage/checking_default_fields.feature")
@pytest.fixture
def register_common_component_page(page:Page,base_url):
    return register_common_component(page,base_url)
@given("I go to Page component management")
def selectOfficialHomepage(register_common_component_page):
    register_common_component_page.select_official_homepage()

@when(parsers.cfparse('I selects country "{country}" and clicks Register Component button'))
def selectCountry_Register(register_common_component_page,country:str):
    register_common_component_page.choose_country(country)
    register_common_component_page.click_register_btn()
@then(parsers.parse('I select "{component_type}" component type'))
def select_component_type(register_common_component_page,component_type:str):
    register_common_component_page.select_component_type_page(component_type)

@then(parsers.cfparse('I verify if the Display Country field is display "{expected_country}"'))
def verify_display_country(register_common_component_page,expected_country:str):
    actual = register_common_component_page.get_selected_country()
    assert actual == expected_country,\
        f"Expected: {expected_country}, Actual: {actual}"
@then(parsers.parse('I verify if the Component Type is "{component_type}"'))
def verify_component_type(register_common_component_page,component_type:str):
    register_common_component_page.see_component_type_detail(component_type)
@then(parsers.parse('I verify if the Component ID has the placeholder "{expected_placeholder}" and disable'))
def verify_placeholder(register_common_component_page,expected_placeholder:str):
    assert register_common_component_page.get_component_id_placeholder()==expected_placeholder,\
        f"Expected: {expected_placeholder}"
    assert register_common_component_page.get_component_id_disable(), \
        f"Expected:Component ID should be disabled "
@then(parsers.parse('I verify if the Title field has the placeholder "{expected_placeholder}" and enable'))
def verify_title(register_common_component_page,expected_placeholder:str):
    assert register_common_component_page.get_title()==expected_placeholder, \
        f"Expected: {expected_placeholder}"
@then(parsers.parse('I verify if the display Status is "{expected_status}"'))
def verify_status(register_common_component_page,expected_status:str):
    actual = register_common_component_page.get_display_status()
    assert actual==expected_status, \
        f"Expected: {expected_status}, Actual: {actual}"
@then(parsers.parse('I verify if the period from and period to is display correct period from and period to'))
def verify_period(register_common_component_page):
    assert register_common_component_page.is_display_period_from()
    assert register_common_component_page.is_display_period_to()
@then(parsers.parse('I verify if Display Order is "{expected_order}"'))
def verify_order(register_common_component_page,expected_order:str):
    assert register_common_component_page.get_display_order()==expected_order, \
        f"Expected: {expected_order}"
@then(parsers.parse('I verify if the Use Component Title Option is {component_tile_option}'))
def verify_options(register_common_component_page,component_tile_option:str):
    assert register_common_component_page.get_component_title_options()==component_tile_option,\
        f"Expected: {component_tile_option}"

@then(parsers.parse('I verify if the default language is "{expected_language}"'))
def verify_default_language(register_common_component_page,expected_language:str):
    actual_language = register_common_component_page.get_default_language_cbx()
    assert actual_language==expected_language, \
        f"Expected: {expected_language}"
