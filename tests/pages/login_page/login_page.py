from playwright.sync_api import Page, sync_playwright
import os


class LoginPage:
    def __init__(self,page:Page,base_url:str):
        self.page = page
        self.base_url=base_url
        self.login1_btn = self.page.locator('(//*[@class="login"])[3]')
        self.username_input = self.page.locator('//input[@id="user_id"]')
        self.password_input = self.page.locator("//input[@id='user_pwd']")
        self.login2_btn = self.page.locator("//*[@id='btn-login']")
        self.partner_logo=self.page.locator("//*[@id='logo']")

    def open_login_page(self,base_url):
        self.page.goto(base_url)
        self.login1_btn.click()

    def input_username(self,username):
        self.username_input.fill(username)
    def input_password(self,password):
        self.password_input.fill(password)
    def login_btn(self):
        self.login2_btn.click()
    def is_partner_displayed(self):
        print("cho partner")
        return self.partner_logo.is_visible()


    def save_login_state(self):
        self.page.wait_for_selector('text=Partners')
        print("da thay partners")
        os.makedirs("auth", exist_ok = True)
        self.page.context.storage_state(path="./tests/auth/storage_state.json")
