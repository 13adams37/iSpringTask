from pages.productPage import ProductPage
from pages.cartPage import CartPage
from pages.loginPage import LoginPage
import pytest

link = "https://www.ozon.ru/product/avtomatizatsiya-testirovaniya-interfeysa-programmirovaniya-prilozheniya-169159321" \
       "/?asb=OKbGwFiafuMPkY5Y0JWU4i1%252FNduGf3Q6hsbxDVkEmn8%253D&asb2" \
       "=p5kPfuP8IXeWtQvr4GT1OiEaDNyozavqbCzx4NxgkBeQ6X-QGozZBH1JTYNhmw46&keywords=%D0%BA%D0%BD%D0%B8%D0%B3%D0%B0+%D0" \
       "%BF%D0%BE+%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8+%D1%82%D0%B5%D1%81" \
       "%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F&sh=qaHnSQAAAA "


@pytest.mark.tc_0001
def test_Case0001(browser):
    browser.get(link)  # step 1
    pp = ProductPage(browser, link)
    pp.AddProductToCart()  # step 2
    details = pp.ProductDetailsAfterAddToCart()
    pp.go_to_cart_page()  # step 3
    cp = CartPage(browser, link)
    cp.CartCheckAllDetails(details)


@pytest.mark.tc_0002
def test_Case0002(browser):
    browser.get(link)  # step 1
    pp = ProductPage(browser, link)
    pp.AddProductToCart()  # step 2
    pp.go_to_cart_page()  # step 3
    cp = CartPage(browser, link)
    cp.CartDeleteProduct()  # step 4
    cp.CartEmptyCheck()


@pytest.mark.tc_0003
def test_Case0003(browser):
    browser.get(link)  # step 1
    pp = ProductPage(browser, link)
    cp = CartPage(browser, link)
    pp.AddProductToCart()  # step 2
    pp.ProductAmountCheck()
    pp.ProductAddMoreAndCheck()  # step 3
    details = pp.ProductDetailsAfterAddToCart()
    pp.go_to_cart_page()  # step 4
    cp.CartCheckAllDetails(details)
    pp.go_back()  # step 5
    pp.ProductAmountCheck()
    pp.ProductReduceAndCheck()  # step 6
    details = pp.ProductDetailsAfterAddToCart()
    pp.go_to_cart_page()  # step 7
    cp.CartCheckAllDetails(details)


@pytest.mark.tc_0004
def test_Case0004(browser):
    browser.get(link)  # step 1
    pp = ProductPage(browser, link)
    cp = CartPage(browser, link)
    pp.AddProductToCart()  # step 2
    pp.go_to_cart_page()  # step 3
    max_products = cp.GetMaxProducts()
    cp.ChangeProductCount(1)  # step 4
    cp.CartCheckAfterChangeValue()
    cp.ChangeProductCount(5)  # step 5
    cp.CartCheckAfterChangeValue()
    cp.ChangeProductCount(10)  # step 6
    cp.CartCheckAfterChangeValue()
    cp.ChangeProductCount(int(max_products+1))  # step 7
    cp.CartCheckAfterChangeValue()
    cp.ChangeProductCount(int(max_products/2))  # step 8
    cp.CartCheckAfterChangeValue()


@pytest.mark.tc_0005
def test_Case0005(browser):
    browser.get(link)  # step 1
    pp = ProductPage(browser, link)
    cp = CartPage(browser, link)
    lp = LoginPage(browser, link)
    pp.AddProductToCart()  # step 2
    pp.go_to_cart_page()  # step 3
    cp.select_all()  # step 4
    cp.go_to_checkout()
    cp.select_all()  # step 5
    cp.go_to_checkout()  # step 6
    lp.should_be_login_form()


@pytest.mark.xfail(reason="Не отображается скидка на товаре.")
@pytest.mark.tc_0006
def test_Case0006(browser):
    browser.get(link)  # step 1
    pp = ProductPage(browser, link)
    cp = CartPage(browser, link)
    pp.AddProductToCart()  # step 2
    pp.go_to_cart_page()  # step 3
    cp.DiscountCheck()
    max_products = cp.GetMaxProducts()
    cp.ChangeProductCount(49)  # step 4
    cp.DiscountCheck()
    cp.ChangeProductCount(50)  # step 5
    cp.DiscountCheck()
    cp.ChangeProductCount(int(max_products/2))  # step 6
    cp.DiscountCheck()
    cp.ChangeProductCount(max_products)
    cp.DiscountCheck()
