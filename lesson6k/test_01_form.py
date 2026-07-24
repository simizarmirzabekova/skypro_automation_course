import time  # Только для создания уникального имени скриншота!
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Импортируем менеджер драйверов для Edge
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def test_form():
    """
    Автотест заполнения формы на странице data-types.html.
    Проверяет подсвечивание обязательных полей красным цветом,
    если они остались незаполненными.
    """

    # Инициализация драйвера (ТРЕБОВАНИЕ ТЗ — Edge)
    driver = webdriver.Edge(
        service=webdriver.EdgeService(EdgeChromiumDriverManager().install())
    )
    
    wait = WebDriverWait(driver, 15)  # Увеличим ожидание до 15 секунд

    # Шаг 1. Открываем страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Шаг 2. Заполняем форму (поиск по атрибуту name)
    first_name_field = driver.find_element(By.NAME, "firstName")  # Иван
    last_name_field = driver.find_element(By.NAME, "lastName")     # Петров
    address_field = driver.find_element(By.NAME, "address")       # Ленина, 55-3
    email_field = driver.find_element(By.NAME, "email")           # test@skypro.com
    phone_field = driver.find_element(By.NAME, "phone")           # +7985899998787
        
    # Zip code оставляем ПУСТЫМ (требование ТЗ). Это обязательное поле!
    zip_code_field = driver.find_element(By.NAME, "zipCode")

    city_field = driver.find_element(By.NAME, "city")             # Москва
    country_field = driver.find_element(By.NAME, "country")      # Россия
    job_title_field = driver.find_element(By.NAME, "jobTitle")   # QA
    company_field = driver.find_element(By.NAME, "company")       # SkyPro

    submit_button = driver.find_element(By.CSS_SELECTOR, "#submit")

    # Отправка данных
    first_name_field.send_keys("Иван")
    last_name_field.send_keys("Петров")
    address_field.send_keys("Ленина, 55-3")
    email_field.send_keys("test@skypro.com")
    phone_field.send_keys("+7985899998787")

    # Оставляем поле ZIP CODE пустым! Оно обязательно к заполнению.

    city_field.send_keys("Москва")
    country_field.send_keys("Россия")
    job_title_field.send_keys("QA")
    company_field.send_keys("SkyPro")

    # Ждём, пока кнопка станет кликабельной (иногда форма подгружается медленно)
    wait.until(EC.element_to_be_clickable(submit_button))
    submit_button.click()

    # Шаг 3. Проверки (assert)

    # Ожидаем, что страница обновилась после отправки
    # После нажатия кнопки появляется заголовок <h3>Thank you!</h3>
    thank_you_header = wait.until(
        EC.visibility_of_element_located((By.TAG_NAME, 'h3'))
    )

    # Проверяем красный фон поля ZIP CODE (оно осталось пустым)
    assert (
            zip_code_field.value_of_css_property("background-color").lower() == "rgba(255, 0, 0, 1)"  
        ), f"Поле ZIP CODE не подсвечено красным"

    # Проверяем зелёный фон остальных полей
    fields_to_check = [
            first_name_field,
            last_name_field,
            address_field,
            email_field,
            phone_field,
            city_field,
            country_field,
            job_title_field,
            company_field,
        ]

    for field in fields_to_check:
            color = field.value_of_css_property("background-color").lower()
            assert color == "rgba(0, 255, 0, 1)", \
                f"Поле {field.tag_name} не зеленое: {color}"

    # Закрываем браузер **в конце работы** (так требует ДЗ)
    driver.quit()
    