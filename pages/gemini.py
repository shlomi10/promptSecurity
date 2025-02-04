import allure
from selenium.webdriver.common.by import By

from pages.basePage import BasePage


class Gemini(BasePage):
    recaptcha_iframe = (By.CSS_SELECTOR, "iframe[title='reCAPTCHA']")
    recaptcha_checkbox = (By.ID, "recaptcha-anchor")
    login_btn = (By.CSS_SELECTOR, "[data-test-id='action-button']")
    enter_email_field = (By.XPATH, "//input[@type='email']")
    next_btn = (By.CSS_SELECTOR, "#identifierNext")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("click on recaptcha")
    def click_on_recaptcha(self) -> None:
        if self.wait_for_visibility_of_element(self.recaptcha_iframe):
            self.switch_to_iframe(self.recaptcha_iframe)
            self.click(self.recaptcha_checkbox)
            self.driver.switch_to.default_content()
        else:
            print("reCAPTCHA not found")
            pass

    @allure.step("click login")
    def click_login(self) -> None:
        self.wait_for_element_to_be_clickable(self.login_btn)
        self.click(self.login_btn)

    @allure.step("enter email")
    def enter_email(self, test_mail: str) -> None:
        self.wait_for_visibility_of_element(self.enter_email_field)
        self.fill_text(self.enter_email_field, test_mail)
        self.click(self.next_btn)
