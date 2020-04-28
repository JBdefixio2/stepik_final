from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CLASS_NAME, "login_form")
    REGISTER_FORM = (By.CLASS_NAME, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alertinner strong")
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, "div.alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")
