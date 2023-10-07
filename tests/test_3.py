import time
import pytest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from tests.conftest import URL
from tests.conftest import url_pag_prod


class Test3:
    # aplicando confitest
    def test_click_login_btn(self, setup):

        # instancia do obj driver (conftest)
        driver = setup

        # buscar botao login
        login_btn = driver.find_element(By.ID, 'login-button')  # busca elemento por Id
        # driver.find_element(By.CSS_SELECTOR, '#login-button') #busca elemento por CSS Selector
        # driver.find_element(By.XPATH,'//*[@id="login-button"]') #busca elemento por Xpath dinamico
        # driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[1]/div/div/form/input') #busca elemento por Xpath full

        # clicar no botao login
        login_btn.click()
        time.sleep(2)

        # validar que mudou de pagina apos click
        assert driver.current_url == URL, 'Aplicacao nao permaneceu na mesma pagina!'

        # validar que msg de erro foi exibida
        msg_erro = driver.find_element(By.CLASS_NAME, 'error-message-container').text
        assert msg_erro == 'Epic sadface: Username is required', 'Erro ao validar mensagem de erro!'

    def test_login_saucedemo(self, setup):

        # instancia do obj driver (conftest)
        driver = setup

        # inserir usuario
        driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        # inserir senha
        driver.find_element(By.CSS_SELECTOR, '[data-test="password"]').send_keys('secret_sauce')
        # click btn login
        driver.find_element(By.ID, 'login-button').click()

        time.sleep(2)

        # validar se pagina de produtos foi apresentada (por URL)
        assert driver.current_url == url_pag_prod, 'URL invalida! Pagina de produtos nao acessada.'

        # validar se pagina de produtos foi apresentada (por objeto "titulo")
        tittle_text = driver.find_element(By.CLASS_NAME, 'title').text
        assert tittle_text == 'Products', 'TITULO da pagina de produtos NAO APRESENTADO!'

        # validar se MENU na pagina de produtos foi apresentado (por objeto "menu")
        menu = driver.find_element(By.ID, 'react-burger-menu-btn')
        menu.is_displayed(), 'MENU na pagina de produtos NAO APRESENTADO!'

        # validar se MENU na pagina de produtos foi apresentado usando try except)
        try:
            menu
        except NoSuchElementException:
            pytest.fail('MENU na pagina de produtos NAO APRESENTADO!')

        time.sleep(2)
