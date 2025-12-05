import pytest
from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import sync_playwright
from pytest_bdd.types import GIVEN

from tests.pages.partners_page.official_homepage.register_common_mod_component_page import register_common_mod_component
scenarios("../../../features/partners/official_homepage/register_common_mod_component.feature")
@pytest.fixture
def register_common_mod_component_page(page,base_url):
    return register_common_mod_component(page,base_url)
@given("User goes to Page component management")
def selectOfficialHomepage(register_common_mod_component_page):

    register_common_mod_component_page.select_official_homepage()

@then("User selects country and clicks Register Component button")
def selectCountry_Register(register_common_mod_component_page,country:str,page):
    register_common_mod_component_page.choose_country(country)
    register_common_mod_component_page.click_register_btn()

