from selenium.webdriver.common.by import By

class Browser(object):

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def click_element(self, selector, by=By.CSS_SELECTOR):
        return self.driver.find_element(by=by, value=selector).click()

    def compare_text(self, selector, by=By.CSS_SELECTOR):
        return self.driver.find_element(by=by, value=selector).text

    def wait(self, sec):
        self.driver.implicitly_wait(sec)

    def close(self):
        self.driver.quit()
