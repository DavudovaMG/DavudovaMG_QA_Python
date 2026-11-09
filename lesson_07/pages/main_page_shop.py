from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    # BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    # BOLT_T_SHIRT_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    # ONESIE_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_container")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def main_shop(self, data_test_value: str):
        # Добавление товаров в корзину
        locator = (By.XPATH, f"//button[@data-test='{data_test_value}']")
        btn = self.wait.until(EC.element_to_be_clickable(locator))
        btn.click()

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(
            (self.CART_LINK))).click()
