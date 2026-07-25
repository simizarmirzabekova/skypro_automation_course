from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainShopPage:
    BACKPACK_ADD_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOLT_TSHIRT_ADD_BTN = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_ADD_BTN = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack(self):
        self.wait.until(EC.element_to_be_clickable(self.BACKPACK_ADD_BTN)).click()

    def add_bolt_tshirt(self):
        self.driver.find_element(*self.BOLT_TSHIRT_ADD_BTN).click()

    def add_onesie(self):
        self.driver.find_element(*self.ONESIE_ADD_BTN).click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
        