from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CheckoutStepOnePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        self.first_name_field_locator = (By.ID, "first-name")
        self.last_name_field_locator = (By.ID, "last-name")
        self.postal_code_field_locator = (By.ID, "postal-code")
        self.continue_button_locator = (By.ID, "continue")

    @allure.step("Заполнение формы доставки")
    def fill_form(self, user_info: dict) -> None:
        first_name_field = self.wait.until(
            EC.element_to_be_clickable(self.first_name_field_locator)
        )
        first_name_field.send_keys(user_info["first-name"])

        last_name_field = self.driver.find_element(*self.last_name_field_locator)
        last_name_field.send_keys(user_info["last-name"])

        postal_code_field = self.driver.find_element(*self.postal_code_field_locator)
        postal_code_field.send_keys(user_info["postal-code"])

    @allure.step("Продолжение к следующему шагу")
    def continue_to_next_step(self) -> None:
        continue_button = self.wait.until(
            EC.element_to_be_clickable(self.continue_button_locator)
        )
        continue_button.click()

