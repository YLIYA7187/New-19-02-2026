# test_calculator.py
import pytest
from selenium import webdriver
from calculator_page import CalculatorPage  # Укажите правильный путь к вашему файлу


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    """
    Тест: проверка работы медленного калькулятора.
    1. Открыть страницу с калькулятором.
    2. Ввести значение задержки 45 с в поле #delay.
    3. Нажать кнопки: 7 + 8 =.
    4. Проверить, что через 45 с отобразится результат 15 в .screen.
    """
    page = CalculatorPage(driver)

    # 1. Ввод значения задержки
    page.set_delay(45)

    # 2. Нажатие кнопок калькулятора: 7 + 8 =
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    # 3. Получение и проверка результата
    actual_result = page.get_result()
    assert (
        actual_result == "15"
    ), f"❌ Ожидался результат '15', но найдено '{actual_result}'"
