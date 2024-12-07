import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def tela_inicio(browser):
    browser.get("http://127.0.0.1:4004")
    return browser


@pytest.fixture
def procura_elden_ring(browser):
    browser.find_element(By.ID, "validarNome").send_keys("elden ring")
    return browser


@pytest.fixture
def procura_dark_souls(browser):
    browser.find_element(By.ID, "validarNome").send_keys("dark souls")
    return browser


@pytest.fixture
def procura_silent_hill(browser):
    browser.find_element(By.ID, "validarNome").send_keys("silent hill 2")
    return browser


@pytest.fixture
def procura_jogo_invalido(browser):
    browser.find_element(By.ID, "validarNome").send_keys("jogo inválido")
    return browser


@pytest.fixture
def clica_pesquisar(browser):
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
    return browser


@pytest.fixture
def tela_jogo(browser):
    time.sleep(5)
    grafico = browser.find_element(By.ID, "graficoMeses")
    nome_jogo = browser.find_element(By.ID, "nomeJogo")
    tendencia = browser.find_element(By.ID, "tendencia")
    assert grafico.is_displayed()
    assert nome_jogo.is_displayed()
    assert tendencia.is_displayed()


@pytest.fixture
def outras_ocorrencias(browser):
    time.sleep(3)
    assert browser.find_element(By.PARTIAL_LINK_TEXT, "dark souls").is_displayed()


@pytest.fixture
def opcao_dark_souls(browser):
    browser.find_element(By.LINK_TEXT, "dark souls iii").click()
    return browser


@pytest.fixture
def nao_encontrado(browser):
    assert browser.find_element(By.CLASS_NAME, "text-danger").is_displayed()


@pytest.fixture
def inserir_texto(browser):
    assert browser.find_element(By.CLASS_NAME, "invalid-feedback").is_displayed()


@pytest.fixture
def sem_dados(browser):
    assert browser.find_element(By.CLASS_NAME, "alert-danger").is_displayed()


@pytest.fixture
def acessa_inexistente(browser):
    browser.get("http://127.0.0.1:4004/jogo/12345")
