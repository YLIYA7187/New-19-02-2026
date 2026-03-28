from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://uitestingplayground.com/dynamicid")
    driver.implicitly_wait(5)

    # 2. Находим синюю кнопку с динамическим ID
    # Используем CSS-селектор по классам (btn + btn-primary), так как ID меняется
    blue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )

    blue_button.click()
    print("Синяя кнопка нажата!")

finally:
    # Закрываем браузер
    driver.quit()
