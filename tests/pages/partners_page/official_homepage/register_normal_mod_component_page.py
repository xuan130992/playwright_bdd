import uuid
from playwright.sync_api import Playwright,Page
class register_normal_mod_component:
    def __init__(self,page:Page):
        self.page =page
        self.iframe = page.frame_locator("#iframe-BLZ00000001004")
        self.resource_methods_manual=self.iframe.locator('//*[@value="MANUAL"]')
        self.resource_methods_auto=self.iframe.locator('//*[@value="AUTOMATIC"]')
        self.auto_mod_selection=self.iframe.locator('//*[@id="v-0-0-10"]')
        self.auto_Sorting_method=self.iframe.locator('//*[@id="v-0-0-16"]')
        self.maxcount_display=self.iframe.locator('//*[@id="maximum_display"]')
        self.maxcount_display_select= self.iframe.locator('//*[@id="pv_id_0_0_4_1"]')
        self.seemore_checkbox=self.iframe.locator('//*[@id="v-0-0-6"]')
    def select_manual_registration(self):
        self.resource_methods_manual.click()
        self.maxcount_display.click()
        self.maxcount_display_select.click()
        self.seemore_checkbox.click()
    def select_auto_registration(self):
        self.resource_methods_auto.click()
        self.auto_mod_selection.click()
        self.maxcount_display.click()
        self.maxcount_display_select.click()
        self.seemore_checkbox.click()
        self.auto_Sorting_method.click()