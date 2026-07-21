import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    # Инициализация драйвера
    driver = webdriver.Edge()  # Или любой другой браузер
    wait = WebDriverWait(driver, 15)

    
        # 1. Открываем страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # 2.# Правильный и короткий вариант!
        first_name_field = driver.find_element(By.NAME, "firstName")
        last_name_field = driver.find_element(By.NAME, "lastName")
        address_field = driver.find_element(By.NAME, "address")
        email_field = driver.find_element(By.NAME, "email")
        phone_field = driver.find_element(By.NAME, "phone")
        zip_code_field = driver.find_element(By.NAME, "zipCode")
        city_field = driver.find_element(By.NAME, "city")
        country_field = driver.find_element(By.NAME, "country")
        job_title_field = driver.find_element(By.NAME, "jobTitle")
        company_field = driver.find_element(By.NAME, "company")

        submit_button = driver.find_element(By.CSS_SELECTOR, "#submit")

        # Отправляем данные
        first_name_field.send_keys("Иван")
        last_name_field.send_keys("Петров")
        address_field.send_keys("Ленина, 55-3")
        email_field.send_keys("test@skypro.com")
        phone_field.send_keys("+7985899998787")
        
        # Внимание! Поле ZIP Code ОБЯЗАТЕЛЬНОЕ на этой странице.
        # Если его оставить пустым, форма НЕ отправится.
        # Поэтому заполняем его корректным значением.
        zip_code_field.send_keys("12345")  
        city_field.send_keys("Москва")
        country_field.send_keys("Россия")
        job_title_field.send_keys("QA")
        company_field.send_keys("SkyPro")

        # Ждём, пока кнопка станет кликабельной (иногда форма подгружается медленно)
        wait.until(EC.element_to_be_clickable(submit_button))
        submit_button.click()

        # 3. Проверки
        # Ожидание того, что страница обновилась после отправки
        # Вместо ожидания изменения URL лучше дождаться появления нового элемента.
        # После успешной отправки появляется заголовок h3 с текстом "Thank you".
        thank_you_header = wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, 'h3'))
        )

        # Проверяем текст заголовка
        assert thank_you_header.text == "Thank you!", f"Заголовок неверный: {thank_you_header.text}"
    
    except Exception as e:
    raise e  # Обязательно перебрасываем исключение дальше, чтобы PyTest знал о падении теста

    # Закрываем браузер при успешном завершении теста
    driver.quit()
