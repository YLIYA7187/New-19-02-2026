from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalcMainPage:
    def __init__(self, driver):
        """
        Конструктор класса CalcMainPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Открытие страницы калькулятора")
    def open(self):
        """
        Открывает страницу калькулятора.
        """
        self.driver.get(
            "https://bonigarcia.dev/" "selenium-webdriver-java/slow-calculator.html"
        )

    @allure.step("Установка задержки {delay} секунд")
    def set_delay(self, delay):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.

        :param delay: int — время задержки в секундах.
        """
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    @allure.step("Нажатие кнопки '{button}'")
    def click_button(self, button):
        """
        Нажимает на кнопку калькулятора.

        :param button: str — текст на кнопке, которую нужно нажать.
        """
        self.driver.find_element(By.XPATH, f"//span[text()='{button}']").click()

    @allure.step("Нажатие кнопок: {buttons}")
    def click_buttons(self, buttons):
        """
        Нажимает на несколько кнопок калькулятора по очереди.
        :param buttons: list[str] — список текстов на кнопках,
        которые нужно нажать.
        """
        for button in buttons:
            self.click_button(button)

    @allure.step("Ожидание результата '{expected_result}'")
    def wait_for_result(self, expected_result, delay):
        """
        Ожидает появления ожидаемого результата на экране калькулятора.

        :param expected_result: str — ожидаемый результат.
        :param delay: int — время задержки в секундах.
        """
        # Добавляем +1 секунду к задержке для надежности
        WebDriverWait(self.driver, delay + 1).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), expected_result)
        )

    @allure.step("Получение результата с экрана калькулятора")
    def get_result(self):
        """
        Возвращает текущий результат с экрана калькулятора.

        :return: str — текст результата на экране калькулятора.
        """
        return self.driver.find_element(By.CLASS_NAME, "screen").text
