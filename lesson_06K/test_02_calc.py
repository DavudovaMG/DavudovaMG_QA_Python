from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    wait = WebDriverWait(driver, 60)
    delay_input = wait.until(EC.visibility_of_element_located(
        (By.ID, "delay")))
    delay_input.clear()
    delay_input.send_keys(45)
    driver.save_screenshot("lesson_06K/screenshots/test_calc_screen2.png")
    # Нажатие кнопки 7
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    # Нажатие на +
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    # Нажатие на 8
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    # Нажатие на =
    driver.find_element(By.XPATH, "//span[text()='=']").click()
    # Ждём появления результата в .screen
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                                                 "div.screen"), "15"))
    screen = driver.find_element(By.CSS_SELECTOR, "div.screen")
    driver.save_screenshot("lesson_06K/screenshots/test_calc_screen3.png")
    result_text = screen.text.strip()
    assert result_text == "15",  f"Ожидался 15, но получено: {result_text}"

    print("Тест пройден!")
    driver.quit()
