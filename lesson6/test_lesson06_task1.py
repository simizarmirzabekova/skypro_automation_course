# test_lesson06_task1.py

import time  # Для имени файла скриншота
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # 2. Найдите и нажмите на кнопку "Start"
    # Используем CSS-селектор, как было сказано в подсказках.
    start_button = driver.find_element(By.CSS_SELECTOR, "#start button") 
    start_button.click()

    # 3. Дождитесь появления текста "Hello World!"
    # Ждём исчезновения спиннера ИЛИ появления заголовка h4.
    wait = WebDriverWait(driver, 15)
    finish_locator = (By.ID, 'finish')
    wait.until(EC.visibility_of_element_located(finish_locator))
    
    # Получаем текст элемента для проверки.
    hello_text = driver.find_element(*finish_locator).text

    # 4. Сделайте скриншот страницы
    timestamp = int(time.time())  # Уникальное имя файла
    screenshot_path = f"task1_{timestamp}.png"
    driver.save_screenshot(screenshot_path)  # Файл сохранится рядом со скриптом!

    # 5. Проверьте, что появившийся текст равен "Hello World!"
    assert hello_text == "Hello World!", \
        f"Текст не совпадает. Ожидаемый: Hello World!, Фактический: {hello_text}"

    driver.quit()  # Обязательно закрываем браузер
    