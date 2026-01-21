from playwright.sync_api import Playwright,Page
from conftest import base_url
class ugc_genre_managementPage:
    def __init__(self,page:Page,base_url):
        self.page = page
        self.base_url = base_url
        self.iframe_genre= page.frame_locator('#iframe-BLZ00000005003')
        self.bubblely_menu = self.page.locator('//*[contains(text(),"Bubblelyz")]')
        self.ugc_management = self.page.locator('//*[contains(text(),"UGC Management") and @class="menu-title"]')
        self.ugc_genre_manage=self.page.locator('//*[contains(text(),"UGC Genre Management") and @class="menu-title"]')
        self.register_btn= self.iframe_genre.locator('//*[contains(text(),"Register") and @class="p-button-label"]')
    def navigate_genre_management(self):
        self.page.goto(f"{self.base_url}/main")
        self.bubblely_menu.click()
        self.ugc_management.click()
        self.ugc_genre_manage.click()
    def click_register1_btn(self):
        self.register_btn.click()



