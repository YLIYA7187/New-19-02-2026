from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.username_field_locator = (By.ID, "user-name")
        self.password_field_locator = (By.ID, "password")
        self.login_button_locator = (By.ID, "login-button")

    def login(self, username, password):
        username_field = self.wait.until(
            EC.presence_of_element_located(self.username_field_locator)
        )
        password_field = self.driver.find_element(*self.password_field_locator)

        username_field.send_keys(username)
        password_field.send_keys(password)

        login_button = self.driver.find_element(*self.login_button_locator)
        login_button.click()
