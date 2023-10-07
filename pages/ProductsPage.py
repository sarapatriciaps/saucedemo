from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class ProductsPage:
    url_pag_prod = 'https://www.saucedemo.com/inventory.html'

    def __init__(self, driver):
        self.driver = driver

    def is_url(self):
        return self.driver.current_url == self.url_pag_prod

    def has_tittle(self):
        tittle_text = self.driver.find_element(By.CLASS_NAME, 'title').text
        return tittle_text == 'Products'

    def has_menu_icon(self):
        try:
            menu = self.driver.find_element(By.ID, 'react-burger-menu-btn')
        except NoSuchElementException:
            return False
        return menu.is_displayed()
