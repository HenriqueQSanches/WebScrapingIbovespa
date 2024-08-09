from selenium import webdriver
import time

def inicializar_navegador():
    navegador = webdriver.Chrome()
    navegador.maximize_window()
    url = "https://inteligenciafinanceira.com.br/mercado-financeiro/ibovespa/"
    navegador.get(url)
    return navegador