from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def find_all_values(navegador):
    wait = WebDriverWait(navegador, 10)

    elementos = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "td.ticker1")))
    empresas = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "td.empresa1")))
    volumes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "td.volume1")))
    fechamentos = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "td.fechamento")))
    minimas = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "td.minima")))
    maximas = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "td.maxima")))
    ultimas = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "td.ultima1")))
    spansValue = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.value')))

    data = []
    for i in range(len(elementos)):
        row = {
            "Ticker": elementos[i].text,
            "Nome da Empresa": empresas[i].text,
            "Volume": volumes[i].text,
            "Fechamento Anterior": fechamentos[i].text,
            "Fechamento Mínimo": minimas[i].text,
            "Fechamento Máximo": maximas[i].text,
            "Última do Mês": ultimas[i].text,
            "Variação (Dia)": spansValue[i * 3].text,
            "Variação (Mês)": spansValue[i * 3 + 1].text,
            "Variação (Ano)": spansValue[i * 3 + 2].text
        }
        data.append(row)

    return data