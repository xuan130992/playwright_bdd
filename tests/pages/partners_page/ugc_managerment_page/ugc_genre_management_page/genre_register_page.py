from playwright.sync_api import Playwright,Page
import uuid
class RegisterPage(Page):
    def __init__(self,page:Page):
        self.page = page
        self.iframe_genre=page.frame_locator('#iframe-BLZ00000005003')
        self.random_suffix = uuid.uuid4().hex[:6]
        #self.usage_status_use= self.page.locator('//*[contains(text(),"Usage Status")]')
        #self.usage_status_notuse= self.page.locator('//*[contains(text(),"Usage Status")]')
        self.genre_title= self.iframe_genre.get_by_label('Genre Name ')
        self.genre_name= f'genre_name{uuid.uuid4().hex[:6]}'
        self.genre_upload= self.iframe_genre.locator('(//*[@class="p-button-label" and contains(text(),"Upload")])[1]')
        self.register_btn= self.iframe_genre.locator('//*[contains(text(),"Register") and @class="p-button-label"]')
        self.confirm_btn1= self.iframe_genre.locator('//*[contains(text(),"Confirm") and @class="p-button-label"]')
        self.confirm_btn2= self.iframe_genre.locator('//*[contains(text(),"Confirm") and @class="p-button-label"]')
    def register_genre(self,usage_status:str):
        print("input genre")
        self.iframe_genre.locator(usage_status).click()
        self.genre_title.fill(self.genre_name)
    def click_upload_genre(self):
        self.genre_upload.click()
    def click_register2_btn(self):
        print('click_register2_btn')
        self.register_btn.click()
        self.confirm_btn1.click()
        self.confirm_btn2.click()


