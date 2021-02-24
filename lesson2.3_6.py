from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


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
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()