from random import randint

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class ProductsPage(PageObject):
    url_pag_prod = 'https://www.saucedemo.com/inventory.html'
    class_product_card = 'inventory_item'
    class_add_to_cart_btn = 'btn_primary'
    text_add_to_cart = 'Add to cart'
    class_remove_btn = 'btn_secondary'
    text_remove_btn = 'remove'
    class_product_name = 'inventory_item_name'

    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver=driver)

    def is_url_products(self):
        return self.is_url(self.url_pag_prod)

    def has_tittle(self):
        tittle_text = self.driver.find_element(By.CLASS_NAME, 'title').text
        return tittle_text == 'Products'

    def has_menu_icon(self):
        try:
            menu = self.driver.find_element(By.ID, 'react-burger-menu-btn')
        except NoSuchElementException:
            return False
        return menu.is_displayed()

    def add_random_product_to_cart(self):
        products_list = self.driver.find_element(By.CLASS_NAME, self.class_product_card)
        random_index = randint(0, len(products_list) - 1)
        product_card = products_list[random_index]

        add_to_cart_btn = product_card.find_element(By.CSS_SELECTOR, self.class_add_to_cart_btn)
        if add_to_cart_btn.text != self.text_add_to_cart:
            raise Exception('Add to cart button name is invalid!')
        add_to_cart_btn.click()

        remove_btn = product_card.find_element(By.CLASS_NAME, self.class_remove_btn)
        if remove_btn.text != self.text_remove_btn:
            raise Exception('Remove button name is invalid!')
