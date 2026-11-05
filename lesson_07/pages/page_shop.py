from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageShop:

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (
        By.CSS_SELECTOR, "input[data-test='password']")
    LOGIN_BUTTON = (By.ID, "login-button")

    BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOLT_T_SHIRT_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")

    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_container")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINAL_COST = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.wait = WebDriverWait(self.driver, 60)

    def open(self):
        self.driver.get(self.url)

    def authorization_shop(self):
        # Проверка видимости и ввод user-name"
        username_input = self.wait.until(EC.visibility_of_element_located(
            (self.USERNAME_INPUT)))
        # Проверка видимости и ввод пароля
        password_input = self.driver.find_element(*self.PASSWORD_INPUT)
        # Поиск и нажатие кнопки Login
        login_btn = self.driver.find_element(*self.LOGIN_BUTTON)
        username_input.clear()
        username_input.send_keys("standard_user")
        password_input.clear()
        password_input.send_keys("secret_sauce")
        self.driver.save_screenshot("lesson_07/screenshots_07/login.png")
        login_btn.click()

    def main_shop(self):
        # Добавление товаров в корзину
        sl_backpack_btn = self.wait.until(EC.element_to_be_clickable(
            (self.BACKPACK_BUTTON)))
        sl_bolt_t_shirt_btn = self.wait.until(EC.element_to_be_clickable(
            (self.BOLT_T_SHIRT_BUTTON)))
        sl_onesie_btn = self.wait.until(EC.element_to_be_clickable(
            (self.ONESIE_BUTTON)))
        sl_backpack_btn.click()
        sl_bolt_t_shirt_btn.click()
        sl_onesie_btn.click()
        self.driver.save_screenshot("lesson_07/screenshots_07/add_cart07.png")

    def cart_shop(self):
        # Перейти в корзину "https://www.saucedemo.com/cart.html"
        cart_link = self.wait.until(EC.element_to_be_clickable(
            (self.CART_LINK)))
        cart_link.click()
        self.wait.until(EC.url_contains("/cart.html"))
        self.driver.save_screenshot(
             "lesson_07/screenshots_07/cart_shop.png")
        # Нажмите на кнопку Checkout
        self.wait.until(EC.element_to_be_clickable(
             (self.CHECKOUT_BUTTON))).click()

    def order_placement(self):
        # Заполните форму своими данными в форме checkout_info
        # имя
        first_name = self.wait.until(
            EC.visibility_of_element_located((self.FIRST_NAME)))
        first_name.send_keys("Мария")
        # фамилия
        last_name = self.wait.until(
            EC.visibility_of_element_located((self.LAST_NAME)))
        last_name.send_keys("Давудова")
        # почтовый индекс
        postal_code = self.wait.until(
            EC.visibility_of_element_located((self.POSTAL_CODE)))
        postal_code.send_keys("445042")  # Твой почтовый индекс
        self.driver.save_screenshot(
            "lesson_07/screenshots_07/checkout_info.png")
        # Нажмите кнопку Continue
        self.wait.until(EC.element_to_be_clickable(
            (self.CONTINUE_BUTTON))).click()
        self.driver.save_screenshot("lesson_07/screenshots_07/Continue.png")
        # Прочитайте со страницы итоговую стоимость (Total)
        total_element = self.wait.until(
            EC.visibility_of_element_located(
                (self.FINAL_COST)))
        self.driver.save_screenshot("lesson_07/screenshots_07/Total_1.png")
        # ВАЖНО: сохраняем текст в переменную ДО закрытия браузера
        total_text = total_element.text.strip()
        return total_text
        # print(f"Текст сохранён в переменную: {total_text!r}")
