from pages.ProductsPage import ProductsPage


class Test4:

    def test_add_product_to_cart(self, login_saucedemo):
        products_page = ProductsPage(login_saucedemo.driver)
        products_page.add_random_product_to_cart()
