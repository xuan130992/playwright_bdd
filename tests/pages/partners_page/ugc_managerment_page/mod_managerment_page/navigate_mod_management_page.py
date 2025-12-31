from playwright.sync_api import Page
from conftest import base_url
import os
class navigate_mod_managementPage:
    def __init__(self,page:Page,base_url):
        self.page = page
        self.base_url = base_url
        self.iframe = page.frame_locator("#iframe-BLZ00000001004")
        self.bubblely_menu = self.page.locator('//*[contains(text(),"Bubblelyz")]')
        self.ugc_management = self.page.locator('//*[contains(text(),"UGC Management")]')
        self.mod_management = self.page.locator('(//*[contains(text(),"MOD Management")])[2]')
        self.registration_btn= self.page.locator('//*[contains(text(),"Registration") and @class="p-button-label"]')
    def navigate_mod_management(self):

        print("run khuc nay truoc")
        print(f"cai nay thu{self.base_url}/main")
        self.page.goto(f"{self.base_url}/main")
        self.bubblely_menu.click()
        self.ugc_management.click()
        self.mod_management.click()

    def click_registration_button(self):
        self.registration_btn.click()

