import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome ou firefox")
    parser.addoption("--executor", action="store", default="local", help="Executor: local ou remote")

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser").lower()
    executor = request.config.getoption("--executor").lower()
    grid_url = os.getenv("SELENIUM_GRID_URL", "http://localhost:4444/wd/hub")

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        
        if executor == "remote":
            driver_instance = webdriver.Remote(command_executor=grid_url, options=options)
        else:
            driver_instance = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        
        if executor == "remote":
            driver_instance = webdriver.Remote(command_executor=grid_url, options=options)
        else:
            driver_instance = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Navegador '{browser}' não suportado.")

    yield driver_instance

    # Hook to add screenshot to Allure if test fails
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        try:
            allure.attach(
                driver_instance.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print(f"Failed to capture screenshot: {e}")

    driver_instance.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)