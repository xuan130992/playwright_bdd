from playwright.sync_api import Page
from conftest import base_url
class navigate_mod_management:
    def __init__(self,page:Page,base_url):
        self.page = page
        self.base_url = self.page.url
        self.iframe = page.frame_locator("#iframe-BLZ00000001004")
        self.bubblely_menu = self.page.locator('//*[contains(text(),"Bubblelyz")]')
        self.ugc_management = self.page.locator('//*[contains(text(),"Official Homepage Management")]')
        self.mod_management = self.page.locator('//*[contains(text(), "Page Component Management")]')
        self.registration_btn= self.page.locator('//*[contains(text(),"Button Registration")]')
    def navigate_mod_management(self):
        self.page.goto(f"{self.base_url}/main")
        self.bubblely_menu.click()
        self.ugc_management.click()
        self.mod_management.click()

    def click_registration_button(self):
        self.registration_btn.click()

