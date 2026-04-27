from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.cart_link_locator = (By.CLASS_NAME, "shopping_cart_link")
        self.item_button_locator_template = (
            By.CSS_SELECTOR,
            f'button[data-test="add-to-cart-{{item_id}}"]',
        )

    def add_items_to_cart(self, item_ids):
        for item_id in item_ids:
            locator = (
                self.item_button_locator_template[0],
                self.item_button_locator_template[1].format(item_id=item_id),
            )
            button = self.wait.until(EC.element_to_be_clickable(locator))
            button.click()

    def go_to_cart(self):
        cart_link = self.wait.until(EC.element_to_be_clickable(self.cart_link_locator))
        cart_link.click()
