from selenium.common.exceptions import NoSuchElementException
from .headerPage import HeaderPage
from .locators import ProductPageLocators
from .locators import HeaderPageLocators
import os
import time


class ProductPage(HeaderPage):
    def ProductAddMoreAndCheck(self):
        self.ProductAddMore()
        self.ProductAmountCheck()

    def ProductReduceAndCheck(self):
        self.ProductReduce()
        self.ProductAmountCheck()

    def AddProductToCart(self):
        self.browser.find_element(*ProductPageLocators.PRODUCT_ADDTOCARTBUTTON).click()

    def GetProductPrice(self):
        amount = self.getNumeric(self.browser.find_element(*ProductPageLocators.PRODUCT_COUNT).text)
        try:
            price = self.getNumeric(self.browser.find_element(*ProductPageLocators.PRODUCT_PRICEWITHOUTDISCOUNT).text)
            return price * amount
        except NoSuchElementException:
            price = self.getNumeric(self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text)
            return price * amount

    def GetSeller(self):
        seller = self.browser.find_element(*ProductPageLocators.PRODUCT_SELLERNAME).text
        if seller == "OZON":
            seller = ""
        return seller

    def ProductDetailsAfterAddToCart(self):
        # Берём детали: картинка, имя, цена (без скидки), продавец, количество.
        product_picture = os.path.basename(
            self.browser.find_element(*ProductPageLocators.PRODUCT_SMALLIMAGEFIRST).get_attribute("src"))
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.GetProductPrice()
        product_seller = self.GetSeller()
        product_amount = self.browser.find_element(
            *HeaderPageLocators.PRODUCT_COUNTONCARTLINK).text  # Берём количество из шапки
        return product_picture, product_name, product_seller, product_amount, product_price

    def ProductAddMore(self):
        self.browser.find_element(*ProductPageLocators.PRODUCT_ADDMOREBUTTON).click()

    def ProductReduce(self):
        self.browser.find_element(*ProductPageLocators.PRODUCT_REDUCEBUTTON).click()

    def ProductAmountCheck(self):
        time.sleep(2)  # Задержка после действий добавления или уменьшения
        product_amount = self.browser.find_element(*ProductPageLocators.PRODUCT_COUNT).text
        header_amount = self.browser.find_element(*HeaderPageLocators.PRODUCT_COUNTONCARTLINK).text
        assert product_amount == header_amount, "Количество товара не совпадает с количеством в корзине."
