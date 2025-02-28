import pandas as pd
import requests
import os

# Configurar a pasta de saída
output_folder = 'api_csv/'
os.makedirs(output_folder, exist_ok=True)

# Lista de empresas (tickers)
empresas = ["ABEV", "AZUL", "BBDC", "BRFS", "CSAN", "ITUB", "JBSS", "VALE",
            "PETZ", "QUAL", "RAIL", "RENT", "RNEW", "SBFG", "SEER", "SOND",
            "TKNO", "VAMO", "VSTE", "WEST", "AGRO", "AMBP", "CASH", "ELMD", "MBLY"]

# Iterar sobre os símbolos e buscar dados da API
for symbol in empresas:
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey=XKKF8ZKJVIB14W6U'
    
    r = requests.get(url)
    data = r.json()
    
    if 'Time Series (Daily)' in data:
        df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
        
        # Salvar o resultado como CSV
        output_file = os.path.join(output_folder, f'{symbol}_dados.csv')
        df.to_csv(output_file, index=True)
        print(f'Dados de {symbol} salvos em {output_file}')
    else:
        print(f'Erro ao buscar dados para {symbol}: {data.get("Note", "Erro desconhecido")}')

print("Empresas encontradas na Alpha e salvas!")
