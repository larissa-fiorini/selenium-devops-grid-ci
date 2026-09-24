import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.epic("Authentication")
@allure.feature("Login")
class TestLogin:

    @allure.story("Successful Login on SauceDemo")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_login(self, driver):
        with allure.step("Go to SauceDemo page"):
            driver.get("https://www.saucedemo.com/")

        with allure.step("Enter username and password"):
            driver.find_element(By.ID, "user-name").send_keys("standard_user")
            driver.find_element(By.ID, "password").send_keys("secret_sauce")

        with allure.step("Click on login button"):
            driver.find_element(By.ID, "login-button").click()

        with allure.step("Verify user is logged in"):
            wait = WebDriverWait(driver, 10)
            title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
            assert title.text.upper() == "PRODUCTS"