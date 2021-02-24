import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestMainPage():

    def wait_by_css(self, browser, element_locator):
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_locator)))
        return self

    def wait_by_xpath(self, browser, element_locator):
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, element_locator)))
        return self

    def test_roles(self, browser, login):
        browser.get("http://r78-rc-superset.zdrav.netrika.ru/users/list/")
        name = browser.find_element_by_css_selector('body > div.container > div > div.panel.panel-primary > div.panel-body.list-container > div.table-responsive > table > thead > tr > th:nth-child(4)').text
        print("name")
        time.sleep(10)