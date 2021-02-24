import pytest
from selenium import webdriver


@pytest.fixture
def setup_class(self):
    self.driver.get('http://ss.dev.bnvt.ru/')
    self.driver.maximize_window()
    self.driver.find_element_by_css_selector("#username").send_keys("netrika")
    self.driver.find_element_by_css_selector("#password").send_keys("netrika")
    self.driver.find_element_by_css_selector("input.btn").click()
    self.driver.get('http://ss.dev.bnvt.ru/superset/dashboard/179')

@pytest.fixture(scope='session')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture
def login(browser):
    browser.get("http://r78-rc-superset.zdrav.netrika.ru/")
    browser.maximize_window()
    browser.find_element_by_css_selector("#username").send_keys("admin")
    browser.find_element_by_css_selector("#password").send_keys("lifeisgood")
    browser.find_element_by_css_selector("input.btn").click()