import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Импортируем созданные классы страниц (они в той же папке)
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_step_one_page import CheckoutStepOnePage
from checkout_step_two_page import CheckoutStepTwoPage


@pytest.fixture(scope="function")
def driver():
    """Фикстура для управления браузером Firefox."""
    print("\n Запускаю браузер Firefox...")
    # Убедитесь, что у вас установлен geckodriver и он доступен в PATH
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    print(" Закрываю браузер...")
    driver.quit()


def test_shopping_cart_flow(driver):
    """
    Тестовый сценарий:
    1. Открыть сайт.
    2. Авторизоваться.
    3. Добавить 3 товара в корзину.
    4. Перейти в корзину и оформить заказ.
    5. Заполнить форму доставки.
    6. Проверить итоговую сумму.
    """
    # 1. Открытие сайта и Авторизация (Логика LoginPage)
    print("Открываю сайт https://www.saucedemo.com")
    driver.get("https://www.saucedemo.com")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # 2. Работа с товарами (Логика InventoryPage)
    inventory_page = InventoryPage(driver)

    items_to_add = [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-onesie",
    ]

    print("Добавляем товары в корзину...")
    inventory_page.add_items_to_cart(items_to_add)

    # Переход в корзину (Логика InventoryPage -> CartPage)
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)

    # Оформление заказа (Логика CartPage -> CheckoutStepOnePage)
    print("Переходим в корзину и оформляем заказ...")
    cart_page.checkout()

    checkout_info = {
        "first-name": "Юлия",
        "last-name": "Бельчук",
        "postal-code": "12345",
    }

    checkout_step_one = CheckoutStepOnePage(driver)

    print("Заполняем форму доставки...")
    checkout_step_one.fill_form(checkout_info)
    checkout_step_one.continue_to_next_step()

    # 3. Проверка суммы (Логика CheckoutStepTwoPage + Assertion в тесте)
    print("Проверяем итоговую сумму...")

    checkout_step_two = CheckoutStepTwoPage(driver)

    total_text = checkout_step_two.get_total_price()

    # --- ЭТО ПРОВЕРКА (ASSERT), ОНА ДОЛЖНА БЫТЬ В ТЕСТЕ ---
    assert (
        total_text == "Total: $58.29"
    ), f" Ошибка! Ожидалась сумма $58.29, но найдена {total_text}"

    print(f"УСПЕХ! Итоговая сумма подтверждена: {total_text}")
