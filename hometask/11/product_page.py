class ProductPage(object):

    def __init__(self, browser):
        self.browser = browser

    def products_name(self):
        return self.browser.compare_text('#content > div:nth-child(1) > div.col-sm-4 > h1')