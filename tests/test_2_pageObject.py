from pages.ProductsPage import ProductsPage


# aplicando conceito do pageObject
# implementando LoginPage
# implementando ProductsPage
class Test2_pageObject:

    def test_click_login_btn(self, open_browser):
        pg_login = open_browser
        pg_login.click_login_btn()

        assert pg_login.is_url_login_page(), 'Aplicacao nao permaneceu na mesma pagina!'
        assert pg_login.has_login_error_msg(), 'Erro ao validar mensagem de erro!'

    def test_login_saucedemo(self, open_browser):
        pg_login = open_browser
        pg_login.enter_login()

        pg_products = ProductsPage(driver=pg_login.driver)

        assert pg_products.is_url_products(), 'URL invalida! Pagina de produtos nao acessada.'
        assert pg_products.has_tittle(), 'TITULO da pagina de produtos NAO APRESENTADO!'
        assert pg_products.has_menu_icon(), 'MENU na pagina de produtos NAO APRESENTADO!'
