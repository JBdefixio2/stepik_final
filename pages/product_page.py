import math
from .base_page import BasePage
import time

from selenium.common.exceptions import NoAlertPresentException

from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_add_button(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is missing"

    def should_be_product_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE), "Product price is missing"

    def should_be_product_name(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME), "Product name is missing"

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_the_same_name(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert name == added_name, f"Added product name does not match product name in the basket. Expected {name}, got {added_name}"

    def should_be_the_same_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        added_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text
        assert price == added_price, f"Added product price does nt match product price in the basket. Expected {price}, got {added_price}"

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
