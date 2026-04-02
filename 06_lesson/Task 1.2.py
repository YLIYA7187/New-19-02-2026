from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")
    print("Страница 'Text Input' открыта.")

    input_field = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#newButtonName"))
    )

    input_field.clear()
    input_field.send_keys("SkyPro")
    print("Текст 'SkyPro' введен в поле.")

    # Поиск кнопки (остается без изменений)
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#updatingButton"))
    )
    submit_button.click()
    print("Синяя кнопка нажата.")

    # Получаем текст кнопки ПОСЛЕ нажатия
    updated_button_text = submit_button.text

    print("Текст на кнопке:", updated_button_text)

finally:
    driver.quit()
