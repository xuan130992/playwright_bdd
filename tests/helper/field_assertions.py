from playwright.sync_api import expect, Locator
from pyexpat.errors import messages

from tests.pages.partners_page.official_homepage.register_common_component_page import register_common_component
from tests.locators.Partner.official_homepage.common_locators import component_common_locators
from tests.locators.Partner.official_homepage.Herobanner_banner_locators import component_hero_banner_locators

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

def assert_locator_visible(locator: Locator, message: str = ""):
    expect(locator).to_be_visible(timeout=5000)

def fill_validation(com_loc:component_common_locators,banner_loc:component_hero_banner_locators,fields:str):
    actions={
        "Title":lambda:com_loc.title_input.fill(com_loc.component_name),
        "Display Period from":lambda:com_loc.display_period_from.fill("2026.01.01 19:45"),
        "Display Period to":lambda :com_loc.display_period_to.fill("2025.12.31 19:45"),
        "Main Title":lambda:banner_loc.main_title_input.fill(banner_loc.component_name),
    }
    action =actions.get(fields)
    if action is None:
        raise ValueError(f"Field '{fields}' not found in field_map")
    action()

def get_error_locator(com_loc:component_common_locators,banner_loc:component_hero_banner_locators,field:str):
    field_error_locator_map = {
        "Title": lambda : com_loc.missing_title,
        "Display Period": lambda : com_loc.invalid_display_period,
        "Main Title": lambda : banner_loc.missing_main_title,
        "PC image": lambda : banner_loc.missing_image_pc,
        "mobile image": lambda : banner_loc.missing_image_mobile,
        "Link URL": lambda : banner_loc.missing_link_url,

    }
    locator_func=field_error_locator_map.get(field)
    if locator_func is None:
        raise ValueError(f"Field '{field}' not found in field_map")
    return locator_func()