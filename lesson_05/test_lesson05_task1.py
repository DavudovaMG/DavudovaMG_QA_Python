from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online")
    # Сохраняем исходный URL
    original_url = driver.current_url
    # Находим и кликаем на ссылку HTML Form
    driver.find_element(By.LINK_TEXT, "HTML Form").click()

    # Проверяем, что URL изменился на /forms/post
    assert driver.current_url.endswith("/forms/post")

    # Возвращаемся назад
    driver.back()

    # Проверяем, что вернулись на исходный URL
    assert driver.current_url == original_url
    driver.quit()
