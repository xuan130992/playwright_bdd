import uuid
from playwright.sync_api import Playwright,Page
class register_mod_component:
    def __init__(self,page:Page):
        self.page =page
        self.iframe = page.frame_locator("#iframe-BLZ00000001004")
        self.component_type= self.iframe.locator('//*[contains(text(),"Featured MOD")]')
        self.random_suffix = uuid.uuid4().hex[:6]
        self.title_input= self.iframe.locator('//*[@id="component-title"]')
        self.display_options= self.iframe.locator('(//*[@name="display_true"])[1]')
        self.display_period= self.iframe.locator('//*[@id="component-display-period"]')
        self.display_order= self.iframe.locator('//*[@id="component-displayOrder"]')
        self.use_title_options=self.iframe.locator('(//*[@name="display_true"])[2]')
        self.en_language_component_title= self.iframe.locator('//*[@id="component-title-en"]')
        self.set_aggregation_period= self.iframe.locator('//*[contains(text(),"Entire")]')
        self.mod_register_btn= self.iframe.locator('//*[@class="p-button p-component text-14"]')
        self.mod_type_btn= self.iframe.locator('//*[@id="modType"]')
        self.over_lay= self.iframe.locator('//*[@class="p-select-overlay p-component"]')
        self.mod_type_select=self.iframe.locator('//span[text()="Official MOD"]')
        self.search_mod_btn= self.iframe.locator('//*[@class="p-button-icon i-mdi:magnify text-20"]')
        self.mod_checkbox= self.iframe.locator('(//*[@class="p-checkbox-input"])[3]')
        self.registe_mod_btn=self.iframe.locator('(//*[@class="p-button p-component text-14"])[2]')
        self.register_scs_confirm= self.iframe.locator('//*[contains(text(),"Confirm") and @class="p-button-label"]')
        self.register_btn= self.iframe.locator('//*[contains(text(),"Register") and @class="p-button-label"]')
        self.register_complete_btn= self.iframe.locator('//*[contains(text(),"Confirm") and @class="p-button-label"]')
        self.component_name = f'feature mod component_{self.random_suffix}'






    def input_register_field(self):
        self.title_input.fill(self.component_name)
        self.display_options.click()
        self.display_order.fill("0")
        self.use_title_options.click()
        self.en_language_component_title.fill(f'EN_feature mod component_{self.random_suffix}')
    def select_mod(self):
        self.mod_register_btn.click()
        self.mod_type_btn.click()
        self.mod_type_select.click()
        self.search_mod_btn.click()
        self.mod_checkbox.click()

    def register_mod_components(self):
        self.registe_mod_btn.click()
        self.register_scs_confirm.click()
        self.register_btn.click()
        self.register_complete_btn.click()

    def verify_register_component_successful(self,component_name):
        new_component = self.iframe.locator(f'xpath=(//*[contains(text(),"{component_name}")])[1]')
        new_component.is_visible()



