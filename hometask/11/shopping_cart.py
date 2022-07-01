class ShoppingCart(object):

    def __init__(self, browser):
        self.browser = browser

    def open_shopping_cart(self):
        self.browser.click_element("#top-links > ul > li:nth-child(4) > a > i")

    def products_name(self):
        return self.browser.compare_text("#content > form > div > table > tbody > tr > td:nth-child(2) > a")