from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    wait = WebDriverWait(driver, 10)

    fields_to_fill = [
        {"locator": (By.NAME, "first-name"), "value": "Иван"},
        {"locator": (By.NAME, "last-name"), "value": "Петров"},
        {"locator": (By.NAME, "address"), "value": "Ленина, 55-3"},
        {"locator": (By.CSS_SELECTOR, "input[name='e-mail']"),
         "value": "test@skypro.com"},
        {"locator": (By.CSS_SELECTOR, "input[name='phone']"),
         "value": "+7985899998787"},
        {"locator": (By.CSS_SELECTOR, "input[name='city']"),
         "value": "Москва"},
        {"locator": (By.CSS_SELECTOR, "input[name='country']"),
         "value": "Россия"},
        {"locator": (By.CSS_SELECTOR, "input[name='job-position']"),
         "value": "QA"},
        {"locator": (By.CSS_SELECTOR, "input[name='company']"),
         "value": "SkyPro"},
        ]
    # ЗАПОЛНЕНИЕ ПОЛЕЙ
    for item in fields_to_fill:
        locator, value = item["locator"], item["value"]
        element = wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)
    # Zip code оставляем пустым
    zip_code = driver.find_element(By.NAME, "zip-code")
    zip_code.clear()

    # Нажимаем Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    driver.save_screenshot("lesson_06K/screenshots/full_screen.png")

    # ПРОВЕРКА ОШИБКИ ДЛЯ ZIP-CODE (красный)
    # Ждём, пока элемент появится/станет видимым после валидации
    zip_code_field = wait.until(EC.visibility_of_element_located(
        (By.ID, "zip-code")))
    background_color = zip_code_field.value_of_css_property('background-color')
    assert background_color == 'rgba(248, 215, 218, 1)', "Zip code должен "
    "быть подсвечен красным"

    # expected_color = "rgba(248, 215, 218, 1)"
    # assert background_color == expected_color
    driver.save_screenshot("lesson_06K/screenshots/zip_code_1.png")
    # ПРОВЕРКА ОСТАЛЬНЫХ ПОЛЕЙ, КРОМЕ ZIP-CODE
    fields_locators = [
        (By.ID, "first-name"),
        (By.ID, "last-name"),
        (By.ID, "address"),
        (By.ID, "e-mail"),
        (By.ID, "phone"),
        (By.ID, "city"),
        (By.ID, "country"),
        (By.ID, "job-position"),
        (By.ID, "company"),
    ]
    # 2. Проверяем, что все эти поля видны
    for locator in fields_locators:
        elem = wait.until(EC.visibility_of_element_located(locator))
        background_color = elem.value_of_css_property('background-color')
        assert background_color == 'rgba(209, 231, 221, 1)', "Все поля,"
    "кроме поля 'Zip code' должены быть подсвечены зеленым"
    print("PASS: Zip code красный, остальные поля зеленые.")
    # Закрываем браузер
    driver.quit()
