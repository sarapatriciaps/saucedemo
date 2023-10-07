import pytest
from selenium import webdriver

from pages.LoginPage import LoginPage

URL = 'https://www.saucedemo.com/'
url_pag_prod = 'https://www.saucedemo.com/inventory.html'


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get(URL)

    yield driver
    driver.quit()


@pytest.fixture()
def open_browser():
    login_p = LoginPage()
    login_p.open_page()
    yield login_p
    login_p.close_page()
