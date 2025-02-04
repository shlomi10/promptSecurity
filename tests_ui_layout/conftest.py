import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.bank_of_america import BankOfAmerica
from pages.chatGPT import ChatGPT
from pages.extensionPage import ExtensionPage
from pages.gemini import Gemini
from pages.gemini_error_page import GeminiErrorPage
from utils.constants import EXTENSION_URL


@pytest.fixture(scope="function", autouse=True)
def initialize():
    options = Options()
    options.add_extension(r"..\extension.crx")
    options.add_argument("--lang=en-US")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # options.add_argument('--headless=new') # Runs Chrome in headless mode.

    driver = webdriver.Chrome(options=options)
    #driver = uc.Chrome(options=options)
    # request.cls.driver = driver

    chat_gpt_page = ChatGPT(driver)
    gemini_page = Gemini(driver)
    gemini_error_page = GeminiErrorPage(driver)
    bank_of_america_page = BankOfAmerica(driver)
    extension_page = ExtensionPage(driver)

    driver.get(EXTENSION_URL)

    driver.maximize_window()
    yield driver, chat_gpt_page, gemini_page, gemini_error_page, extension_page, bank_of_america_page
    driver.close()
    driver.quit()

#tryfirst=True: Ensures this hook runs before other hooks of the same type.
# hookwrapper=True: Indicates the function will wrap the execution, allowing code both before and after the hook.
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Attach screenshot to the report on failure."""
    outcome = yield # Wrap the execution to modify the result
    report = outcome.get_result()

    # Proceed only if the test failed during the main execution phase
    if report.when == "call" and report.failed:
        initialize_fixture = item.funcargs.get("initialize")
        if initialize_fixture:
            driver = initialize_fixture[0]

            # Attach screenshot
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )