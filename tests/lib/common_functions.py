from playwright.sync_api import Page,expect, ElementHandle
import uuid
class commonFunctions():
    def __init__(self,page: Page,component_name=None, mod_name=None):
        self.page = page
        self.component_name = component_name
        self.mod_name = mod_name
        self.iframe = page.frame_locator("#iframe-BLZ00000001004")
        self.iframe_mod=page.frame_locator("#iframe-BLZ00000005001")

    def upload_image(self, upload_locator:str, filepath:str):
        print("bat dau upload.")
        with self.page.expect_file_chooser() as fc_info:
             self.iframe.locator(upload_locator).click()
             file_chooser=  fc_info.value
             file_chooser.set_files(filepath)
    def upload_image_mod(self, upload_locator:str, filepath:str):
        print("bat dau upload.")
        with self.page.expect_file_chooser() as fc_info:
             self.iframe_mod.locator(upload_locator).click()
             file_chooser=  fc_info.value
             file_chooser.set_files(filepath)

    def verify_register_new_component_successful(self, component_name):
        new_component = self.iframe.locator(f'xpath=(//*[contains(text(),"{component_name}")])[1]')
        new_component.is_visible()
    def verify_register_new_mod_successful(self, mod_name):
        new_mod=self.iframe.locator(f'xpath=(//*[contains(text(),"{mod_name}")])[1]')
        new_mod.is_visible()





