from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 30)
    # Проверка видимости и ввод user-name"
    username_input = wait.until(EC.visibility_of_element_located(
        (By.ID, "user-name")))
    # Проверка видимости и ввод пароля
    password_input = driver.find_element(
        By.CSS_SELECTOR, "input[data-test='password']")
    # Поиск и нажатие кнопки Login
    login_btn = driver.find_element(By.ID, "login-button")

    username_input.clear()
    username_input.send_keys("standard_user")
    password_input.clear()
    password_input.send_keys("secret_sauce")
    login_btn.click()
    driver.save_screenshot("lesson_06K/screenshots/login.png")

    # Добавление товаров в корзину
    sl_backpack_btn = wait.until(EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-backpack")))
    sl_bolt_t_shirt_btn = wait.until(EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")))
    sl_onesie_btn = wait.until(EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-onesie")))
    sl_backpack_btn.click()
    sl_bolt_t_shirt_btn.click()
    sl_onesie_btn.click()
    driver.save_screenshot("lesson_06K/screenshots/add_cart.png")
    # Перейти в корзину https://www.saucedemo.com/cart.html
    cart_link = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".shopping_cart_container")))
    cart_link.click()
    wait.until(EC.url_contains("/cart.html"))
    # Нажмите на кнопку Checkout
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    # Заполните форму своими данными в форме checkout_info
    # имя
    first_name = wait.until(
         EC.visibility_of_element_located((By.ID, "first-name")))
    first_name.send_keys("Мария")
    # фамилия
    last_name = wait.until(
         EC.visibility_of_element_located((By.ID, "last-name")))
    last_name.send_keys("Давудова")
    # почтовый индекс
    postal_code = wait.until(
         EC.visibility_of_element_located((By.ID, "postal-code")))
    postal_code.send_keys("445042")  # Твой почтовый индекс
    driver.save_screenshot("lesson_06K/screenshots/checkout_info.png")
    # Нажмите кнопку Continue
    wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()
    driver.save_screenshot("lesson_06K/screenshots/Continue.png")
    # Прочитайте со страницы итоговую стоимость (Total)
    total_element = wait.until(
         EC.visibility_of_element_located(
             (By.CSS_SELECTOR, ".summary_total_label")))
    driver.save_screenshot("lesson_06K/screenshots/Total_1.png")
    # ВАЖНО: сохраняем текст в переменную ДО закрытия браузера
    total_text = total_element.text.strip()
    print(f"Текст сохранён в переменную: {total_text!r}")
    # Закройте браузер
    driver.quit()
    # Проверьте, что итоговая сумма равна $58.29
    expected = "Total: $58.29"
    assert total_text == expected, (
        f"Ожидалось '{expected}', но получено: '{total_text}'")
    print("Тест пройден: итоговая сумма верна.")
