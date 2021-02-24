from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math
import os
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    cond = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


    x_element_find = browser.find_element_by_id("input_value")
    x = x_element_find.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    # Отправляем заполненную форму
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element_by_id("solve")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()