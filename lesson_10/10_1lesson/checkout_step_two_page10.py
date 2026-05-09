from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckoutStepTwoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        # Локатор для элемента с итоговой суммой
        self.total_price_locator = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Получение итоговой суммы")
    def get_total_price(self) -> str:
        """
        Получает текст с итоговой суммой заказа.

        Returns:
            str: Текст с итоговой суммой (например, "Total: $43.18")
        """
        total_element = self.wait.until(
            EC.visibility_of_element_located(self.total_price_locator)
        )
        return total_element.text.strip()
