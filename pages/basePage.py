import allure
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage(object):

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def get_web_driver(self):
        return self.driver

    @allure.step("click on element locator")
    def click(self, locator) -> bool:
        try:
            self.get_web_driver().find_element(*locator).click()
            return True
        except Exception as e:
            allure.attach(
                body=f"Error occurred: {str(e)}",
                name="click on element",
                attachment_type=allure.attachment_type.TEXT
            )
            return False

    @allure.step("fill text on locator")
    def fill_text(self, locator, txt: str) -> bool:
        try:
            elem = self.get_web_driver().find_element(*locator)
            elem.clear()
            elem.send_keys(txt)
            return True
        except Exception as e:
            allure.attach(body=f"Error occurred: {str(e)}",
                          name="fill text on locator",
                          attachment_type=allure.attachment_type.TEXT
                          )
            return False

    @allure.step("press enter on locator")
    def press_enter(self, locator) -> bool:
        try:
            elem = self.get_web_driver().find_element(*locator)
            elem.send_keys(Keys.RETURN)  # or use Keys.ENTER
            return True
        except Exception as e:
            allure.attach(body=f"Error occurred: {str(e)}",
                          name="press enter on locator",
                          attachment_type=allure.attachment_type.TEXT
                          )
            return False

    @allure.step("wait for visibility of element locator")
    def wait_for_visibility_of_element(self, locator) -> bool:
        try:
            WebDriverWait(self.get_web_driver(), 10).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            print(f"\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> {locator[1]}")
            allure.attach(
                body=f"Failed to find element: {locator[1]} within {10} seconds",
                name="Timeout Error",
                attachment_type=allure.attachment_type.TEXT
            )
            return False

    @allure.step("wait for presence of element locator")
    def wait_for_presence_of_element(self, locator) -> bool:
        try:
            WebDriverWait(self.get_web_driver(), 10).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            print(f"\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> {locator[1]}")
            allure.attach(
                body=f"Failed to find element: {locator[1]} within {10} seconds",
                name="Timeout Error",
                attachment_type=allure.attachment_type.TEXT
            )
            return False

    @allure.step("wait for element locator to be clickable")
    def wait_for_element_to_be_clickable(self, locator) -> bool:
        try:
            WebDriverWait(self.get_web_driver(), 20).until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            print(f"\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> {locator[1]}")
            allure.attach(
                body=f"Failed to find element: {locator[1]} within {20} seconds",
                name="Timeout Error",
                attachment_type=allure.attachment_type.TEXT
            )
            return False

    @allure.step("get text from element locator")
    def get_text_from_element(self, locator) -> tuple[bool, str]:
        try:
            text = self.get_web_driver().find_element(*locator).text
            return True, text
        except Exception as e:
            allure.attach(body=f"Error occurred: {str(e)}",
                          name="Error while getting text from element",
                          attachment_type=allure.attachment_type.TEXT
                          )
            return False, str(e)

    @allure.step("switch to iframe")
    def switch_to_iframe(self, locator) -> bool:
        try:
            iframe = self.get_web_driver().find_element(*locator)
            self.get_web_driver().switch_to.frame(iframe)
            return True
        except Exception as e:
            allure.attach(body=f"Error occurred: {str(e)}",
                          name="Error while switch to iframe",
                          attachment_type=allure.attachment_type.TEXT
                          )
            return False

    @allure.step("get href from element")
    def get_href_from_element(self, locator) -> tuple[bool, str]:
        try:
            if self.wait_for_presence_of_element(locator):
                href_value = self.get_web_driver().find_element(*locator).get_attribute("href")
            return True, href_value
        except Exception as e:
            allure.attach(body=f"Error occurred: {str(e)}",
                          name="Error while get the href from element",
                          attachment_type=allure.attachment_type.TEXT
                          )
            return False, str(e)
