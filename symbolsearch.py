import pandas as pd
from sqlalchemy import create_engine, text

# Criação do banco de dados SQLite em memória (ou pode ser um arquivo)
engine = create_engine('sqlite:///:memory:')

# Carregar os CSVs para DataFrames
csv1_path = 'empresas_listadas_alpha.csv'
csv2_path = 'empresas_listadas_b3.csv'

df1 = pd.read_csv(csv1_path)
df2 = pd.read_csv(csv2_path)

# Carregar os DataFrames como tabelas no banco SQLite
df1.to_sql('tabela1', con=engine, index=False, if_exists='replace')
df2.to_sql('tabela2', con=engine, index=False, if_exists='replace')

print("Banco de dados SQLite configurado com sucesso!")

with engine.connect() as connection:
    result = connection.execute(text("""
        SELECT t1.*, t2.* 
        FROM tabela1 t1
        INNER JOIN tabela2 t2 
        ON t1.symbol = t2.codigo
    """))

    # Transformar o resultado em DataFrame
    result_df = pd.DataFrame(result.fetchall(), columns=result.keys())
    
    # Salvar o resultado em um arquivo CSV
    result_df.to_csv('Empresas_Listadas_B3eAlpha.csv', index=False)
    print("Consulta salva como 'Empresas_Listadas_B3eAlpha.csv'!")
