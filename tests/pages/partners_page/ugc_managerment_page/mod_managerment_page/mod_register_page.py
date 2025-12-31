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
        self.set_country= self.iframe.locator('//*[@class="p-button p-component text-14" and contains(.,"Set Countries")]')
        self.select_country= self.iframe.locator('//*[@id="v-0-264-check-all"]')
        self.register_country_btn= self.iframe.locator('(//*[@class="p-button-label" and contains(text(),"Register")])[1]')
        self.ingame_display_order=self.iframe.locator('//*[@class="p-inputtext p-component w-full text-14" and @placeholder="Input a number"]')
        self.english_title= self.iframe.locator('//*[@id="title-v-0-227"]')
        self.english_oneline_description= self.iframe.locator('//*[@id="one_line_description-v-0-227"]')
        self.english_description= self.iframe.locator('//*[@class="p-textarea p-component block w-full resize-none pr-35 text-14"]')
        self.genre_settings=self.iframe.locator('(//*[@class="p-button p-component btn btn-primary text-14"])[1]')
        self.genre_selected= self.iframe.locator('(//*[@class="flex items-center justify-center"])[2]')
        self.add_screenshot= self.iframe.locator('//*[@class="p-button p-component btn btn-primary text-14" and contains(.,"Add Screenshot")]')
        self.upload_screenshot=self.iframe.locator('(//*[@class="p-button-label" and contains(text(),"Upload")])[1]')
        # self.max_participants= self.iframe.locator()
        # self.min_participants= self.iframe.locator()
        # self.start_participants= self.iframe.locator()
        # self.reduction_time= self.iframe.locator()
        # self.addition_recruitment_time= self.iframe.locator()
        self.android_file_upload=self.iframe.locator('(//*[@class="p-button-label" and contains(text(),"Upload")])[4]')
        self.ios_file_upload= self.iframe.locator('(//*[@class="p-button-label" and contains(text(),"Upload")])[5]')
        self.windowns_file_upload= self.iframe.locator('(//*[@class="p-button-label" and contains(text(),"Upload")])[6]')
        self.server_file_upload= self.iframe.locator('(//*[@class="p-button-label" and contains(text(),"Upload")])[7]')
        self.register_btn= self.iframe.locator('//*[@class="p-button-label" and contains(text(),"Register")]')
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


