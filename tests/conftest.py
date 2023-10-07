import pytest
from selenium import webdriver

URL = 'https://www.saucedemo.com/'
url_pag_prod = 'https://www.saucedemo.com/inventory.html'

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get(URL)

    yield driver
    driver.quit()
