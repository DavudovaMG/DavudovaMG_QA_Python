from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def checkout(self):
        self.wait.until(EC.element_to_be_clickable(
             (self.CHECKOUT_BUTTON))).click()

    def cart_content(self, expected_items):
        # Проверка содержимого корзины
        # Ждём, пока появятся товары в корзине
        cart_items = self.wait.until(
            EC.presence_of_all_elements_located((self.CART_ITEMS)))

        actual_texts = [item.text for item in cart_items]

        for expected in expected_items:
            # Ищем, есть ли ожидаемый текст в каком‑либо элементе корзины
            if not any(expected in text for text in actual_texts):
                raise AssertionError(
                    f"Товар '{expected}' отсутствует в корзине")
