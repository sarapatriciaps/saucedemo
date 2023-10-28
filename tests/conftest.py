import pytest
from selenium import webdriver

from pages.LoginPage import LoginPage

URL = 'https://www.saucedemo.com/'


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


@pytest.fixture()
def login_saucedemo(open_browser):
    login_p = open_browser
    login_p.enter_login()
    yield login_p
