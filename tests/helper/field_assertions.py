from playwright.sync_api import expect
from pyexpat.errors import messages

from tests.pages.partners_page.official_homepage.register_common_component_page import register_common_component

def assert_field(pom: register_common_component, field: str, visibility: str, default_value: str):
    locator = pom.get_field_locator(field)

    if locator is None:
        raise ValueError(f"Field '{field}' not found in field_map")

    if visibility == "invisible":
        expect(locator).not_to_be_visible()
        return

    expect(locator).to_be_visible()

    if default_value == "enable":
        pass  # visible là đủ

    elif default_value == "checked":
        expect(locator).to_be_checked()

    elif default_value == "All":
        expect(locator).to_have_text("All")

    else:
        expect(locator).to_have_text(default_value)

def assert_require_fields(locators:str,message:str):
        expect(locators).to_be_visible(timeout=5000)
        message or f"locator '{locators}' is not visible"