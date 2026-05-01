from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.checkout_button_locator = (By.ID, "checkout")

    def checkout(self):
        checkout_button = self.wait.until(
            EC.element_to_be_clickable(self.checkout_button_locator)
        )
        checkout_button.click()
