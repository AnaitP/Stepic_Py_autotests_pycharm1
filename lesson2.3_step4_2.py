from selenium import webdriver
import time
import math
import os
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element_find = browser.find_element_by_id("input_value")
    x = x_element_find.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    # Отправляем заполненную форму
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()