from pyexpat.errors import messages

from tests.helper.field_assertions import assert_locator_visible
class validate_require_fields:
    def __init__(self,page,base_url):
        self.page=page
        self.base_url=base_url
        self.assertions =assert_locator_visible(page)
    def verify_required_error(self,field_name:str):
        error_locator=self.page.locator(
            f'//label[contains(text(),"{field_name}")]'
            f'/following-sibling::div[contains(text(),"{field_name}")]'
        )
        self.assertions.assert_locator_visible(
            error_locator,
            messages=f'Required error of field {field_name} is not visible',
        )