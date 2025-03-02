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

A API limita-se no plano gratuito a 25 consultas diárias. A partir disso, de acordo com o
valor de mercado e composição IBOVESPA, escolheu-se as seguintes:

ABEV - Ambev S.A., AZUL - Azul S.A., BBDC - Barings BDC Inc (relacionado ao Bradesco)
BRFS - BRF S.A., CSAN - Cosan S.A., ITUB - Itau Unibanco Holding S.A.
JBSS - JBS S.A., VALE - Vale S.A., PETZ - TDH Holdings Inc (Petlove)
QUAL - Qualicorp, RAIL - Rumo S.A., RENT - Localiza
RNEW - Renova Energia, SBFG - Grupo SBF (Centauro), SEER - Ser Educacional
SOND - Sondotecnica, TKNO - Tekno, VAMO - Vamos
VSTE - Veste, WEST - Westwing, AGRO - BrasilAgro
AMBP - Ambipar, CASH - Meliuz, ELMD - Eletromidia, MBLY - Mobly

Lê-se o csv das empresas já reconhecidas.
Itera-se todas as empresas na API, fazendo com que obtenha-se os dados de todas as listadas.
Salva-se em uma pasta separada para após enviar ao banco de dados.

---------------------------------

Faz-se o tratamento dos dados, removendo os valores nulos (se existentes), tratando os dados, e acrescenta-se o código da empresa.
Envia-se os dados para o banco de dados utilizando pandas e SQLAlchemy.

---------------------------------

Transformação dos dados em uma tabela geral (staging)
Agora, utiliza-se o DBT Cloud para fazer a modelagem dos dados.

Modelagens feitas:

Modelo de Retornos Diários
Objetivo: Calcular o retorno diário de cada ação, medindo a variação percentual entre o preço de abertura e fechamento.

Modelo de Médias Móveis
Objetivo: Calcular as médias móveis de 7 e 30 dias para o preço de fechamento.

Modelo de Volatilidade
Objetivo: Calcular a volatilidade como o desvio padrão dos retornos diários em um período de 30 dias.

Modelo de Métricas Agregadas
Objetivo: Gerar métricas agregadas, como a média de volume negociado por mês para cada ação.

Modelo de Comparações entre Ações
Objetivo: Identificar as 5 ações com maior retorno médio.

---------------------------------

Por fim, utilizou-se do Power BI para desenvolver um dashboard interativo, que permite ao usuário visualizar as métricas e tendências das ações.
link_do_dashboard.dash.br

---------------------------------
