import self
from playwright.sync_api import Playwright,Page
import uuid
class mod_register:
    def __init__(self,page:Page, base_url):
        self.page = page()
        self.base_url= base_url
        self.iframe = page.frame_locator("#iframe-BLZ00000001004")
        self.random_suffix = uuid.uuid4().hex[:6]
        self.mod_type=self.iframe.locator('//*[@aria-label="Select Type"]')
        self.mod_type_selected= self.iframe.locator('//*[@aria-label="Official MOD"]')
        self.package_version= self.iframe.locator('//*[@id="version_id-v-0-228"]')
        self.visibility= self.iframe.locator('//*[@value="PRIVATE"]')
        self.set_country= self.iframe.locator()
        self.select_country= self.iframe.locator()
        self.register_country_btn= self.iframe.locator()
        self.ingame_display_order=self.iframe.locator()
        self.english_title= self.iframe.locator()
        self.english_oneline_description= self.iframe.locator()
        self.english_description= self.iframe.locator()
        self.genre_settings=self.iframe.locator()
        self.genre_selected= self.iframe.locator()
        self.add_screenshot= self.iframe.locator()
        self.upload_screenshot=self.iframe.locator()
        self.max_participants= self.iframe.locator()
        self.min_participants= self.iframe.locator()
        self.start_participants= self.iframe.locator()
        self.reduction_time= self.iframe.locator()
        self.addition_recruitment_time= self.iframe.locator()
        self.android_file_upload=self.iframe.locator()
        self.ios_file_upload= self.iframe.locator()
        self.windowns_file_upload= self.iframe.locator()
        self.server_file_upload= self.iframe.locator()
        self.register_btn= self.iframe.locator()
        self.confirm_btn= self.iframe.locator()
        self.mod_name= f'mod_name_{self.random_suffix}'

    def register_official_mod(self,package_version,ingame_display_order,eng_oneline_description,eng_description):
        self.mod_type.click()
        self.mod_type_selected.click()
        self.package_version.fill(package_version)
        self.set_country.click()
        self.select_country.click()
        self.register_country_btn.click()
        self.ingame_display_order.fill(ingame_display_order)
        self.english_title.fill(self.mod_name)
        self.english_oneline_description.fill(eng_oneline_description)
        self.english_description.fill(eng_description)
        self.genre_settings.click()
        self.genre_selected.click()

    def click_screenshot_btn(self):
        self.add_screenshot.click()


    def click_register_btn(self):
        self.register_btn.click()
        self.confirm_btn.click()


