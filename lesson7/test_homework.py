import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


@pytest.fixture(scope="function")
def chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()


def test_calculator_page_object(chrome_driver):
    page = CalculatorPage(chrome_driver)
    page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    page.set_delay(45)
    page.click_button(CalculatorPage.BUTTON_7)
    page.click_button(CalculatorPage.BUTTON_PLUS)
    page.click_button(CalculatorPage.BUTTON_8)
    page.click_button(CalculatorPage.BUTTON_EQUALS)
    
    assert page.get_result_text() == "15"


    import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from login_page import LoginPage
from main_shop_page import MainShopPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture(scope="function")
def firefox_driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    yield driver
    driver.quit()


def test_saucedemo_page_object(firefox_driver):
    login_page = LoginPage(firefox_driver)
    shop_page = MainShopPage(firefox_driver)
    cart_page = CartPage(firefox_driver)
    checkout_page = CheckoutPage(firefox_driver)

    firefox_driver.get("https://www.saucedemo.com/")
    
    login_page.login("standard_user", "secret_sauce")
    
    shop_page.add_backpack()
    shop_page.add_bolt_tshirt()
    shop_page.add_onesie()
    
    shop_page.go_to_cart()
    cart_page.proceed_to_checkout()
    
    # Используйте свои реальные данные
    checkout_page.fill_form_and_continue("Иван", "Иванов", "123456")
    
    total_text = checkout_page.get_total_amount()
    assert total_text == "Total: 58.29"
