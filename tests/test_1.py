import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Teste1:
    URL = 'https://www.saucedemo.com/'
    @pytest.fixture
    def setup(self):
        print('\n######SETUP######')
        #instancia do Chrome (controler/driver)
        self.driver = webdriver.Chrome()

        #executar browser e acessar URL
        self.driver.get(self.URL)
        time.sleep(2)

        #pos condicao (executa apos todos os testes da classe)
        yield
        print('\n####TEARDOWN####')
        self.driver.quit()

    def test_click_login_btn(self, setup):

        #buscar botao login
        login_btn = self.driver.find_element(By.ID, 'login-button') #busca elemento por Id
        #driver.find_element(By.CSS_SELECTOR, '#login-button') #busca elemento por CSS Selector
        #driver.find_element(By.XPATH,'//*[@id="login-button"]') #busca elemento por Xpath dinamico
        #driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[1]/div/div/form/input') #busca elemento por Xpath full

        #clicar no botao login
        login_btn.click()
        time.sleep(2)

        #validar que mudou de pagina apos click
        assert self.driver.current_url == self.URL,'Aplicacao nao permaneceu na mesma pagina!'

        #validar que msg de erro foi exibida
        msg_erro = self.driver.find_element(By.CLASS_NAME, 'error-message-container').text
        assert msg_erro == 'Epic sadface: Username is required', 'Erro ao validar mensagem de erro!'
