from playwright.sync_api import Playwright,Page
class register_common_mod_component:
    def __init__(self,page:Page):
        self.page=page
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
        self.bubblely_menu.click()
        self.official_homepage.click()
        self.page_component.click()
    def select_county(self,country:str):
        self.select_county.click()
        self.input_country.fill(country)
        self.select_country_details.click()
    def click_register_btn(self):
        self.register_btn.click()
        self.register_component_option.click()