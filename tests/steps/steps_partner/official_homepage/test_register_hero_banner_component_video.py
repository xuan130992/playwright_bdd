import pytest
import os
from playwright.sync_api import Playwright, Page
from pytest_bdd import given, when, then, parsers, scenarios, scenario
from tests.pages.partners_page.official_homepage.register_hero_banner_component_page import register_hero_banner_component
from tests.lib.common_functions import commonFunctions
from tests.pages.official_website.main_display_page import main_display_page
from tests.pages.partners_page.official_homepage.register_common_component_page import register_common_component

@scenario("../../../features/partners/official_homepage/register_hero_banner_component.feature","I create a Hero banner with video type")

def test_create_hero_banner_with_video_type():
    pass
@pytest.fixture
def register_common_component_page(page:Page,base_url):
    return register_common_component(page,base_url)
@pytest.fixture
def main_displayed_page(page:Page,main_display_url):
    return main_display_page(page,main_display_url)
@pytest.fixture
def commonFunctions_page(page:Page):
    return commonFunctions(page)
@pytest.fixture()
def register_hero_banner_component_page(page:Page,):
    return register_hero_banner_component(page)
@given('I go to Page component management video')
def selectofficialHomepage(register_common_component_page):
    register_common_component_page.select_official_homepage()
@when(parsers.cfparse('I selects country "{country}" and clicks Register Component button video'))
def selectCountry_Register(register_common_component_page,country:str):
    register_common_component_page.choose_country(country)
    register_common_component_page.click_register_btn()
@then(parsers.cfparse('I select "{component_type}" component type video'))
def selectComponent(register_common_component_page,component_type:str):
    register_common_component_page.select_component_type_page(component_type)
@then(parsers.cfparse('I can see "{component_type}" register form video'))
def seeComponentType(register_common_component_page,component_type:str):
    register_common_component_page.see_component_type_detail(component_type)
@then(parsers.cfparse('I input all information fields include {display_order} video'))
def input_common_hero_banner_fields(register_hero_banner_component_page,display_order:str):
    register_hero_banner_component_page.input_common_hero_banner_fields(display_order)
@then(parsers.cfparse('I input information fields for video type include {link} and {background_color_selected} and {video_url} video'))
def input_hero_banner_video(register_hero_banner_component_page,background_color_selected:str,link:str,video_url:str):
    register_hero_banner_component_page.input_hero_banner_video(background_color_selected,link,video_url)
@then(parsers.cfparse('I upload thumbnail image {upload_locator_PC} and {filepath_PC} for video type video'))
def uploadThumbnail(commonFunctions_page,upload_locator_PC:str,filepath_PC:str):
    commonFunctions_page.upload_image_root(upload_locator_PC,filepath_PC)
@then('I register new Hero Banner component successful video')
def registerHeroBannersuccessful(register_hero_banner_component_page):
    register_hero_banner_component_page.register_banner_button()
    pytest.component_name= register_hero_banner_component_page.component_name
@then('I can see New component in list video')
def see_new_component(commonFunctions_page,register_hero_banner_component_page):
    commonFunctions_page.verify_register_new_component_successful(register_hero_banner_component_page.component_name)
@then('I can see New component in main displayed video')
def displayNewComponent(main_displayed_page,register_hero_banner_component_page):
    main_displayed_page.open_main_page()
    main_displayed_page.verify_register_banner_component_displayed(register_hero_banner_component_page.component_name)
