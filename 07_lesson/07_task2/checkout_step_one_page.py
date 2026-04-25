from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutStepOnePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.continue_button_locator = (By.ID, "continue")
        self.input_field_locator_template = (By.ID, "{field_name}")

    def fill_form(self, user_info):
        for field_name, value in user_info.items():
            locator = (
                self.input_field_locator_template[0],
                self.input_field_locator_template[1].format(field_name=field_name),
            )
            field = self.wait.until(EC.presence_of_element_located(locator))
            field.send_keys(value)

    def continue_to_next_step(self):
        continue_button = self.wait.until(
            EC.element_to_be_clickable(self.continue_button_locator)
        )
        continue_button.click()
