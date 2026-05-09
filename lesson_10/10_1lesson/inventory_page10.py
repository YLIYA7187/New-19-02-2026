from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step("Добавление товара '{item_key}' в корзину")
    def add_item_to_cart(self, item_key: str) -> None:
        # Используем data-test атрибут для точного поиска кнопки
        add_to_cart_locator = (
            By.CSS_SELECTOR,
            f"button[data-test='add-to-cart-{item_key}']",
        )
        try:
            add_button = self.wait.until(
                EC.element_to_be_clickable(add_to_cart_locator)
            )
            add_button.click()
            print(f"Товар {item_key} добавлен в корзину")
        except Exception as e:
            # Добавляем скриншот при ошибке
            self.driver.save_screenshot(f"error_adding_{item_key}.png")
            print(f"Ошибка при добавлении товара {item_key}: {e}")
            raise

    def add_items_to_cart(self, items: list) -> None:
        for item in items:
            self.add_item_to_cart(item)

    @allure.step("Получение цены товара '{item_key}'")
    def get_item_price(self, item_key: str) -> float:
        price_locator = (
            By.XPATH,
            f"//button[@data-test='add-to-cart-{item_key}']/ancestor::div[@class='inventory_item']//div[@class='inventory_item_price']",
        )
        price_element = self.wait.until(EC.visibility_of_element_located(price_locator))
        price_text = price_element.text.strip().replace("$", "")
        return float(price_text)

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        cart_icon = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_icon.click()
