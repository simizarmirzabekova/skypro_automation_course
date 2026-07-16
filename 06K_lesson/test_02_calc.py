import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.skipif(
    pytest.config.getoption("--browser") != "chrome",
    reason="Test requires Google Chrome"
)
def test_calculator():
    """Автотест калькулятора"""

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 60) # Увеличено время ожидания до 1 минуты

    try:
        # 1. Открываем страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # 2. Устанавливаем задержку
        delay_input = driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # 3. Нажимаем кнопки
        buttons = {
            "7": driver.find_element(By.XPATH, "//span[text()='7']"),
            "+": driver.find_element(By.XPATH, "//span[text()='+']"),
            "8": driver.find_element(By.XPATH, "//span[text()='8']"),
            "=": driver.find_element(By.XPATH, "//span[text()='=']"),
        }

        for button_text in ["7", "+", "8", "="]:
            buttons[button_text].click()

        # 4. Ждем результата
        result_locator = (By.ID, "result")
        # Используем правильный локатор и метод ожидания
        wait.until(EC.text_to_be_present_in_element(result_locator, "15")) 

        # 5. Проверка
        # Получаем ТЕКСТ элемента (у div нет value)
        result = driver.find_element(*result_locator).text  
        assert result == "15", f"Результат неверен: {result}"
    
    finally:
        # Закрытие браузера должно быть здесь!
        driver.quit()
