from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPlacementPage:

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINAL_COST = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def fill_form(self, first_name: str, last_name: str, postal_code: str):
        # Заполните форму своими данными в форме checkout_info
        # имя
        first_name_input = self.wait.until(
            EC.visibility_of_element_located((self.FIRST_NAME)))
        first_name_input.send_keys(first_name)
        # фамилия
        last_name_input = self.wait.until(
            EC.visibility_of_element_located((self.LAST_NAME)))
        last_name_input.send_keys(last_name)
        # почтовый индекс
        postal_code_input = self.wait.until(
            EC.visibility_of_element_located((self.POSTAL_CODE)))
        postal_code_input.send_keys(postal_code)
        # Нажмите кнопку Continue
        self.wait.until(EC.element_to_be_clickable(
            (self.CONTINUE_BUTTON))).click()

    def order_placement(self):
        # Прочитайте со страницы итоговую стоимость (Total)
        total_element = self.wait.until(
            EC.visibility_of_element_located(
                (self.FINAL_COST)))
        # ВАЖНО: сохраняем текст в переменную ДО закрытия браузера
        total_text = total_element.text.strip()
        return total_text
