from playwright.sync_api import sync_playwright,Page
from conftest import base_url
class ingame_notice_management_page:
    def __init__(self,page:Page,base_url):
        self.page =page
        self.base_url =base_url
        self.notice_iframe= page.frame_locator("iframe[id^='iframe-BLZ']")
        self.bubblely_menu = self.page.locator('//*[@menu-id="Bubblelyz"]')
        self.notice_management = self.page.locator('//*[@menu-id="BLZ00000017000"]')
        self.ingame_notice_management = self.page.locator(
            '//*[contains(text(),"In-game Notice Management") and @class="menu-title"]'
        )
        self.register_btn = self.notice_iframe.locator('//*[contains(text(),"Register") and @class="p-button-label"]')
        self.ingame_notice_management_sb = self.page.locator('//*[@menu-id="BLZ00000017002"]')
    def get_ingame_notice_menu(self):
        if self.ingame_notice_management.count()>0:
            return self.ingame_notice_management
        else:
            return self.ingame_notice_management_sb
    def navigate_notice_management(self):
        self.page.goto(f"{self.base_url}/main")
        self.bubblely_menu.click()
        self.notice_management.click()
        self.get_ingame_notice_menu().click()

    def click_register1_button(self):
        self.register_btn.click()
