import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import Date, Float, BigInteger, String

# Usa os dados pra conectar no banco
db_params = {
    'host': 'aws-0-us-west-1.pooler.supabase.com',
    'database': 'postgres',
    'user': 'postgres.vbionqmazkbltxfvsnvg',
    'password': 'f7pEDy8XQIQk7zb4'
}

# Usa o SQLalchemy pra conectar no banco
engine = create_engine(f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}/{db_params['database']}")

# Caminho dos csvs
csv_directory = 'api_csv/att/'

# Itera por todos os csvs na pasta
for filename in os.listdir(csv_directory):
    if filename.endswith('.csv'):
        # Lê o csv
        file_path = os.path.join(csv_directory, filename)
        df = pd.read_csv(file_path)

        # Renomeia as colunas para o schema desejado
        df.columns = ['data', 'open', 'high', 'low', 'close', 'volume', 'symbol']

        # Converte os tipos de dados das colunas
        df['data'] = pd.to_datetime(df['data'])  # Converte para date
        df['open'] = df['open'].astype(float)   # Converte para float
        df['high'] = df['high'].astype(float)    # Converte para float
        df['low'] = df['low'].astype(float)      # Converte para float
        df['close'] = df['close'].astype(float)  # Converte para float
        df['volume'] = df['volume'].astype(int)  # Converte para int
        df['symbol'] = df['symbol'].astype(str)  # Converte para varchar (string)

        # Cria o nome da tabela: remove '_dados' e adiciona 'f' no início
        table_name = 'f' + os.path.splitext(filename)[0].replace('_dados', '').upper()

        # Upload pro Supabase
        try:
            df.to_sql(
                name=table_name,
                con=engine,
                if_exists='replace',  # Garantia de que substitua caso a tabela exista
                index=False,
                dtype={
                    'data': Date,      # Tipo DATE do SQLAlchemy
                    'open': Float,     # Tipo FLOAT do SQLAlchemy
                    'high': Float,     # Tipo FLOAT do SQLAlchemy
                    'low': Float,      # Tipo FLOAT do SQLAlchemy
                    'close': Float,    # Tipo FLOAT do SQLAlchemy
                    'volume': BigInteger, # Tipo BigINTEGER (alguns valores são muito grandes) do SQLAlchemy
                    'symbol': String   # Tipo VARCHAR
                }
            )
            print(f"CSV enviado: {filename} to table {table_name}")
        except Exception as e:
            print(f"Erro no envio do CSV: {filename}: {str(e)}")

print("Todos CSVs enviados ao banco de dados")