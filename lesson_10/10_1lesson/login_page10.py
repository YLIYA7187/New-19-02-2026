from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.username_field_locator = (By.ID, "user-name")
        self.password_field_locator = (By.ID, "password")
        self.login_button_locator = (By.ID, "login-button")

    @allure.step("Ввод логина '{username}' и пароля '{password}'")
    def login(self, username: str, password: str) -> None:
        print("Ожидание загрузки страницы авторизации...")
        self.driver.get("https://www.saucedemo.com")

        # Ждём видимости поля логина
        username_field = self.wait.until(
            EC.visibility_of_element_located(self.username_field_locator)
        )
        print(f"Текущий URL: {self.driver.current_url}")
        print("Поле логина найдено и видимо на странице")

        password_field = self.wait.until(
            EC.element_to_be_clickable(self.password_field_locator)
        )
        print("Поле пароля найдено и готово к вводу")

        username_field.send_keys(username)
        password_field.send_keys(password)

        login_button = self.wait.until(
            EC.element_to_be_clickable(self.login_button_locator)
        )
        print("Кнопка входа найдена и готова к нажатию")
        login_button.click()
