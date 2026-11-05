import pytest
from selenium import webdriver
from pages.calc_page import CalcPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calc_page(driver):
    calc_page = CalcPage(driver)
    calc_page.open()
    calc_page.delay_input()
    calc_page.test_calc()
    calc_page.check_form_result()
    calc_page.check_form_result()
    result = calc_page.check_form_result()
    assert result == "15", f"Ожидался результат 15, но получено: {result}"
