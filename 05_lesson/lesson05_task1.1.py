from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoAlertPresentException

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://uitestingplayground.com/classattr")
    driver.implicitly_wait(3)

    blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    blue_button.click()
    print("Синяя кнопка нажата!")

    wait = WebDriverWait(driver, 5)
    alert = wait.until(EC.alert_is_present())

    alert_text = alert.text
    print(f"Текст алерта: {alert_text}")

    # Подтверждаем алерт (эквивалент нажатию "OK")
    alert.accept()

finally:
    driver.quit()
