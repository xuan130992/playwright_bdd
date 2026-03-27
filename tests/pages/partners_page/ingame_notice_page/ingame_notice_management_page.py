from playwright.sync_api import sync_playwright,Page
from conftest import base_url
class ingame_notice_management_page:
    def __init__(self,page:Page,base_url):
        self.page =page
        self.base_url =base_url
        self.notice_iframe= page.frame_locator("#iframe-BLZ00000007001")
        self.bubblely_menu = self.page.locator('//*[contains(text(),"Bubblelyz")]')
        self.notice_management = self.page.locator('//*[contains(text(),"Notice Management") and @class="menu-title"]')
        self.ingame_notice_management = self.page.locator('//*[contains(text(),"In-game Notice Management") and @class="menu-title"]')
        self.register_btn = self.notice_iframe.locator('//*[contains(text(),"Register") and @class="p-button-label"]')
    def navigate_notice_management(self):
        self.page.goto(f"{self.base_url}/main")
        self.bubblely_menu.click()
        self.notice_management.click()
        self.ingame_notice_management.click()
    def click_register1_button(self):
        self.register_btn.click()
