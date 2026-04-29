from datetime import datetime,timedelta

from playwright.sync_api import Playwright,Page

from conftest import base_url
from tests.pages.login_page import login_page
import os
class register_common_component:
    def __init__(self,page:Page,base_url):
        self.page=page
        self.base_url= base_url
        self.iframe=page.frame_locator("iframe[id^='iframe-BLZ']")
        self.bubblely_menu = self.page.locator('//*[@menu-id="Bubblelyz"]')
        self.official_homepage = self.page.locator('//*[@menu-id="BLZ00000001000"]')
        self.official_homepage_sb= self.page.locator('//*[@menu-id="BLZ00000011000"]')
        self.page_component =self.page.locator('//*[@menu-id="BLZ00000011001"]')
        self.page_component_sb= self.page.locator('//*[@menu-id="BLZ00000001004"]')
        self.select_county = self.iframe.locator("//*[@id='country']")
        self.input_country = self.iframe.locator('//*[@class="p-inputtext p-component p-select-filter text-14"]')
        self.select_country_details = self.iframe.locator('//*[contains(text(),"Republic of Korea (used)")]')
        self.register_btn = self.iframe.locator('//*[contains(text(),"Register Component")]')
        self.register_component_option= self.iframe.locator('//*[contains(text(),"Please select the type of component to register.")]')
        self.component_id= self.iframe.locator('//*[@id="component-id"]')
        self.title_input = self.iframe.locator('//*[@id="component-title"]')
        self.display_options = self.iframe.locator('(//*[@name="display_true" and @value="true"])[1]')
        self.display_period_from = self.iframe.locator("input.p-datepicker-input").first
        self.display_period_to = self.iframe.locator("input.p-datepicker-input").nth(1)
        self.display_order = self.iframe.locator('//*[@id="component-displayOrder"]')
       # self.use_component_title_option = self.iframe.locator('//*[@id="component-title"]')
        self.language_text=self.iframe.get_by_text("English", exact =True)
        self.default_language_cbx= self.iframe.get_by_label("Default language")
        self.add_banner_btn = self.iframe.locator('//*[@class="p-button p-component p-button-primary text-14"]')
        self.mod_register_btn= self.iframe.locator('//*[@class="p-button p-component text-14"]')
        self.manual_registration_radio = self.iframe.locator('//*[@value="MANUAL"]')
        self.max_count_display = self.iframe.locator('//*[@id="maximum_display"]')
        self.seemore_checkbox = self.iframe.locator('//*[@id="v-0-0-6"]')
        self.mod_bulk_register_btn= self.iframe.locator('//*[@class="p-button p-component ml-12 text-14"]')
        self.Set_Aggregation_Period_Entire = self.iframe.locator('//*[contains(@value,"ENTIRE")]')

    def get_official_homepage_menu(self):
        if self.official_homepage.count()>0:
            return self.official_homepage
        else:
            return self.official_homepage_sb
    def get_component_menu(self):
        if self.page_component.count()>0:
            return self.page_component
        else:
            return self.page_component_sb

    def select_official_homepage(self):
        print("run khuc nay truoc")
        print(f"cai nay thu{self.base_url}/main")
        self.page.goto(f"{self.base_url}/main")
        self.bubblely_menu.click()
        self.get_official_homepage_menu().click()
        self.get_component_menu().click()
    def choose_country(self,country:str):
        self.select_county.click()
        self.input_country.fill(country)
        self.select_country_details.click()
    def click_register_btn(self):
        self.register_btn.click()
        self.register_component_option.click()
    def select_component_type_page(self,component_type:str):
        component_type_locator= self.iframe.locator(f'//*[@class="py-8 px-24 rounded-br-10 rounded-tl-10 w-auto bg-black color-white inline-block text-18" and text()={component_type}]')
        component_type_locator.click()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(5000)
    def see_component_type_detail(self,component_type:str):
        component_type_detail= self.iframe.locator(f'(//*[contains(text(),"{component_type}")])[1]')
        component_type_detail.is_visible()
    def get_selected_country(self) -> str:
        return self.iframe.locator("span[id^='country-v']").inner_text()
    def get_component_id_placeholder(self) -> str:
        return self.component_id.get_attribute("placeholder")
    def get_component_id_disable(self) -> str:
        return self.component_id.is_disabled()
    def get_title(self) -> str:
       return self.title_input.get_attribute("placeholder")
    def get_display_status(self) -> str:
        all_radios = self.iframe.locator('//*[@name ="display_true"]')
        count = all_radios.count()
        print(f"Total radios: {count}")
        for i in range(count):
            radio = all_radios.nth(i)
            print(f"Radio [{i}]: checked={radio.is_checked()}, value={radio.get_attribute('value')}")
        is_checked = self.display_options.is_checked()
        print(f"Display radio is_checked: {is_checked}")
        if is_checked:
            return "Display"
        return "Do Not Display"
    def is_display_period_from(self)-> bool:
        expected = datetime.now().strftime("%Y.%m.%d %H:%M")
        print(f"expected: {expected}")
        print(f"actual: {self.display_period_from.get_attribute('value')}")

        return self.display_period_from.get_attribute("value")==expected
    def is_display_period_to(self)-> bool:
        expected= (datetime.now() + timedelta(days=90)).strftime("%Y.%m.%d %H:%M")
        return self.display_period_to.get_attribute("value")==expected
    def get_display_order(self)->str:
        return self.display_order.get_attribute("value")
    def get_component_title_options(self)->str:
        if self.iframe.get_by_role("radio", name="Do Not Use").is_checked():
            return "Do Not Use"
        return "Use"
    def get_default_language_cbx(self)-> bool:
        if self.default_language_cbx.is_checked() and self.language_text.inner_text()=="English":
            return "English"
        return "other language"

    def get_field_locator(self, field: str):

        field_map = {
            "Add Banner": self.add_banner_btn,
            "Mod Register": self.mod_register_btn,
            "Mod Bulk Register": self.mod_bulk_register_btn,
            "Manual Registration": self.manual_registration_radio,
            "Maximum Display Count": self.max_count_display,
            "Entire": self.Set_Aggregation_Period_Entire,
        }
        return field_map.get(field)





