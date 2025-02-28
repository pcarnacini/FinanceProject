import pandas as pd
import os

# Encontra todos os arquivos CSV na pasta "api_csv"
csv_files = [f for f in os.listdir('api_csv') if f.endswith('.csv')]

for csv_file in csv_files:
    # Lê o arquivo CSV
    df = pd.read_csv(f'api_csv/{csv_file}')
    
    # Renomeia a primeira coluna para 'date'
    df.rename(columns={df.columns[0]: 'date'}, inplace=True)
    
    # Remove o número do cabeçalho da coluna
    new_columns = ['Date'] + [col.split('.')[-1].strip() for col in df.columns[1:]]
    df.columns = new_columns
    
    # Remove linhas com valores NaN/null
    df = df.dropna()
    
    # Adiciona a coluna 'symbol' com o nome do arquivo sem '_dados'
    symbol_name = csv_file.replace('_dados.csv', '')
    df['symbol'] = symbol_name
    
    # Salva o arquivo CSV atualizado
    df.to_csv(f'api_csv/att/{csv_file}', index=False)