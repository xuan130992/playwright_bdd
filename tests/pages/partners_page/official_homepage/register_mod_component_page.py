from playwright.sync_api import Playwright,Page
class register_feature_mod_component:
    def __init__(self,page:Page):
        self.page =page
        self.iframe = page.frame_locator("#iframe-BLZ00000001004")
        self.title_input= self.iframe.locator()
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


