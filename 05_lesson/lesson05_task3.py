from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    driver.get("http://the-internet.herokuapp.com/inputs")
    driver.implicitly_wait(5)

    input_field = driver.find_element(By.TAG_NAME, "input")

    input_field.send_keys("12345")
    print("Введено: 12345")

    input_field.clear()
    print("Поле очищено")

    input_field.send_keys("54321")
    print("Введено: 54321")

finally:
    driver.quit()
    print("Браузер закрыт")
