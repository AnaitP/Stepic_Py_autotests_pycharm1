from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException # в начале файла
from .locators import ProductPageLocators
from selenium import webdriver
import math

class ProductPage(BasePage):

    def add_product_to_backet(self):
        add_to_backet_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BACKET)
        add_to_backet_button.click()

    def solve_quiz_and_get_code(self):
         alert = self.browser.switch_to.alert
         x = alert.text.split(" ")[2]
         answer = str(math.log(abs((12 * math.sin(float(x))))))
         alert.send_keys(answer)
         alert.accept()
         try:
           alert = self.browser.switch_to.alert
           alert_text = alert.text
           print(f"Your code: {alert_text}")
           alert.accept()
         except NoAlertPresentException:
             print("No second alert presented")

    def product_should_be_added(self):
        assert self.is_element_present(*ProductPageLocators.LOGIN_LINK), "Login link is not presented"