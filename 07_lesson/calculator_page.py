# calculator_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input_locator = (By.ID, "delay")
        self.button_locator_template = (
            By.XPATH,
            f"//span[contains(text(), '{{text}}')]",
        )
        self.result_locator = (By.CSS_SELECTOR, ".screen")

    def set_delay(self, seconds):
        delay_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.delay_input_locator)
        )
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, button_text):
        locator = (
            self.button_locator_template[0],
            self.button_locator_template[1].format(text=button_text),
        )
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        button.click()

    def get_result(self):
        result_element = WebDriverWait(self.driver, 70).until(
            EC.presence_of_element_located(self.result_locator)
        )
        # Ждём появления текста "15"
        WebDriverWait(self.driver, 70).until(
            lambda d: d.find_element(*self.result_locator).text == "15"
        )
        return result_element.text
