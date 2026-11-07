from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    DELAY_INPUT = (By.ID, "delay")
    RESULT_FIELD = (By.CSS_SELECTOR, "div.screen")

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-" \
            "calculator.html"
        self.wait = WebDriverWait(self.driver, 60)

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, delay_time):
        delay_field = self.wait.until(EC.visibility_of_element_located(
            (self.DELAY_INPUT)))
        delay_field.clear()
        delay_field.send_keys(delay_time)

    def test_calc(self, button_value: str):
        #  формирование локатора «на лету»
        safe = button_value.replace("'", "\\'")
        locator = self.driver.find_element(
            By.XPATH, f"//span[normalize-space()='{safe}']"
            )
        button = self.wait.until(EC.element_to_be_clickable(locator))
        button.click()

    def check_form_result(self):
        # Ждём появления результата в .screen
        self.wait.until(EC.text_to_be_present_in_element(
            (self.RESULT_FIELD), "15"))
        screen = self.driver.find_element(*self.RESULT_FIELD)
        result_text = screen.text.strip()
        return result_text
