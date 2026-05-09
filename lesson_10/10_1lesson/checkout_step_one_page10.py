from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckoutStepOnePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        # Локаторы для полей формы
        self.first_name_field_locator = (By.ID, "first-name")
        self.last_name_field_locator = (By.ID, "last-name")
        self.postal_code_field_locator = (By.ID, "postal-code")
        # Локатор для кнопки продолжения
        self.continue_button_locator = (By.ID, "continue")

    @allure.step("Заполнение формы доставки")
    def fill_form(self, user_info: dict) -> None:
        """
        Заполняет форму доставки информацией о пользователе.

        Args:
            user_info (dict): Словарь с данными пользователя:
                - "first-name": имя
                - "last-name": фамилия
                - "postal-code": почтовый индекс
        """
        # Заполняем поле имени
        first_name_field = self.wait.until(
            EC.element_to_be_clickable(self.first_name_field_locator)
        )
        first_name_field.clear()
        first_name_field.send_keys(user_info["first-name"])

        # Заполняем поле фамилии
        last_name_field = self.wait.until(
            EC.element_to_be_clickable(self.last_name_field_locator)
        )
        last_name_field.clear()
        last_name_field.send_keys(user_info["last-name"])

        # Заполняем поле почтового индекса
        postal_code_field = self.wait.until(
            EC.element_to_be_clickable(self.postal_code_field_locator)
        )
        postal_code_field.clear()
        postal_code_field.send_keys(user_info["postal-code"])

    @allure.step("Продолжение к следующему шагу")
    def continue_to_next_step(self) -> None:
        """
        Нажимает кнопку продолжения для перехода к следующему шагу оформления заказа.
        """
        continue_button = self.wait.until(
            EC.element_to_be_clickable(self.continue_button_locator)
        )
        continue_button.click()
