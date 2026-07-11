# test_lesson06_task2.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    # URL профилей пользователей. Вы можете найти их после входа через Cookie.
    USER1_PROFILE_URL = "/user/simisar_mirzabekova"  # Пример
    USER2_PROFILE_URL = "/user/test_user"              # Пример

    # ВАШИ РЕАЛЬНЫЕ КУКИ (НЕ ПУБЛИКУЙТЕ!)
    COOKIE_USER1 = {
        "name": "session",
        "value": "Zjg2ZGJiNDMtNGY0Ni00NjlkLTgyMzYtMjhhNmEzZDE3MDVm",
        "domain": ".gitflic.ru",  # Обратите внимание на точку перед доменом
        "path": "/"
    }

    COOKIE_USER2 = {
        "name": "session",
        "value": "YTUzMGNlMWEtMDA0OC00ODVhLTk0ODEtMGQ3MWQ1YWU2YTJk",
        "domain": ".gitflic.ru",
        "path": "/"
    }

    # 1. Заходим на главную страницу
    driver.get("https://gitflic.ru/")

    # 2. Устанавливаем куки пользователя 1
    driver.add_cookie(COOKIE_USER1)
    driver.refresh()  # ОБЯЗАТЕЛЬНО обновляем страницу

    # 3. Переходим на профиль пользователя 1 и сохраняем URL
    driver.get(f"https://gitflic.ru{USER1_PROFILE_URL}")
    user1_url = driver.current_url

    # 4. Выход из системы (очистка куки)
    driver.delete_all_cookies()
    driver.refresh()

    # 5. Авторизация пользователя 2
    driver.add_cookie(COOKIE_USER2)
    driver.refresh()

    # 6. Профиль пользователя 2
    driver.get(f"https://gitflic.ru{USER2_PROFILE_URL}")
    user2_url = driver.current_url

    # 7. Проверено, что URL различаются
    assert user1_url != user2_url, \
        f"УРЛы совпадают: {user1_url} и {user2_url}"

    driver.quit()
