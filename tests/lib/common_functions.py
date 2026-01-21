from playwright.sync_api import Page,expect, ElementHandle
import uuid
class commonFunctions():
    def __init__(self,page: Page,component_name=None, mod_name=None):
        self.page = page
        self.component_name = component_name
        self.mod_name = mod_name
        self.iframe = page.frame_locator("#iframe-BLZ00000001004")
        self.iframe_mod=page.frame_locator("#iframe-BLZ00000005001")
        self.iframe_genre=page.frame_locator("#iframe-BLZ00000005003")

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
    # def upload_image_genre(self,iframe1,upload_locator:str, filepath:str):
    #     print("bat dau upload genre")
    #     with self.page.expect_file_chooser() as fc_info:
    #          iframe1.locator(upload_locator).click()
    #          file_chooser=  fc_info.value
    #          file_chooser.set_files(filepath)
    def upload_image_root(self, upload_locator: str, filepath: str):
        print(f"📤 Bắt đầu upload ảnh '{upload_locator}' với file: {filepath}")


        # Duyệt qua tất cả iframe để tìm locator này
        for frame in self.page.frames:
            print("Frame URL:", frame.url)
            try:
                locator = frame.locator(upload_locator)
                if locator.count() > 0:
                    print(f"✅ Tìm thấy locator trong iframe: {frame.url}")
                    with self.page.expect_file_chooser() as fc_info:
                        locator.click()
                        fc_info.value.set_files(filepath)
                    print("✅ Upload thành công!")
                    return
            except Exception as e:
                print(f"⚠️ Lỗi khi kiểm tra iframe: {e}")
                continue

        raise Exception(f"❌ Không tìm thấy element '{upload_locator}' va {frame} trong bất kỳ iframe nào!")

    def verify_register_new_component_successful(self, component_name):
        new_component = self.iframe.locator(f'xpath=(//*[contains(text(),"{component_name}")])[1]')
        new_component.is_visible()
    def verify_register_new_mod_successful(self, mod_name):
        new_mod=self.iframe_mod.locator(f'xpath=(//*[contains(text(),"{mod_name}")])[1]')
        expect(new_mod).to_be_visible()
    def verify_register_new_genre_successful(self, genre_name):
        new_genre=self.iframe_genre.locator(f'xpath=(//*[contains(text(),"{genre_name}")])[1]')
        expect(new_genre).to_be_visible()






