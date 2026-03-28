from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import (
    ChromeDriverManager,
)  # упрощает управление ChromeDriver

# Инициализация драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://uitestingplayground.com/classattr")
    driver.implicitly_wait(3)

    blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")

    blue_button.click()
    print("Синяя кнопка нажата!")

finally:
    # Закрываем браузер после выполнения
    driver.quit()
