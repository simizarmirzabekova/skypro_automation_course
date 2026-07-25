from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    TOTAL_AMOUNT = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form_and_continue(self, first_name, last_name, zip_code):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.ZIP_CODE).send_keys(zip_code)
        self.driver.find_element(*self.CONTINUE_BTN).click()

    def get_total_amount(self):
        return self.wait.until(EC.visibility_of_element_located(self.TOTAL_AMOUNT)).text
    