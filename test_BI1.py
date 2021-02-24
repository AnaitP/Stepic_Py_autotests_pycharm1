from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture (scope='class', autouse=True)
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('http://ss.dev.bnvt.ru/')


    browser.find_element_by_id("username").send_keys("netrika")
    browser.find_element_by_css_selector("#password").send_keys("netrika")
    browser.find_element_by_css_selector("input.btn").click()
    browser.get('http://ss.dev.bnvt.ru/superset/dashboard/179')
    return browser

class TestDirectedHierAndDD():  # Проверяем иерархию из шапки и значений таблицы и таблицы среза


    def wait_by_css(self, element_locator):
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_locator)))
        return self



    def test_hierDirected1(self, browser):
        # 0+ в графе
        actions = webdriver.ActionChains(browser)
        self.wait_by_css('#slice-container-740 > svg > g:nth-child(4) > circle')
        clickPoint = browser.find_element_by_css_selector('#slice-container-740 > svg > g:nth-child(4) > circle')
        actions.move_to_element(clickPoint).context_click().perform()
        browser.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(2)').click()  # клик по меню
        self.wait_by_css('#slice-container-740 > svg > g:nth-child(4) > circle')
        result = browser.find_element_by_css_selector('#slice-container-740 > svg > g:nth-child(5) > text').text
        print(result)
        assert result == '2', 'Упало при переходе из hierDirected1'  # проверка появившегося поля

    def test_hierDirected2(self, browser):
       #Красногвардейский район в графе
        actions = webdriver.ActionChains(browser)
        self.wait_by_css('#slice-container-740 > svg > g:nth-child(9) > circle')
        clickPoint = browser.find_element_by_css_selector('#slice-container-740 > svg > g:nth-child(9) > circle')
        actions.move_to_element(clickPoint).context_click().perform()
        browser.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(2)').click()  # клик по меню
        self.wait_by_css('#slice-container-740 > svg > g:nth-child(13) > circle')
        result = browser.find_element_by_css_selector('#slice-container-740 > svg > g:nth-child(13) > text').text
        print(result)
        assert result == 'ДГП №68', 'Упало при переходе из hierDirected2'  # проверка появившегося поля

    def test_ddDirected2(self, browser):
        #Красногвардейский район в графе
        actions = webdriver.ActionChains(browser)
        self.wait_by_css('#slice-container-740 > svg > g:nth-child(13) > circle')
        clickPoint = browser.find_element_by_css_selector('#slice-container-740 > svg > g:nth-child(13) > circle')
        actions.move_to_element(clickPoint).context_click().perform()
        browser.find_element_by_css_selector(
            '.d3-context-menu ul li:nth-of-type(4)').click()  # клик по меню
        self.wait_by_css('div:nth-of-type(1) > .slice-cell .slice_container.table '
                         '> .dataTables_wrapper.dt-bootstrap.form-inline.no-footer .dataTables_scrollBody '
                         '> table[role="grid"] > tbody > tr:nth-of-type(1) > td:nth-of-type(1) > .like-pre')
        result = browser.find_element_by_css_selector('div:nth-of-type(1) > .slice-cell .slice_container.table '
                                                          '> .dataTables_wrapper.dt-bootstrap.form-inline.no-footer .'
                                                          'dataTables_scrollBody > table[role="grid"] > tbody > '
                                                          'tr:nth-of-type(1) > td:nth-of-type(1) > .like-pre').text
        result1 = browser.find_element_by_css_selector('div:nth-of-type(1) > .slice-cell .slice_container.table > '
                                                           '.dataTables_wrapper.dt-bootstrap.form-inline.no-footer '
                                                           '.dataTables_scrollBody > table[role="grid"] > tbody > '
                                                            'tr:nth-of-type(2) > td:nth-of-type(2) > .like-pre').text
        result2 = browser.find_element_by_css_selector('div:nth-of-type(1) > .slice-cell .slice_container.table > '
                                                           '.dataTables_wrapper.dt-bootstrap.form-inline.no-footer '
                                                           '.dataTables_scrollBody > table[role="grid"] > tbody > '
                                                           'tr:nth-of-type(3) > td[title="3"] > .like-pre').text
        print(result)
        assert result == 'Красногвардейский район', 'Упало при переходе из hierDirected1'  # проверка появившегося поля
        assert result1 == 'ДГП №68', 'Упало при переходе из hierDirected1'  # проверка появившегося поля
        assert result2 == '3', 'Упало при переходе из hierDirected1'  # проверка появившегося поля


