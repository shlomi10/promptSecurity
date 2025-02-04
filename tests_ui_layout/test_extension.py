import allure
import pytest

from tests_ui_layout.conftest import initialize
from utils.constants import CHAT_GPT_URL, GEMINI_URL, TEST_MAIL, BANK_OF_AMERICA_URL


@allure.epic("functional")
@allure.feature("title - functional")
@allure.story("validate the functionality of the extension")
@pytest.mark.flaky(reruns=2)
class TestExtensionFunctionality:

    @pytest.fixture(autouse=True)
    def setup(self, initialize):
        """Initialize driver and page objects before each test"""
        self.driver, self.chat_gpt_page, self.gemini_page, self.gemini_error_page, self.extension_page, self.bank_of_america_page = initialize

    @allure.story("Validate extension on ChatGPT")
    @allure.description("validate if extension is worked correct on chat GPT")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("validate extension on chat GPT")
    def test_extension_case1(self, initialize):

        try:
            with allure.step("set the extension"):
                self.extension_page.fill_details_in_extension()

                # Navigate to ChatGPT URL
                self.driver.get(CHAT_GPT_URL)

            with allure.step("Login to ChatGPT"):
                assert self.chat_gpt_page.check_chat_gpt_allowance(), f"Failed to load chat gpt homepage"

                # chat_gpt_page.send_greeting_message()

                # chat_gpt_page.fill_details()

            # Print test result for GitHub Actions (successful)
            print("✅ Test Passed: Extension works on ChatGPT")

        except AssertionError as e:
            # Print the failure message for GitHub Actions
            print(f"❌ Test Failed: {str(e)}")
            raise

    @allure.story("Validate extension on Gemini")
    @allure.description("validate if extension is worked correct on Gemini")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("validate extension on Gemini")
    def test_extension_case2(self, initialize):

        try:
            with allure.step("set the extension"):
                self.extension_page.fill_details_in_extension()

                # Navigate to Gemini URL
                self.driver.get(GEMINI_URL)

            with allure.step("validate if there is recaptcha check"):
                self.gemini_page.click_on_recaptcha()

            with allure.step("Login to Gemini"):
                self.gemini_page.click_login()
                self.gemini_page.enter_email(TEST_MAIL)

            with allure.step("Validate error message on Gemini"):
                success, error_message = self.gemini_error_page.get_error_message()
                assert success, f"Failed to get error message"
                assert error_message == "Couldn’t sign you in", f"Expected error message 'Couldn’t sign you in', but got {error_message}"

            # Print test result for GitHub Actions (successful)
            print("✅ Test Passed: Extension works on Gemini")

        except AssertionError as e:
            # Print the failure message for GitHub Actions
            print(f"❌ Test Failed: {str(e)}")
            raise

    @allure.story("Validate extension on Bank of America")
    @allure.description("validate if extension is worked correct on bank of America")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Validate extension on Bank of America")
    def test_extension_case3(self, initialize):

        try:
            with allure.step("set the extension"):
                self.extension_page.fill_details_in_extension()

                # Navigate to Bank of America URL
                self.driver.get(BANK_OF_AMERICA_URL)

            with allure.step("validate if there is any block in bank of America"):
                success, link = self.bank_of_america_page.get_link_from_element()
                assert success, f"Failed to get link from bank of America"
                assert link == "https://www.bankofamerica.com/", f"Expected link 'https://www.bankofamerica.com', but got {link}"

            # Print test result for GitHub Actions (successful)
            print("✅ Test Passed: Extension works on Bank of America")

        except AssertionError as e:
            # Print the failure message for GitHub Actions
            print(f"❌ Test Failed: {str(e)}")
            raise