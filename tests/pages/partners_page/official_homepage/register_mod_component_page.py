import uuid
from playwright.sync_api import Playwright,Page
class register_feature_mod_component:
    def __init__(self,page:Page):
        self.page =page
        self.iframe = page.frame_locator("#iframe-BLZ00000001004")
        self.component_type= self.page.iframe.locator('//*[contains(text(),"Featured MOD")]')
        self.random_suffix = uuid.uuid4().hex[:6]
        self.title_input= self.iframe.locator('//*[@id="component-title"]')
        self.display_options= self.iframe.locator()
        self.display_period= self.iframe.locator()
        self.display_order= self.iframe.locator()
        self.use_title_options=self.iframe.locator()
        self.en_language_component_title= self.iframe.locator()
        self.set_aggregation_period= self.iframe.locator()
        self.mod_register_btn= self.iframe.locator()
        self.mod_type_btn= self.iframe.locator()
        self.over_lay= self.iframe.locator()
        self.mod_type_select=self.iframe.locator()
        self.search_mod_btn= self.iframe.locator()
        self.mod_checkbox= self.iframe.locator()
        self.registe_mod_btn=self.iframe.locator()
        self.register_scs_confirm= self.iframe.locator()
        self.register_btn= self.iframe.locator()
        self.register_complete_btn= self.iframe.locator()




    def input_register_field(self):
        self.title_input.fill(f'feature mod component_{self.random_suffix}')
        self.display_options.click()
        self.display_order.fill("0")
        self.use_title_options.click()
        self.en_language_component_title.fill(f'EN_feature mod component_{self.random_suffix}')
    def select_mod(self):
        self.mod_register_btn.click()
        self.mod_type_select.click()
        self.search_mod_btn.click()
        self.mod_checkbox.click()

    def register_mod_components(self):
        self.registe_mod_btn.click()
        self.register_scs_confirm.click()
        self.register_btn.click()
        self.register_complete_btn.click()



