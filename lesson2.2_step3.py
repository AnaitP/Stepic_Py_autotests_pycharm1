from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select



try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)



    x_find = browser.find_element_by_id("num1")
    x = x_find.text
    y_find = browser.find_element_by_id("num2")
    y = y_find.text
    z = int(x) + int(y)
    z_str=str(z)
    # Отправляем заполненную форму
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(z_str)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()