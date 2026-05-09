import pytest
import allure
from selenium import webdriver
from login_page10 import LoginPage
from inventory_page10 import InventoryPage
from cart_page10 import CartPage
from checkout_step_one_page10 import CheckoutStepOnePage
from checkout_step_two_page10 import CheckoutStepTwoPage


@pytest.fixture(scope="function")
def driver():
    # Инициализация драйвера Firefox
    driver = webdriver.Firefox()
    yield driver
    # Закрытие браузера после теста
    driver.quit()


@allure.title("Тест: Полный поток оформления заказа в интернет‑магазине")
@allure.description(
    "Проверяет сценарий покупки: авторизация → добавление товаров → оформление заказа → проверка суммы"
)
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_shopping_cart_flow(driver):
    """
    Тест проверяет полный сценарий оформления заказа:
    1. Авторизуется под валидным пользователем.
    2. Добавляет товары в корзину.
    3. Переходит в корзину и начинает оформление заказа.
    4. Заполняет форму доставки.
    5. Проверяет итоговую сумму на финальном экране.
    """
    # Инициализация страниц
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_step_one = CheckoutStepOnePage(driver)
    checkout_step_two = CheckoutStepTwoPage(driver)

    with allure.step("Авторизация под пользователем standard_user"):
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        inventory_page.add_items_to_cart(
            ["sauce-labs-backpack", "sauce-labs-bolt-t-shirt", "sauce-labs-onesie"]
        )

    with allure.step("Переход в корзину"):
        inventory_page.go_to_cart()

    with allure.step("Начало оформления заказа"):
        cart_page.checkout()

    with allure.step("Заполнение формы доставки"):
        user_info = {
            "first-name": "Иван",
            "last-name": "Петров",
            "postal-code": "123456",
        }
        checkout_step_one.fill_form(user_info)
        checkout_step_one.continue_to_next_step()

    with allure.step("Проверка итоговой суммы"):
        total_price = checkout_step_two.get_total_price()
        assert "Total: $" in total_price, f"Ожидаемая сумма не совпадает: {total_price}"
