import allure
from selenium.webdriver.common.by import By

from pages.basePage import BasePage
from utils.constants import API_DOMAIN, API_KEY


class ExtensionPage(BasePage):
    api_domain_field = By.XPATH, "//input[@id='apiDomain']"
    api_key_field = By.XPATH, "//input[@id='apiKey']"
    save_button = By.XPATH, "//button[@id='saveButton']"


    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("fill details in extension")
    def fill_details_in_extension(self) -> None:
        self.wait_for_visibility_of_element(self.api_domain_field)
        self.fill_text(self.api_domain_field, API_DOMAIN)
        self.wait_for_visibility_of_element(self.api_key_field)
        self.fill_text(self.api_key_field, API_KEY)
        self.wait_for_element_to_be_clickable(self.save_button)
        self.click(self.save_button)
