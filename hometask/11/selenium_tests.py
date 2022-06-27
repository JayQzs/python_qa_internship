from main_page import MainPage
from product_page import ProductPage
from shopping_cart import ShoppingCart

def test_opening_salespage(browser):
    MainPage(browser).open_url()
    MainPage(browser).click_the_product_image()
    assert ProductPage(browser).products_name() == "iPhone"


def test_adding_to_cart(browser):
    MainPage(browser).open_url()
    MainPage(browser).add_to_cart()
    ShoppingCart(browser).open_shopping_cart()
    assert ShoppingCart(browser).products_name() == "MacBook"


def test_adding_to_wishlist(browser):
    MainPage(browser).open_url()
    MainPage(browser).add_to_cart()
    assert MainPage(browser).wishlist_assertion() == "Wish List (1)"