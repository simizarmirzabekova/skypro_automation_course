# 07_lesson/calculator_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    # Локаторы
    DELAY_INPUT = (By.ID, "delay")
    BUTTON_7 = (By.XPATH, "//button[text()='7']")
    BUTTON_PLUS = (By.XPATH, "//button[text()='+']")
    BUTTON_8 = (By.XPATH, "//button[text()='8']")
    BUTTON_EQUALS = (By.XPATH, "//button[text()='=']")
    RESULT_OUTPUT = (By.ID, "answer")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60) # Ожидание до 60 секунд из-за задержки калькулятора

    def open(self, url):
        self.driver.get(url)

    def set_delay(self, value):
        delay_input = self.wait.until(EC.visibility_of_element_located(self.DELAY_INPUT))
        delay_input.clear()
        delay_input.send_keys(str(value))

    def click_button(self, locator):
        button = self.wait.until(EC.element_to_be_clickable(locator))
        button.click()

    def get_result_text(self):
        result = self.wait.until(EC.visibility_of_element_located(self.RESULT_OUTPUT))
        return result.text
    