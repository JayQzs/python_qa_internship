class MainPage(object):

    def __init__(self, browser):
        self.browser = browser

    def open_url(self):
        self.browser.open_url("http://tutorialsninja.com/demo/")

    def click_the_product_image(self):
        self.browser.click_element("#content > div.row > div:nth-child(2) > div > div.image > a > img")

    def add_to_cart(self):
        self.browser.click_element(
            "#content > div.row > div:nth-child(1) > div > div.button-group > button:nth-child(1)")

    def add_to_wishlist(self):
        self.browser.click_element(
            "#content > div.row > div:nth-child(1) > div > div.button-group > button:nth-child(2) > i")

    def wishlist_assertion(self):
        return self.browser.compare_text("#wishlist-total > span")