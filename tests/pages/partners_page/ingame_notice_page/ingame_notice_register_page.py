from playwright.sync_api import Playwright,Page
import uuid
class register_ingame_notice_page:
    def __init__(self,page:Page):
        self.page = page
        self.notice_iframe = page.frame_locator("iframe[id^='iframe-BLZ']")
        self.register_notice= self.notice_iframe.locator("//*[contains(text(),'Register') and @class='p-button-label']")
        self.notice_country = self.notice_iframe.locator("//*[@class='p-button p-component text-14']")
        self.notice_country_select= self.notice_iframe.locator("//*[contains(text(),'Select All')]")
        self.notice_register_country = self.notice_iframe.locator("(//*[contains(text(),'Register') and @class='p-button-label'])[2]")
        self.notice_content_input = self.notice_iframe.locator("//*[@data-pc-name='textarea']")
        self.notice_content= f'notice_content{uuid.uuid4().hex[:6]}'
        self.register_notice_2_btn =self.notice_iframe.locator("//*[contains(text(),'Register') and @class='p-button-label']")
        self.confirm_btn= self.notice_iframe.locator("//*[contains(text(),'Confirm') and @class='p-button-label']")
    def send_platform_option(self,platform):
        return self.notice_iframe.locator(f'(//*[contains(text(),"{platform}")])[1]')

    def display_area_option(self,display_area):
        locator=self.notice_iframe.locator(f'(//*[contains(text(),"{display_area}")])[2]')
        if locator.count() ==0:
            locator=self.notice_iframe.locator(f'//*[contains(text(),"{display_area}")]')
        return locator
    def send_type_option(self,send_type):
        return self.notice_iframe.locator(f'//*[contains(text(),"{send_type}")]')
    def select_platform(self,platform):
        print(f"Selecting platform: {platform}")
        self.send_platform_option(platform).click()


    def select_display_area(self,display_area):
        self.display_area_option(display_area).click()

    def select_send_type(self,send_type):
        print(f"Selecting send_type: {send_type}")
        self.send_type_option(send_type).click()

    def select_notice_country(self):
        self.notice_country.click()
        self.notice_country_select.click()
        self.notice_register_country.click()

    def input_notice_content(self):
        self.notice_content_input.fill(self.notice_content)

    def click_notice_register(self):
        self.register_notice_2_btn.click()
        self.confirm_btn.click()
        self.confirm_btn.click()




