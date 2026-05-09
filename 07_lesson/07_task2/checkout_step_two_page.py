from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CheckoutStepTwoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        self.total_price_locator = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Получение итоговой суммы")
    def get_total_price(self) -> str:
        total_price_element = self.wait.until(
            EC.presence_of_element_located(self.total_price_locator)
        )
        return total_price_element.text

