from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        self.cart_link_locator = (By.CLASS_NAME, "shopping_cart_link")
        # Локатор кнопки добавления товара — шаблон CSS-селектора
        self.add_to_cart_button_template = "button[data-test='add-to-cart-{}']"

    @allure.step("Добавление товаров в корзину: {item_ids}")
    def add_items_to_cart(self, item_ids: list) -> None:
        for item_id in item_ids:
            button_locator = (
                By.CSS_SELECTOR,
                self.add_to_cart_button_template.format(item_id)
            )
            add_button = self.wait.until(
                EC.element_to_be_clickable(button_locator)
            )
            add_button.click()
            print(f"Товар {item_id} добавлен в корзину")

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        cart_link = self.wait.until(
            EC.element_to_be_clickable(self.cart_link_locator)
        )
        cart_link.click()
