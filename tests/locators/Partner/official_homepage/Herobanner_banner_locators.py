from playwright.sync_api import Playwright,Page
import uuid
class component_hero_banner_locators:
    def __init__(self,page:Page):
        self.page = page
        self.iframe = page.frame_locator("iframe[id^='iframe-BLZ']")
        self.random_suffix = uuid.uuid4().hex[:6]
        self.title_input=self.iframe.locator('//*[@id="component-title"]')
        self.display_options=self.iframe.locator('(//*[@name="display_true"])[1]')
        self.display_period_from= self.iframe.locator('(//*[@placeholder="YYYY.MM.DD HH:mm"])[3]')
        self.display_period_to = self.iframe.locator('(//*[@placeholder="YYYY.MM.DD HH:mm"])[4]')
        self.display_order= self.iframe.locator('//*[@id="component-displayOrder"]')
        self.banner_btn= self.iframe.locator('//*[@class="p-button p-component p-button-primary text-14"]')
        self.banner_type= self.iframe.locator('//*[contains(text(),"Image Type")]')
        self.main_title_input=self.iframe.locator('//*[@id="mainTitle-en-0"]')
        self.sub_title_input=self.iframe.locator('//*[@id="subTitle-en-0"]')
        self.upload_button_PC= self.iframe.locator('(//*[contains(text(),"Upload")])[1]')
        self.upload_button_mobile= self.iframe.locator('(//*[contains(text(),"Upload")])[2]')
        self.link= self.iframe.locator('//*[@id="link"]')
        self.link_input= self.iframe.locator('(//*[@class="p-inputtext p-component w-350 text-14"])[2]')
        self.register_btn= self.iframe.locator('//*[contains(text(),"Register") and @class="p-button-label"]')
        self.register_complete_btn= self.iframe.locator('(//*[contains(text(),"Confirm") and @class="p-button-label"])[1]')
        self.component_name = f'banner_component_{self.random_suffix}'
        # Video type
        self.banner_type_video = self.iframe.locator('//*[contains(text(),"Video Type")]')
        self.background_color = self.iframe.locator('//*[@id="backgroundColor-en-0"]')
        self.select_background_color= self.iframe.locator('//*[@placeholder="#"]')
        self.apply_background_color=self.iframe.locator('//*[@aria-label="Apply"]')
        self.video_url= self.iframe.locator('//*[@id="videoUrl-en-0"]')
        #Validation required fields banner
        self.missing_banner= self.iframe.locator('//*[contains(text(),"Please add at least one Banner")]')
        self.invalid_display_period_banner= self.iframe.locator('//*[contains(text(),"Please enter main title")]')
        self.missing_main_title = self.iframe.locator('//*[contains(text(),"Please enter main title")]')
        self.missing_image_pc= self.iframe.locator('//*[contains(text(),"Please register PC image")]')
        self.upload_locator_PC=self.page.locator('(//*[contains(text(),"Upload")])[1]')
        self.filepath_PC="./tests/resourse/banner_images/png_2560x542.png"
        self.upload_image_mobile=self.iframe.locator('(//*[contains(text(),"Upload")])[2]')
        self.filepath_mobile="./tests/resourse/banner_images/png_1364x642.png"
        self.filepath_PC_banner = "./tests/resourse/banner_images/png_1300x325.png"
        self.filepath_mobile_banner = "./tests/resourse/banner_images/png_1138x210.png"
        self.missing_image_mobile= self.iframe.locator('//*[contains(text(),"Please register mobile image")]')
        self.missing_link_url= self.iframe.locator('//*[contains(text(),"Please enter link information")]')

