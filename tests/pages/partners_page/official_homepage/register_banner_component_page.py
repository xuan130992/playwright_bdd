from playwright.sync_api import Playwright,Page
import uuid
class register_baner_component:
    def __init__(self,page:Page):
        self.page = page
        self.iframe = page.frame_locator("#iframe-BLZ00000001004")
        self.random_suffix = uuid.uuid4().hex[:6]
        self.title_input=self.iframe.locator()
        self.display_options=self.iframe.locator()
        self.display_period= self.iframe.locator()
        self.display_order= self.iframe.locator()
        self.banner_btn= self.iframe.locator()
        self.banner_type= self.iframe.locator()
        self.main_title_input=self.iframe.locator()
        self.sub_title_input=self.iframe.locator()
        self.upload_button_PC= self.iframe.locator()
        self.upload_button_mobile= self.iframe.locator()
        self.link= self.iframe.locator()
        self.register_btn= self.iframe.locator()
        self.register_complete_btn= self.iframe.locator()
        self.component_name = f'banner_component_{self.random_suffix}'

    def register_banner_component(self,link_value):
        self.title_input.fill(self.component_name)
        self.display_options.check()
        self.display_order.fill("0")
        self.banner_btn.click()
        self.main_title_input.fill(f'banner_component_{self.random_suffix}')
        self.link_input.fill(link_value)

