from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from .locators import CartPageLocators
from .locators import HeaderPageLocators
from .headerPage import HeaderPage
import os
import re
import time


class CartPage(HeaderPage):
    def CartCheckAllDetails(self, details):
        self.CartProductPictureCheck(details[0])
        self.CartProductNameCheck(details[1])
        self.CartProductSellerCheck(details[2])
        self.CartProductAmountCheck(details[3])
        self.CartProductPriceCheck(details[4])
        self.CartFullPriceCheck()

    def CartCheckAfterChangeValue(self):
        self.PriceCartEval()
        self.CartProductAmountCheck(self.browser.find_element(*CartPageLocators.CART_INPUTNUMBERTEXT).text)

    def CartProductPictureCheck(self, picture):
        # чек картинок
        assert picture == os.path.basename(
            self.browser.find_element(*CartPageLocators.CART_PRODUCTSIMG).get_attribute("src")), "Картинки отличаются!"

    def CartProductNameCheck(self, name):
        # чек названия товара
        assert name == self.browser.find_element(
            *CartPageLocators.CART_PRODUCTSNAME).text, "Имя товара не соответсвует имени в корзине."

    def CartProductSellerCheck(self, seller):
        # чек продавца
        assert seller in self.browser.find_element(
            *CartPageLocators.CART_PRODUCTSELLERANDWEIGHT).text, "Продавец в корзине отличается."

    def CartProductAmountCheck(self, amount):
        # чек всех счётчиков товара
        header_count = self.browser.find_element(*HeaderPageLocators.PRODUCT_COUNTONCARTLINK).text
        cart_count_on_name = self.browser.find_element(*CartPageLocators.CART_COUNTONCARTNAME).text
        cart_count_final = self.getNumeric(self.browser.find_element(*CartPageLocators.CART_COUNTONFINAL).text)
        cart_count = re.match(r'^.*(?:•)', self.browser.find_element(*CartPageLocators.CART_COUNTANDWEIGHT).text)
        assert amount == header_count == cart_count_on_name == str(cart_count_final) == str(
            self.getNumeric(cart_count.group(
                0))), "Счётчики товаров в корзине не одинаковые."

    def CartProductPriceCheck(self, price):
        # чек стоимости товара
        try:
            final_price = self.browser.find_element(*CartPageLocators.CART_PRODUCTPRICEWITHOUTDISCOUNT).text
            assert price == self.getNumeric(
                final_price), f"Товар со скидкой. Старая стоимость не совпадает. {price} == {self.getNumeric(final_price)}"
        except NoSuchElementException:
            assert price == self.getNumeric(self.browser.find_element(
                *CartPageLocators.CART_PRODUCTPRICE).text), "Товар без скидок. Стоимость не совпадает"

    def CartFullPriceCheck(self):
        # Стоимость корзины к оформлению
        items_price = self.getNumeric(self.browser.find_element(*CartPageLocators.CART_PRICEALLPRODUCTS).text)
        full_price = self.getNumeric(self.browser.find_element(*CartPageLocators.CART_FULLPRICE).text)
        try:
            price_with_discount = items_price - self.getNumeric(
                self.browser.find_element(*CartPageLocators.CART_PRICEALLDISCOUNT).text)
            assert price_with_discount == full_price, "Корзина со скидкой. Цена со скидкой не совпадает."
        except NoSuchElementException:
            assert items_price == full_price, "Корзина без скидок. Цена не совпадает."

    def CartDeleteProduct(self):
        self.browser.find_element(*CartPageLocators.CART_REMOVEITEM).click()
        self.browser.find_element(*CartPageLocators.CART_REMOVECONFIRM).click()

    def CartEmptyCheck(self):
        assert self.is_element_present(*CartPageLocators.CART_EMPTY), "В корзине остались товары!"

    def ChangeProductCount(self, value):
        self.browser.find_element(*CartPageLocators.CART_COUNTCOMBOBOX).click()
        self.browser.find_element(*CartPageLocators.CART_COUNTLIST).click()
        self.browser.find_element(*CartPageLocators.CART_INPUTNUMBER).send_keys(Keys.CONTROL + "a")  # Выделим всё
        self.browser.find_element(*CartPageLocators.CART_INPUTNUMBER).send_keys(Keys.DELETE)  # Очистим
        self.browser.find_element(*CartPageLocators.CART_INPUTNUMBER).send_keys(value)
        self.browser.find_element(*CartPageLocators.CART_PRODUCTPRICE).click()  # обновление списка
        time.sleep(3)  # Задержка после изменения количества

    def GetMaxProducts(self):
        self.browser.find_element(*CartPageLocators.CART_COUNTCOMBOBOX).click()
        self.browser.find_element(*CartPageLocators.CART_COUNTLIST).click()
        max_products = self.getNumeric(
            self.browser.find_element(*CartPageLocators.CART_INPUTNUMBER).get_attribute("max"))
        self.browser.find_element(*CartPageLocators.CART_INPUTNUMBER).send_keys(Keys.ENTER)
        self.browser.find_element(*CartPageLocators.CART_PRODUCTPRICE).click()  # обновление списка
        return max_products

    def PriceCartEval(self):
        self.CartFullPriceCheck()
        try:
            old_price = self.getNumeric(
                self.browser.find_element(*CartPageLocators.CART_PRODUCTPRICEWITHOUTDISCOUNT).text)
            assert old_price == self.getNumeric(self.browser.find_element(*CartPageLocators.CART_PRICEALLPRODUCTS).text)
        except NoSuchElementException:
            product_price = self.getNumeric(self.browser.find_element(*CartPageLocators.CART_PRODUCTPRICE).text)
            assert product_price == self.getNumeric(self.browser.find_element(*CartPageLocators.CART_FULLPRICE).text)

    def go_to_checkout(self):
        self.browser.find_element(*CartPageLocators.CART_GOTOCHECKOUT).click()

    def select_all(self):
        self.browser.find_element(*CartPageLocators.CART_SELECTALL).click()
        time.sleep(1)  # Необходимое ожидание

    def DiscountCheck(self):
        product_discount = self.getNumeric(self.browser.find_element(*CartPageLocators.CART_PRODUCTDISCOUNT).text)
        cart_discount = self.getNumeric(self.browser.find_element(*CartPageLocators.CART_PRICEALLDISCOUNT).text)
        assert product_discount == cart_discount, "Скидка на товаре, и общая скидка отличаются."

    """
    def DiscountCheck(self):
        product_discount = ""
        cart_discount = ""
        try:
            product_discount = self.getNumeric(self.browser.find_element(*CartPageLocators.CART_PRODUCTDISCOUNT).text)
        except NoSuchElementException:
            pass
        try:
            cart_discount = self.getNumeric(self.browser.find_element(*CartPageLocators.CART_PRICEALLDISCOUNT).text)
        except NoSuchElementException:
            pass
        assert product_discount == cart_discount, "Скидка на товаре, и общая скидка отличаются."
    """
