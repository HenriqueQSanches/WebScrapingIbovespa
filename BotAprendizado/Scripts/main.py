from navegacao.navegador import inicializar_navegador
from dados.extracao_dados import find_all_values
from dataframe.criar_dataframe import criar_dataframe

def main():
    navegador = inicializar_navegador()
    data = find_all_values(navegador)
    df_ibovespa = criar_dataframe(data)

    print(df_ibovespa)

    navegador.quit()

if __name__ == "__main__":
    main()
