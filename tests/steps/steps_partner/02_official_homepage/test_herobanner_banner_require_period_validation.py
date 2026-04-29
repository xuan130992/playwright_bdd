import pytest
from allure_commons import fixture
from playwright.sync_api import Page, Playwright
from pytest_bdd import given, when, then, scenarios, parsers, scenario
from tests.locators.Partner.official_homepage.common_locators import component_common_locators
from tests.pages.partners_page.official_homepage.register_common_component_page import register_common_component
from tests.locators.Partner.official_homepage.Herobanner_banner_locators import component_hero_banner_locators
from tests.helper.field_assertions import assert_locator_visible
@scenario("../../../features/partners/official_homepage/checking_herobanner_banner_validation.feature","Verify Title field is required for <component_type>" )
def test_create_hero_banner_validation():
    pass
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
def filed_assertions_page():
    return assert_locator_visible
# ===============Background steps==============
@given("I go to Page component management")
def selectOfficialHomepage(register_common_component_page):
    register_common_component_page.select_official_homepage()
@given(parsers.cfparse('I selects country "{country}" and clicks Register Component button'))
def selectCountry_Register(register_common_component_page,country:str):
    register_common_component_page.choose_country(country)
    register_common_component_page.click_register_btn()
#================scenario steps=============
@given(parsers.cfparse('I select {component_type} component type'))
def selectComponent(register_common_component_page,component_type):
    register_common_component_page.select_component_type_page(component_type)
