import pytest
from selenium import webdriver
from СаclMainPageAllure import CalcMainPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.parametrize(
    "num1, operation, num2, expected_result, delay",
    [
        ("7", "+", "8", "15", 15),
        ("9", "-", "3", "6", 10),
        ("4", "x", "5", "20", 20),
        ("8", "÷", "2", "4", 5),
    ],
)
@allure.title(
    "Тестирование калькулятора: {num1} {operation} {num2} " "= {expected_result}"
)
@allure.description(
    "Тест проверяет корректность работу калькулятора " "с различными операциями."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_flow(driver, num1, operation, num2, expected_result, delay):
    """
    Тест проверяет работу калькулятора с различными операциями.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    :param num1: str — первое число для операции.
    :param operation: str — операция (+, -, x, ÷).
    :param num2: str — второе число для операции.
    :param expected_result: str — ожидаемый результат операции.
    :param delay: int — задержка в секундах для выполнения операции.
    """
    main_page = CalcMainPage(driver)

    with allure.step("Открытие страницы калькулятора"):
        main_page.open()

    with allure.step(f"Установка задержки {delay} секунд"):
        main_page.set_delay(delay)

    with allure.step(f"Нажатие кнопок: {num1}, {operation}, {num2}, '='"):
        main_page.click_buttons([num1, operation, num2, "="])

    with allure.step(f"Ожидание результата {expected_result}"):
        main_page.wait_for_result(expected_result, delay)

    with allure.step("Проверка результата"):
        assert main_page.get_result() == expected_result, (
            f"Ожидаемый результат: {expected_result}, "
            f"но получен: {main_page.get_result()}"
        )
