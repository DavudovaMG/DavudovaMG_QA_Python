from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    # Cookie должны быть получены из двух реальных аккаунтов GitFlic
    cookie_user1 = {
        "name": "SESSION",
        "value": "NGE1NGYyYmMtMGQ1Ny00NTA1LTk4Y2EtODAwYzE0MzU1N2Nh",
        "domain": "gitflic.ru",
    }

    cookie_user2 = {
        "name": "SESSION",
        "value": "ZGU0MWI2NjAtNGNhMC00ZGYzLWI3ZmMtNWQ4MzcxZTJiOTJk",
        "domain": "gitflic.ru",
    }

    # 1. Открываем GitFlic
    driver.get("https://gitflic.ru/")

    # 2. Устанавливаем cookie пользователя 1
    driver.add_cookie(cookie_user1)

    # 3. Обновляем страницу
    driver.refresh()

    wait.until(
        lambda d: d.execute_script(
            "return document.readyState"
        ) == "complete"
    )

    # 4. Переходим в профиль пользователя 1
    driver.get("https://gitflic.ru/user/user_1")

    # 5. Сохраняем URL пользователя 1
    url_user1 = driver.current_url
    print("URL пользователя 1:", url_user1)

    # 6. Очищаем cookie
    driver.delete_all_cookies()

    # 7. Возвращаемся на GitFlic
    driver.get("https://gitflic.ru/")

    # 8. Устанавливаем cookie пользователя 2
    driver.add_cookie(cookie_user2)

    # 9. Обновляем страницу
    driver.refresh()

    wait.until(
        lambda d: d.execute_script(
            "return document.readyState"
        ) == "complete"
    )

    # 10. Переходим в профиль пользователя 2
    driver.get("https://gitflic.ru/user/user_2")

    # 11. Сохраняем URL пользователя 2
    url_user2 = driver.current_url
    print("URL пользователя 2:", url_user2)

    # 12. Проверяем различие URL
    assert url_user1 != url_user2, (
        "URL профилей пользователей должны различаться"
    )

    # 13. Закрываем браузер
    driver.quit()
