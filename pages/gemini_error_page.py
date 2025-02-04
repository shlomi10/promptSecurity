import allure
from selenium.webdriver.common.by import By

from pages.basePage import BasePage


class GeminiErrorPage(BasePage):
    try_again_button_locator = (By.CSS_SELECTOR, "[data-primary-action-label='Try again']")
    error_locator = (By.CSS_SELECTOR, '#headingText span')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("click login")
    def get_error_message(self) -> tuple[bool, str]:
        self.wait_for_element_to_be_clickable(self.try_again_button_locator)
        self.wait_for_visibility_of_element(self.error_locator)
        success, error_message = self.get_text_from_element(self.error_locator)
        if not success:
            raise AssertionError(f"Failed to get error message: {error_message}")
        return success, error_message
