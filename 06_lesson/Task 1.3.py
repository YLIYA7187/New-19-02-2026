from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    print("Страница открыта.")

    wait = WebDriverWait(driver, 20)

    done_indicator = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.col-12.py-2 > p#text"))
    )

    if done_indicator.text == "Done!":
        print("Появился текст 'Done!'. Загрузка картинок завершена.")

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#award")))

    award_img = driver.find_element(By.CSS_SELECTOR, "#award")
    src_value = award_img.get_attribute("src")

    print(f"Значение атрибута src у картинки: {src_value}")

finally:
    driver.quit()
