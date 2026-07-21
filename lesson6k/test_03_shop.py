import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_shop():
    """Автотест покупки"""

    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)

    
        # Твоё тело теста...
        
    assert total_price == 58.29, f"Сумма неверна: {total_price}"
    
    
        # Теперь этот блок работает корректно! <-- ПЕРЕНЁС СЮДА ИЛИ УБЕРИ ЭТОТ КОММЕНТАРИЙ
    timestamp = int(time.time())
    screenshot_path = os.path.join(variable.driver.screenshot_dir, f"error_{timestamp}.png")
    driver.save_screenshot(screenshot_path)
    print(f"\nСкриншот ошибки сохранён как: ({screenshot_path})")
    raise e  # Перебрасываем исключение дальше, чтобы PyTest знал о падении

    driver.quit()  # Закрываем браузер в конце работы
