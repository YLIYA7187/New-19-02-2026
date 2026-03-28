from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    driver.get("http://the-internet.herokuapp.com/login")
    driver.implicitly_wait(5)

    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")
    print("Введено имя пользователя: tomsmith")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    print("Введён пароль: SuperSecretPassword!")

    # Кнопка <i class="fa fa-2x fa-sign-in"> Login</i>
    login_button = driver.find_element(By.CSS_SELECTOR, "button i.fa-sign-in")
    login_button.click()
    print("Нажата кнопка Login")

    success_message = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "flash"))
    )
    message_text = success_message.text.strip()
    print(f"Текст с зелёной плашки: {message_text}")

    # clean_message = message_text.replace("×", "").replace("\n", " ").strip()

    # print(f"Текст с зелёной плашки: {clean_message}")

finally:
    driver.quit()
    print("Браузер закрыт")
