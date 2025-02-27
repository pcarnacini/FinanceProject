Projeto Financeiro - Análise de Dados Financeiros

Contexto e Escolha de Dados
A pesquisa inicial identificou que dados financeiros brasileiros podem ser obtidos de diversas fontes. Para este projeto, optou-se por focar em preços diários de ações listadas na B3 (Bolsa de Valores Brasileira), dada a relevância para análise de mercado. Fontes como o Banco Central do Brasil (Dados Abertos do Banco Central) oferecem indicadores macroeconômicos, mas não cobrem especificamente preços de ações. Assim, foi selecionada a API Alpha Vantage, que suporta dados de ações brasileiras (ex.: PETR4.SA para Petrobras), com um tier gratuito adequado para projetos iniciais.

Escopo do Projeto
O projeto visa construir um pipeline de dados que:

Extraia dados de preços de ações via API.
Transforme e limpe os dados para análise.
Armazene os dados em Supabase, uma base de dados relacional baseada em PostgreSQL.
Modele os dados usando DBT Cloud para criar visões analíticas.
Gerencie todo o código e documentação com Git.
Este escopo reflete uma abordagem prática, alinhada com os fundamentos de engenharia de dados, como extração, transformação, carregamento (ETL) e modelagem, com foco em ferramentas modernas e acessíveis.



--------------------------------

EMPRESAS BRASILEIRAS NA ALPHA VANTAGE

Obtenção das empresas listadas na B3.
https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/empresas-listadas.htm

Obtenção das empresas listadas na Alpha Vantage.
https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=demo


Precisa ser verificado utilizando os códigos da B3 na Alpha, se contém na API, visto que a
intenção é focar no mercado de ações brasileiro.

Utiliza-se Pandas e SQLalchemy para fazer inner join e verificar pelo SYMBOL.
Após, salva-se em outro csv para usar posteriormente na aplicação direto na API para a busca.

---------------------------------


CONECTAR NA API E OBTER OS DADOS DAS EMPRESAS BRASILEIRAS


