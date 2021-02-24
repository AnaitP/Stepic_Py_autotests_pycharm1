from selenium import webdriver
import time
import math



try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)



    x_element_find = browser.find_element_by_tag_name("img")
    x = x_element_find.get_attribute("valuex")


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    # Отправляем заполненную форму
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()