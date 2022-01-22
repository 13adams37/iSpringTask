from selenium.common.exceptions import NoSuchElementException
from .locators import HeaderPageLocators


class HeaderPage:
    def __init__(self, browser, url, timeout=4):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.browser.maximize_window()

    def open(self):
        self.browser.get(self.url)

    def go_back(self):
        self.browser.execute_script("window.history.go(-1)")

    def go_to_cart_page(self):
        self.browser.find_element(*HeaderPageLocators.BASKET_LINK).click()
        try:
            self.browser.find_element(*HeaderPageLocators.COMPANYALERT).click()
        except NoSuchElementException:
            pass

    def getNumeric(self, string):
        return int(''.join(filter(str.isdigit, string)))

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
