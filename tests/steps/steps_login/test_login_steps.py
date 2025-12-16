import pytest
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import Page
from playwright.async_api import expect
from tests.pages.login_page.login_page import LoginPage

scenarios('../../features/login/login.feature')
@pytest.fixture()
def login_page(page:Page,base_url):
    return LoginPage(page,base_url)

@given("I am on the login page")
def go_to_login_page(login_page):
    print(f"base_url={login_page.base_url}")
    login_page.open_login_page(login_page.base_url)



@when("I enter username and password")
def I_enter_username_and_password(login_page, username, password):
    login_page.input_username(username)
    login_page.input_password(password)


@when("I click the login button")
def I_click_the_login_button(login_page):
    login_page.login_btn()


@then("I should see the partner page")
def I_should_see_partner_page(login_page):
    print("cho partner cho nay  ")
   # assert login_page.is_partner_displayed()

@then("I should see the storage state")
def I_should_see_storage_state(login_page):
    login_page.save_login_state()



