from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (
        By.CSS_SELECTOR, "input[data-test='password']")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        self.driver.get(self.url)

    def login_shop(self, username, password):
        # Проверка видимости и ввод user-name"
        username_input = self.wait.until(EC.visibility_of_element_located(
            (self.USERNAME_INPUT)))
        # Проверка видимости и ввод пароля
        password_input = self.driver.find_element(*self.PASSWORD_INPUT)
        # Поиск и нажатие кнопки Login
        login_btn = self.driver.find_element(*self.LOGIN_BUTTON)
        username_input.clear()
        username_input.send_keys(username)
        password_input.clear()
        password_input.send_keys(password)
        login_btn.click()
