import pytest
from selenium import webdriver
from pages.page_shop import PageShop


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop_page(driver):
    page_shop = PageShop(driver)
    page_shop.open()
    page_shop.authorization_shop()
    page_shop.main_shop()
    page_shop.cart_shop()
    total_text = page_shop.order_placement()
    # Закройте браузер
    driver.quit()
    # Проверьте, что итоговая сумма равна $58.29
    expected = "Total: $58.29"
    assert total_text == expected, (
        f"Ожидалось '{expected}', но получено: '{total_text}'")
    print("Тест пройден: итоговая сумма верна.")
