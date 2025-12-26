import uuid
from playwright.sync_api import Playwright,Page
class register_ranking_component:
    def __init__(self,page:Page):
        self.page =page
        self.iframe = page.frame_locator("#iframe-BLZ00000001004")
        self.Set_Aggregation_Period_Entire= self.iframe.locator('//*[contains(@value,"ENTIRE")]')
    def select_Aggregation_Period(self):
        self.Set_Aggregation_Period_Entire.click()