from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CheckoutStepTwoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_total_price(self):
        # Ждем появления элемента с суммой и возвращаем его текст
        total_element = self.wait.until(
            lambda d: d.find_element(By.CSS_SELECTOR, ".summary_total_label")
        )
        return total_element.text
