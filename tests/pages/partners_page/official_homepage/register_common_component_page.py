from playwright.sync_api import Playwright,Page

from conftest import base_url
from tests.pages.login_page import login_page
import os
class register_common_component:
    def __init__(self,page:Page,base_url):
        self.page=page
        self.base_url= base_url
        self.iframe=page.frame_locator("#iframe-BLZ00000001004")
        self.bubblely_menu = self.page.locator('//*[contains(text(),"Bubblelyz")]')
        self.official_homepage = self.page.locator('//*[contains(text(),"Official Homepage Management")]')
        self.page_component =self.page.locator('//*[contains(text(), "Page Component Management")]')
        self.select_county = self.iframe.locator("//*[@id='country']")
        self.input_country = self.iframe.locator('//*[@class="p-inputtext p-component p-select-filter text-14"]')
        self.select_country_details = self.iframe.locator('//*[contains(text(),"Republic of Korea (used)")]')
        self.register_btn = self.iframe.locator('//*[contains(text(),"Register Component")]')
        self.register_component_option= self.iframe.locator('//*[contains(text(),"Please select the type of component to register.")]')

    def select_official_homepage(self):
        print("run khuc nay truoc")
        print(f"cai nay thu{self.base_url}/main")
        self.page.goto(f"{self.base_url}/main")

        self.bubblely_menu.click()
        self.official_homepage.click()
        self.page_component.click()
    def choose_country(self,country:str):
        self.select_county.click()
        self.input_country.fill(country)
        self.select_country_details.click()
    def click_register_btn(self):
        self.register_btn.click()
        self.register_component_option.click()
    def select_component_type_page(self,component_type:str):
        component_type_locator= self.iframe.locator(f'//*[@class="py-8 px-24 rounded-br-10 rounded-tl-10 w-auto bg-black color-white inline-block text-18" and text()="{component_type}"]')
        component_type_locator.click()
    def see_component_type_detail(self,component_type:str):
        component_type_detail= self.iframe.locator(f'(//*[contains(text(),"{component_type}")])[1]')
        component_type_detail.is_visible()


