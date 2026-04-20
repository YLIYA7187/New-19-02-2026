import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    """Фикстура для управления браузером Firefox."""
    print("\n🚀 Запускаю браузер Firefox...")
    # Убедитесь, что у вас установлен geckodriver и он доступен в PATH
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    print("🔚 Закрываю браузер...")
    driver.quit()


def test_shopping_cart_flow(driver):
    """
    Тестовый сценарий:
    1. Открыть сайт.
    2. Авторизоваться.
    3. Добавить 3 товара в корзину.
    4. Перейти в корзину и оформить заказ.
    5. Проверить итоговую сумму.
    """
    wait = WebDriverWait(driver, 15)

    # 1. Открытие сайта
    print("Открываю сайт https://www.saucedemo.com")
    driver.get("https://www.saucedemo.com")

    # 2. Авторизация
    print("Вводим логин и пароль...")

    # Находим поля и вводим данные
    username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    password_field = driver.find_element(By.ID, "password")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")

    # Нажимаем кнопку Login
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # Ожидаем загрузки главной страницы (инвентории)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))

    # 3. Добавление товаров в корзину
    print("Добавляем товары в корзину...")

    # Список ID кнопок для нужных товаров
    items_to_add = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie",
    ]

    for item_id in items_to_add:
        # Находим кнопку по data-test атрибуту и нажимаем
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f'button[data-test="{item_id}"]')
            )
        )
        add_to_cart_button.click()

        # Небольшая проверка, что товар добавлен (значок корзины обновился)
        cart_badge = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        assert cart_badge.text == str(
            items_to_add.index(item_id) + 1
        ), "Товар не добавился в корзину"

    # 4. Переход в корзину и оформление заказа
    print("Переходим в корзину и оформляем заказ...")

    # Нажимаем на иконку корзины
    cart_link = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    )
    cart_link.click()

    # Нажимаем кнопку CHECKOUT
    checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_button.click()

    # 5. Заполнение формы доставки
    print("Заполняем форму доставки...")

    checkout_info = {
        "first-name": "Юлия",
        "last-name": "Бельчук",
        "postal-code": "12345",
        # Остальные поля (город, страна) не обязательны для продолжения по ТЗ
        # "city": "Москва",
        # "state": "",
        # "country": ""
    }

    for field_name, value in checkout_info.items():
        field_element = wait.until(EC.presence_of_element_located((By.ID, field_name)))
        field_element.send_keys(value)

    # Нажимаем кнопку CONTINUE
    continue_button = wait.until(EC.element_to_be_clickable((By.ID, "continue")))
    continue_button.click()

    # 6. Проверка итоговой суммы
    print("Проверяем итоговую сумму...")

    # Ожидаем загрузки страницы подтверждения заказа (где есть сумма)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))

    # Находим элемент с суммой (он содержит текст 'Total: $58.29')
    total_element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_total_label"))
    )

    total_text = total_element.text

    # Проверяем, что сумма совпадает с ожидаемой
    assert (
        total_text == "Total: $58.29"
    ), f"❌ Ошибка! Ожидалась сумма $58.29, но найдена {total_text}"

    print(f"✅ УСПЕХ! Итоговая сумма подтверждена: {total_text}")
