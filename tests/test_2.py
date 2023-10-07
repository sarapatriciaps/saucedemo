import time
import pytest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Test2:
    URL = 'https://www.saucedemo.com/'

    @pytest.fixture
    def setup(self):
        print('\n######SETUP######')
        # instancia do Chrome (controler/driver)
        self.driver = webdriver.Chrome()

        # executar browser e acessar URL
        self.driver.get(self.URL)
        time.sleep(2)

        # pos condicao (executa apos todos os testes da classe)
        yield
        print('\n####TEARDOWN####')
        self.driver.quit()

    def test_login_saucedemo(self, setup):

        url_pag_prod = 'https://www.saucedemo.com/inventory.html'

        # inserir usuario
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        # inserir senha
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="password"]').send_keys('secret_sauce')
        # click btn login
        self.driver.find_element(By.ID, 'login-button').click()

        time.sleep(2)

        # validar se pagina de produtos foi apresentada (por URL)
        assert self.driver.current_url == url_pag_prod, 'URL invalida! Pagina de produtos nao acessada.'

        # validar se pagina de produtos foi apresentada (por objeto "titulo")
        tittle_text = self.driver.find_element(By.CLASS_NAME, 'title').text
        assert tittle_text == 'Products', 'TITULO da pagina de produtos NAO APRESENTADO!'

        # validar se MENU na pagina de produtos foi apresentado (por objeto "menu")
        menu = self.driver.find_element(By.ID, 'react-burger-menu-btn')
        menu.is_displayed(), 'MENU na pagina de produtos NAO APRESENTADO!'

        # validar se MENU na pagina de produtos foi apresentado usando try except)
        try:
            menu
        except NoSuchElementException:
            pytest.fail('MENU na pagina de produtos NAO APRESENTADO!')

        time.sleep(2)
