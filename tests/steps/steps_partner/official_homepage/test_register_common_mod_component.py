import pytest
from pytest_bdd import given, when, then, scenarios
from playwright.async_api import async_playwright,Page
from pytest_bdd.types import GIVEN

from tests.pages.partners_page.official_homepage.register_common_mod_component import register_common_mod_component
scenarios("../../features/partners/official_homepage/official_homepage.feature")

@pytest.fixture(scope="module")



@given("User goes to Page component management")
def selectOfficialHomepage(page:Page):
    register_common_mod_component.select_official_homepage()

@then("User selects country and clicks Register Component button")
def selectCountry_Register(page:Page,country:str):
    register_common_mod_component.select_county(country)
    register_common_mod_component.click_register_btn()

