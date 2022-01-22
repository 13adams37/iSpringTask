from selenium.webdriver.common.by import By


class HeaderPageLocators:
    BASKET_LINK = (By.XPATH, '//a[@href="/cart"]')
    PRODUCT_COUNTONCARTLINK = (By.XPATH, '(//a[@href="/cart"]/span)[1]')  # Количество товара на кнопке корзины
    COMPANYALERT = (By.XPATH,
                    '//div[@data-widget="alertPopup"]/div/div/div/div/div/div/div/div/div[3]/div/button')  # Окно рекламы для юр лиц


class ProductPageLocators:
    PRODUCT_ADDTOCARTBUTTON = (
        By.XPATH, '(//span[contains(text(), "Добавить в корзину")]/../..)[2]')  # Основная кнопка добавления в корзину
    PRODUCT_NAME = (By.XPATH, '//div[@data-widget="webProductHeading"]/h1')  # Название продукта
    PRODUCT_PRICE = (By.XPATH, '//div[@slot="content"]/div[2]/div/span/span')  # Цена товара
    PRODUCT_PRICEWITHOUTDISCOUNT = (By.XPATH, '//div[@slot="content"]/div[2]/div/span[2]')  # Цена товара без скидки
    PRODUCT_SELLERNAME = (
        By.XPATH, '//div[@data-widget="webCurrentSeller"]/div/div/div/div/div/div/div/a')  # Название продавца продукта
    PRODUCT_COUNT = (By.XPATH,
                     '//div[@data-widget="webSale"]/div/div/div[4]/div/div/div/div/div/div/div[2]/span[2]')  # Количество товара
    PRODUCT_SMALLIMAGEFIRST = (By.XPATH, '//div[@data-index="0"]/div/img')  # Первая уменьшенная картинка товара
    PRODUCT_ADDMOREBUTTON = (
        By.XPATH, '//div[@data-widget="webSale"]/div/div/div[4]/div/div/div/div/div/div/div[2]/span[3]')
    PRODUCT_REDUCEBUTTON = (
        By.XPATH, '//div[@data-widget="webSale"]/div/div/div[4]/div/div/div/div/div/div/div[2]/span[1]')


class CartPageLocators:
    CART_COUNTONCARTNAME = (By.XPATH, '//div[@class="la6"]')  # Счётчик количества товаров в верхнем блоке
    CART_COUNTONFINAL = (By.XPATH, '(//span[@class="a6t"])[1]')  # Счётчик количества товарв к оформлению
    CART_COUNTANDWEIGHT = (By.XPATH, '//span[@class="t9a"]')  # Количество и вес корзины

    CART_SELECTALL = (By.XPATH, '//div[@data-widget="controls"]/label')  # Кнопка слекта всех товаров
    CART_PRODUCTSNAME = (By.XPATH, '//a[@class="a6q"]/span')  # Название товаров

    CART_PRICEALLPRODUCTS = (
    By.XPATH, '//section[@data-widget="total"]/div[2]/div[2]/div[2]/span')  # Полная стоимость товаров без скидки
    CART_PRICEALLDISCOUNT = (
    By.XPATH, '//section[@data-widget="total"]/div[2]/div[3]/div[2]/span/span')  # Общая скидка товаров в корзине
    CART_FULLPRICE = (By.XPATH, '//section[@data-widget="total"]/div[2]/div[last()]/span[2]')  # Общая стоимость корзины
    CART_GOTOCHECKOUT = (By.XPATH, '//section[@data-widget="total"]/div[1]/div/button')  # Кнопка перехода к оформлению
    CART_REMOVEITEM = (By.XPATH, '//span[@class="a4q" and contains(text(), "Удалить")]')  # Удалить отдельный товар
    CART_REMOVECONFIRM = (By.XPATH, '//div[contains(text(), "Удаление товаров")]/../div[last()]/div/button')
    CART_PRODUCTSIMG = (By.XPATH, '//div[@data-widget="split"]/div[2]/a/div/img')  # Отображаемая картинка товаров
    CART_PRODUCTSELLERANDWEIGHT = (By.XPATH, '//div[@class="q6a"]')  # Продавец товара

    CART_PRODUCTPRICE = (By.XPATH, '//div[contains(@style, "15px;") and contains(@style, "bold;")]/span')
    CART_PRODUCTPRICEWITHOUTDISCOUNT = (By.XPATH, '//div[contains(@style, "line-through;")]/span')
    CART_PRODUCTDISCOUNT = (By.XPATH, '//div[@data-widget="split"]/div[2]/div[3]/div[2]/div[2]')

    CART_EMPTY = (By.XPATH, '//h1[contains(text(), "Корзина пуста")]')

    CART_COUNTCOMBOBOX = (By.XPATH, '//input[@role="combobox"]')
    CART_INPUTNUMBER = (By.XPATH, '//input[@type="number"]')
    CART_INPUTNUMBERTEXT = (By.XPATH, '//div[@role="listbox"]/div/div/div')
    CART_COUNTLIST = (By.XPATH, '//div[@role="option" and @title="10+"]')


class LoginPageLocators:
    auth_frame = (By.XPATH, '//iframe[@id="authFrame"]')
