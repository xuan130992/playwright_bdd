import pytest
from pytest_bdd import when, then, parsers, given, scenarios
from playwright.sync_api import playwright,Page
from tests.pages.partners_page.ugc_managerment_page.ugc_genre_management_page.ugc_genre_management_page import ugc_genre_managementPage
from tests.pages.partners_page.ugc_managerment_page.ugc_genre_management_page.genre_register_page import RegisterPage
from tests.lib.common_functions import commonFunctions
scenarios("../../../../features/partners/ugc_management/UGC_Genre/register_ugc_genre.feature")
@pytest.fixture
def commonFunctions_page(page:Page):
    return commonFunctions(page)
@pytest.fixture
def genre_register_Page(page:Page):
    return RegisterPage(page)
@pytest.fixture
def ugc_genre_management_Page(page:Page,base_url:str):
    return ugc_genre_managementPage(page,base_url)
@given('I navigate to ugc gere management')
def navigate_ugc_genre_management(ugc_genre_management_Page):
    ugc_genre_management_Page.navigate_genre_management()
@then('I click register1 button')
def click_register_button(ugc_genre_management_Page):
    ugc_genre_management_Page.click_register1_btn()
@then(parsers.parse('I input genre information with {usage_status}'))
def input_genre_info(genre_register_Page,usage_status:str):
    genre_register_Page.register_genre(usage_status)
    genre_register_Page.genre_name_created=genre_register_Page.genre_name
@then(parsers.parse('I upload with {genre_image} and {filepath_genre_image}'))
def upload_genre_image(commonFunctions_page,genre_image:str,filepath_genre_image:str):
    print("debug",genre_image)
    commonFunctions_page.upload_image_root(genre_image,filepath_genre_image)
@then('I click register2 button')
def click_register_button(genre_register_Page):
    genre_register_Page.click_register2_btn()
@then('I see a new genre was created')
def verify_new_genre(commonFunctions_page,genre_register_Page):
    commonFunctions_page. verify_register_new_genre_successful(genre_register_Page.genre_name)