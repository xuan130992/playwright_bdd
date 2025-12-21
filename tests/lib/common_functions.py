from playwright.sync_api import Page,expect, ElementHandle
import uuid
class commonFunctions():
    def __init__(self,page: Page):
        self.page = page
        self.iframe = page.frame_locator("#iframe-BLZ00000001004")
    def upload_image(self, upload_locator:str, filepath:str):
        print("Upload thành công.")
        with self.page.expect_file_chooser() as fc_info:
             self.iframe.locator(upload_locator).click()
             file_chooser=  fc_info.value
             file_chooser.set_files(filepath)






