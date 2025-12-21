import pytest
from playwright.sync_api import Playwright,Page
from allure_commons import fixture
from pytest_bdd import given, when, then, scenarios, parsers
from tests.pages.partners_page.official_homepage.register_banner_component_page import register_banner_component
from tests.pages.partners_page.official_homepage.register_common_component_page import register_common_component
from tests.lib.common_functions import commonFunctions
scenarios("../../../features/partners/official_homepage/register_banner_component.feature")
@pytest.fixture
def register_common_component_page(page:Page,base_url):
    return register_common_component(page,base_url)
@pytest.fixture
def register_banner_component_page(page: Page):
    return register_banner_component(page)
def commonFunctions_page(page:Page):
    return commonFunctions(page)

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

@when(parsers.parse('I input all information fields include "{display_order}" and input "{link}" and"{filepath}"'))
def input_all_fields(register_banner_component_page,display_order:str,link:str,filepath:str):
    register_banner_component_page.input_register_banner_field(display_order,link)
def upload_file(commonFunctions_page,upload_locator:str,filepath:str):
    commonFunctions_page.upload_image(upload_locator,filepath)
@then('I register new Banner component successful')
def register_banner_component_successful(register_banner_component_page):
    register_banner_component_page.register_banner_button()
@then('I can see New component in list')
def verify_register_banner_component(register_banner_component_page):
    register_banner_component_page.verify_register_banner_component_successful()





