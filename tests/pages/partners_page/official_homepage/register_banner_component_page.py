from playwright.sync_api import Playwright,Page
import uuid
class register_banner_component:
    def __init__(self,page:Page):
        self.page = page
        self.iframe = page.frame_locator("#iframe-BLZ00000001004")
        self.random_suffix = uuid.uuid4().hex[:6]
        self.title_input=self.iframe.locator('//*[@id="component-title"]')
        self.display_options=self.iframe.locator('(//*[@name="display_true"])[1]')
        self.display_period= self.iframe.locator('//*[@id="component-display-period"]')
        self.display_order= self.iframe.locator('//*[@id="component-displayOrder"]')
        self.banner_btn= self.iframe.locator('//*[@class="p-button p-component p-button-primary text-14"]')
        self.banner_type= self.iframe.locator('//*[contains(text(),"Image Type")]')
        self.main_title_input=self.iframe.locator('//*[@id="mainTitle-en-0"]')
        self.sub_title_input=self.iframe.locator('//*[@id="subTitle-en-0"]')
        self.upload_button_PC= self.iframe.locator('(//*[contains(text(),"Upload")])[1]')
        self.upload_button_mobile= self.iframe.locator('(//*[contains(text(),"Upload")])[2]')
        self.link= self.iframe.locator('//*[@id="link"]')
        self.link_input= self.iframe.locator('//*[@class="p-inputtext p-component w-350 text-14"]')
        self.register_btn= self.iframe.locator('//*[contains(text(),"Register") and @class="p-button-label"]')
        self.register_complete_btn= self.iframe.locator('//*[contains(text(),"Confirm") and @class="p-button-label"]')
        self.component_name = f'banner_component_{self.random_suffix}'

    def input_register_banner_field(self,display_order,link_value):
        self.title_input.fill(self.component_name)
        self.display_options.check()
        self.display_order.fill(display_order)
        self.banner_btn.click()
        self.main_title_input.fill(f'banner_component_{self.random_suffix}')
        self.link.click()
        self.link_input.fill(link_value)
    def register_banner_button(self):
        self.register_btn.click()
        self.register_complete_btn.click()
    def verify_register_banner_component_successful(self,component_name):
        new_component= self.iframe.locator(f'xpath=(//*[contains(text(),"{component_name}")])[1]')
        new_component.is_visible()
