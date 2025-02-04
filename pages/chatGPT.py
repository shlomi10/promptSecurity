import allure
from selenium.webdriver.common.by import By

from pages.basePage import BasePage


class ChatGPT(BasePage):
    log_in_btn = (By.CSS_SELECTOR, "[data-testid='login-button']")
    search_field = (By.XPATH, "//textarea[@name='q']")
    email_input_field = (By.CSS_SELECTOR, ".email-input ")
    continue_btn = (By.CSS_SELECTOR, ".continue-btn ")
    message_input_field = (By.CSS_SELECTOR, "#prompt-textarea")
    chat_gpt_greeting_title = (By.XPATH, "//h1[contains(.,'What can I help with?')]")


    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("check if element presented")
    def check_chat_gpt_allowance(self) -> bool:
        return self.wait_for_visibility_of_element(self.chat_gpt_greeting_title)

    @allure.step("send greeting message")
    def send_greeting_message(self):
        self.wait_for_visibility_of_element(self.message_input_field)
        self.wait_for_element_to_be_clickable(self.message_input_field)
        self.fill_text(self.message_input_field, "Hello World")
        self.press_enter(self.message_input_field)

    @allure.step("click login")
    def click_logIn(self) -> None:
        self.wait_for_element_to_be_clickable(self.log_in_btn)
        self.click(self.log_in_btn)

    @allure.step("fill details")
    def fill_details(self) -> None:
        self.wait_for_visibility_of_element(self.email_input_field)
        self.fill_text(self.email_input_field, "test@gmail.com")
        self.wait_for_element_to_be_clickable(self.continue_btn)
        self.click(self.continue_btn)

