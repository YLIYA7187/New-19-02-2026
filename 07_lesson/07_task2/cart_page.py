from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        self.checkout_button_locator = (By.ID, "checkout")

    @allure.step("Начало оформления заказа")
    def checkout(self) -> None:
        checkout_button = self.wait.until(
            EC.element_to_be_clickable(self.checkout_button_locator)
        )
        checkout_button.click()
