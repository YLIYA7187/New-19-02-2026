import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    """Фикстура для управления браузером."""
    print("\n🚀 Запускаю браузер Chrome...")
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    print("🔚 Закрываю браузер...")
    driver.quit()


def test_slow_calculator(driver):
    """
    Тест: проверка работы медленного калькулятора.
    1. Открыть страницу с калькулятором.
    2. Ввести значение задержки 45 с в поле #delay.
    3. Нажать кнопки: 7 + 8 =.
    4. Проверить, что через 45 с отобразится результат 15 в .screen.
    """
    wait = WebDriverWait(driver, 70)  # Таймаут 70 с: 45 с задержка + запас

    # 1. Открытие страницы
    print("Открываю страницу калькулятора...")
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # 2. Ввод значения задержки в поле #delay
    print("Ввожу значение задержки 45 секунд в поле #delay...")
    delay_input = wait.until(EC.element_to_be_clickable((By.ID, "delay")))
    delay_input.clear()
    delay_input.send_keys("45")

    # 3. Нажатие кнопок калькулятора
    print("Нажимаю кнопки калькулятора: 7 + 8 =")

    # Кнопка 7 — ищем по тексту внутри span
    button_7 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '7')]"))
    )
    button_7.click()

    # Кнопка + — ищем по тексту
    button_plus = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '+')]"))
    )
    button_plus.click()

    # Кнопка 8 — используем класс как дополнительный критерий
    button_8 = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(@class, 'btn') and contains(text(), '8')]")
        )
    )
    button_8.click()

    # Кнопка = — ищем по классу и тексту
    button_equals = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[contains(@class, 'btn-outline-warning') and contains(text(), '=')]",
            )
        )
    )
    button_equals.click()

    # 4. Ожидание и проверка результата через 45 секунд
    print("Ожидаю отображения результата через 45 секунд...")

    result_locator = (By.CSS_SELECTOR, ".screen")  # Класс .screen для результата

    try:
        # Ждём появления элемента с результатом
        result_element = wait.until(EC.presence_of_element_located(result_locator))

        # Ждём, пока текст в элементе станет равен "15"
        wait.until(lambda d: d.find_element(*result_locator).text == "15")

        actual_result = result_element.text
        assert (
            actual_result == "15"
        ), f"❌ Ожидался результат '15', но найдено '{actual_result}'"
        print(f"✅ Результат корректен: {actual_result}")

    except Exception as e:
        print(f"❌ Ошибка при проверке результата: {e}")
        driver.save_screenshot("calculator_error.png")
        raise

    print("\n🎉 ТЕСТ УСПЕШНО ПРОЙДЕН!")
    print("✅ Все требования задачи выполнены!")
