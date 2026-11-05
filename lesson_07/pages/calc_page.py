from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    DELAY_INPUT = (By.ID, "delay")
    SEVEN_BUTTON = (By.XPATH, "//span[text()='7']")
    PLUS_BUTTON = (By.XPATH, "//span[text()='+']")
    EIGHT_BUTTON = (By.XPATH, "//span[text()='8']")
    EQUAL_BUTTON = (By.XPATH, "//span[text()='=']")
    RESULT_FIELD = (By.CSS_SELECTOR, "div.screen")

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-" \
            "calculator.html"
        self.wait = WebDriverWait(self.driver, 60)

    def open(self):
        self.driver.get(self.url)

    def delay_input(self):
        delay_input = self.wait.until(EC.visibility_of_element_located(
            (self.DELAY_INPUT)))
        delay_input.clear()
        delay_input.send_keys(45)
        self.driver.save_screenshot(
            "lesson_07/screenshots_07/test_calc_1.png")

    def test_calc(self):
        # Нажатие кнопки 7
        self.driver.find_element(*self.SEVEN_BUTTON).click()
        # Нажатие на +
        self.driver.find_element(*self.PLUS_BUTTON).click()
        # Нажатие на 8
        self.driver.find_element(*self.EIGHT_BUTTON).click()
        # Нажатие на =
        self.driver.find_element(*self.EQUAL_BUTTON).click()

    def check_form_result(self):
        # Ждём появления результата в .screen
        self.wait.until(EC.text_to_be_present_in_element(
            (self.RESULT_FIELD), "15"))
        screen = self.driver.find_element(*self.RESULT_FIELD)
        self.driver.save_screenshot(
            "lesson_07/screenshots_07/test_calc_2.png")
        result_text = screen.text.strip()
        return result_text
