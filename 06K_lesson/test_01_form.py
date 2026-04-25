import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    """Фикстура для управления браузером."""
    print("\n🚀 Запускаю браузер...")
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    print("🔚 Закрываю браузер...")
    driver.quit()


def test_form_validation(driver):
    """
    Тест: проверка валидации формы.
    После сабмита поля заменяются на div с классами alert:
    - alert-success для заполненных полей
    - alert-danger для пустого zip-code (со значением 'N/A')
    """
    wait = WebDriverWait(driver, 30)

    # 1. Открытие страницы
    print("Открываю страницу...")
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # 2. Ожидание готовности формы
    wait.until(EC.visibility_of_element_located((By.NAME, "first-name")))

    # 3. Заполнение полей формы (кроме zip-code)
    print("Заполняю поля формы...")

    fields_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        # Поле 'zip-code' пропускаем намеренно, чтобы оставить пустым
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro",
    }

    for field_name, value in fields_data.items():
        if field_name == "zip-code":
            continue
        element = wait.until(EC.element_to_be_clickable((By.NAME, field_name)))
        element.clear()
        element.send_keys(value)

    # 4. Нажатие кнопки Submit
    print("Нажимаю кнопку Submit...")
    submit_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

    # --- 5. Проверка валидации ---

    # --- Проверка поля Zip Code ---
    print("Проверяю поле Zip Code...")
    zip_code_locator = (By.ID, "zip-code")

    try:
        zip_code_div = wait.until(EC.visibility_of_element_located(zip_code_locator))
        wait.until(EC.text_to_be_present_in_element(zip_code_locator, "N/A"))
        assert "alert-danger" in zip_code_div.get_attribute("class")
        print("✅ Поле Zip Code заменено на сообщение 'N/A' с красной подсветкой.")
    except Exception as e:
        print(f"❌ Ошибка при проверке Zip Code: {e}")
        driver.save_screenshot("zip_code_error.png")
        raise

    # --- Проверка остальных полей (должны стать alert-success) ---
    print("Проверяю остальные поля...")
    valid_fields = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company",
    ]

    for field_name in valid_fields:
        locator = (By.ID, field_name)  # После сабмита используем ID вместо NAME
        expected_value = fields_data[field_name]

        try:
            # Ждём появления div с правильным ID и классом alert-success
            wait.until(
                lambda d: (
                    d.find_element(*locator).is_displayed()
                    and "alert-success"
                    in d.find_element(*locator).get_attribute("class")
                )
            )
            field_element = driver.find_element(*locator)
            field_classes = field_element.get_attribute("class")
            actual_text = field_element.text

            # Проверяем класс и значение
            assert (
                "alert-success" in field_classes
            ), f"❌ Поле {field_name} не имеет класса alert-success"
            assert (
                actual_text == expected_value
            ), f"❌ Поле {field_name}: ожидалось '{expected_value}', но найдено '{actual_text}'"

            print(
                f"✅ Поле {field_name} заменено на div с текстом '{actual_text}' и зелёной подсветкой."
            )
        except Exception as e:
            print(f"❌ Ошибка при проверке поля {field_name}: {e}")
            driver.save_screenshot(f"field_{field_name}_error.png")
            raise

    print("\n🎉 ТЕСТ УСПЕШНО ПРОЙДЕН!")
    print("✅ Все требования задачи выполнены!")
