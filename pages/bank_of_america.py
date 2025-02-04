import allure
from selenium.webdriver.common.by import By

from pages.basePage import BasePage


class BankOfAmerica(BasePage):
    logo_element = (By.XPATH, "//a[@itemprop='url']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("check if element presented")
    def get_link_from_element(self) -> tuple[bool, str]:
        return self.get_href_from_element(self.logo_element)