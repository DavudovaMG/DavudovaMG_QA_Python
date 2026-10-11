from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")
    original_url = driver.current_url
    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Мария")

    driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]"
                        ).click()
    assert driver.current_url != original_url
    driver.quit()
