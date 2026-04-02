from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/ajax")
    print("Страница открыта.")

    ajax_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#ajaxButton"))
    )
    ajax_button.click()
    print("Кнопка нажата.")

    message_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
    )

    message_text = message_element.text
    print("Текст из зелёной плашки:", message_text)

finally:
    driver.quit()
    print("Браузер закрыт")
