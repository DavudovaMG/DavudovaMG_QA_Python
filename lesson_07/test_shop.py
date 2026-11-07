import pytest
from selenium import webdriver
from pages.login_page_shop import LoginPage
from pages.main_page_shop import MainPage
from pages.cart_page_shop import CartPage
from pages.order_placement_page_shop import OrderPlacementPage


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_shop("standard_user", "secret_sauce")


def test_main(driver):
    main_page = MainPage(driver)
    main_page.main_shop("add-to-cart-sauce-labs-backpack")
    main_page.main_shop("add-to-cart-sauce-labs-bolt-t-shirt")
    main_page.main_shop("add-to-cart-sauce-labs-onesie")
    main_page.go_to_cart()


def test_cart(driver):
    cart_page = CartPage(driver)
    # Сюда кладём только то, что реально видно на странице
    expected = [
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Backpack",
        "Sauce Labs Onesie"
    ]
    cart_page.cart_content(expected)
    cart_page.checkout()


def test_order_placement(driver):
    order_placement = OrderPlacementPage(driver)
    order_placement.fill_form("Мария", "Давудова", "445042")
    total_text = order_placement.order_placement()
    # total_text = order_placement_page_shop.order_placement()
    # Закройте браузер
    driver.quit()
    # Проверьте, что итоговая сумма равна $58.29
    expected = "Total: $58.29"
    assert total_text == expected, (
        f"Ожидалось '{expected}', но получено: '{total_text}'")
    print("Тест пройден: итоговая сумма верна.")
