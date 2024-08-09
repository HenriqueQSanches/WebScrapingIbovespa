import pandas as pd
import os

def criar_dataframe(data):
    df = pd.DataFrame(data)
    pasta_dados = os.path.join(os.path.dirname(__file__), '..', 'dados')
    csv_file_path = os.path.join(pasta_dados, 'ibovespa_data.csv')


    df.to_csv(csv_file_path, index=False)

    print(f"Arquivo CSV '{csv_file_path}' criado com sucesso.")
    return df