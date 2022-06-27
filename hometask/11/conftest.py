import pytest
from selenium import webdriver
from browser import Browser


@pytest.fixture(scope="session")
def browser():
    browser = Browser(webdriver.Chrome(executable_path="D:\python qa internship\chromedriver.exe"))
    yield browser
    browser.close()
