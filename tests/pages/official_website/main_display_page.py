from playwright.sync_api import Playwright, Page

from tests.pages.partners_page.official_homepage.register_banner_component_page import register_banner_component



class main_display_page:
    def __init__(self,page:Page,main_page_url,component_name=None):
        self.page=page
        self.component_name = component_name
        self.main_display_url= main_page_url


    def open_main_page(self):
        self.page.goto(f'{self.main_display_url}')
    def verify_register_banner_component_displayed(self,component_name):
        new_component = self.page.locator(f'xpath=(//*[contains(text(),"{component_name}")])[1]')
        new_component.is_visible()
