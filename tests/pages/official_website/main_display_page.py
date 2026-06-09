from playwright.async_api import expect
from playwright.sync_api import Playwright, Page

from tests.pages.partners_page.official_homepage.register_banner_component_page import register_banner_component



class main_display_page:
    def __init__(self,page:Page,main_page_url,component_name=None):
        self.page=page
        self.component_name = component_name
        self.main_display_url= main_page_url
        self.mods_tab = page.locator("(//*[contains(text(), 'MODs')])[1]")


    def open_main_page(self):
        self.page.goto(f'{self.main_display_url}')
        self.mods_tab.click()
        self.page.wait_for_load_state("networkidle")
        print(f"main url is {self.main_display_url}")
    def verify_register_banner_component_displayed(self,component_name):
        assert component_name, f"component_name is None or empty!"
        new_component = self.page.locator(f'xpath=(//*[contains(.,"{component_name}")])[1]')
        print(f'new_component: {new_component}')
        assert new_component.is_visible(),\
        f"component_name '{component_name}' is not visible"
