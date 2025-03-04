# Projeto Financeiro - Análise de Dados Financeiros

Contexto e Escolha de Dados
Este projeto tem como objetivo analisar dados financeiros do mercado de ações brasileiro no exterior (US Market), com foco em preços diários de ações listadas na B3 (Bolsa de Valores de São Paulo). A escolha por esse tipo de dado deve-se à sua relevância para análises de mercado e à disponibilidade de fontes confiáveis.

Inicialmente, fontes como o Banco Central do Brasil (Dados Abertos do Banco Central) foram consideradas, mas, por oferecerem apenas indicadores macroeconômicos sem cobertura específica de preços de ações, optou-se pela API Alpha Vantage, a qual busca os dados no mercado dos EUA (US Market). Essa API suporta dados de ações brasileiras e possui um tier gratuito adequado para projetos iniciais.

## Escopo do Projeto

### O projeto consiste em construir um pipeline de dados completo, abrangendo as seguintes etapas:

Extração: Obtenção de dados de preços de ações via API Alpha Vantage.
Transformação e Limpeza: Processamento dos dados para remover valores nulos e garantir consistência.
Armazenamento: Inserção dos dados tratados em um banco de dados relacional utilizando Supabase (baseado em PostgreSQL).
Modelagem: Criação de visões analíticas com DBT Cloud para facilitar a análise.
Visualização: Desenvolvimento de um dashboard interativo no Power BI para apresentar métricas e tendências.
Controle de Versão: Gerenciamento de código e documentação com Git.
Esse escopo reflete uma abordagem prática e moderna de engenharia de dados, alinhada aos fundamentos de extração, transformação e carregamento (ETL).

### Obtenção das Empresas Brasileiras na Alpha Vantage
Para garantir que as empresas da B3 estivessem disponíveis na Alpha Vantage, foram realizados os seguintes passos:

Lista da B3: Obtenção da lista de empresas diretamente no site da B3 (Empresas Listadas).
Lista da Alpha Vantage: Uso da função LISTING_STATUS da API Alpha Vantage para listar empresas suportadas (Documentação).
Verificação: Utilização de Pandas e SQLAlchemy para fazer um inner join entre as listas, identificando as empresas da B3 disponíveis na API. O resultado foi salvo em um arquivo CSV para uso posterior.
Seleção das Empresas
Devido à limitação de 25 consultas diárias no plano gratuito da API Alpha Vantage, foi necessário selecionar um subconjunto de empresas. A escolha foi baseada no valor de mercado e na composição do Ibovespa, resultando na seguinte lista:

ABEV (Ambev S.A.); AZUL (Azul S.A.); BBDC (Barings BDC Inc, relacionado ao Bradesco); BRFS (BRF S.A.); CSAN (Cosan S.A.); ITUB (Itau Unibanco Holding S.A.); JBSS (JBS S.A.); VALE (Vale S.A.); PETZ (TDH Holdings Inc, Petlove); QUAL (Qualicorp); RAIL (Rumo S.A.); RENT (Localiza); RNEW (Renova Energia); SBFG (Grupo SBF, Centauro); SEER (Ser Educacional); SOND (Sondotecnica); TKNO (Tekno); VAMO (Vamos); VSTE (Veste); WEST (Westwing); AGRO (BrasilAgro); AMBP (Ambipar); CASH (Meliuz); ELMD (Eletromidia); MBLY (Mobly)
Essa seleção representa uma amostra diversificada do mercado brasileiro.

### Extração dos Dados
Leitura do CSV: O arquivo CSV com as empresas selecionadas foi lido para identificar os símbolos a serem consultados.
Consulta à API: Iteração sobre as empresas para obter dados históricos de preços via API Alpha Vantage.
Armazenamento Local: Os dados brutos foram salvos em uma pasta separada para posterior processamento.
Tratamento e Envio dos Dados
Limpeza: Remoção de valores nulos e padronização dos tipos de dados.
Enriquecimento: Adição do código da empresa (symbol) para facilitar a identificação.
Envio ao Banco: Uso de Pandas e SQLAlchemy para inserir os dados tratados no Supabase.

### Modelagem dos Dados
DBT Cloud: Criação de uma tabela geral (staging) e desenvolvimento de modelos analíticos, como visões de retornos diários, médias e volatilidade.
Visões Analíticas: Facilitam consultas eficientes e fornecem insights diretos sobre o desempenho das ações.

### Visualização
Power BI: Desenvolvimento de um dashboard interativo para apresentar métricas e tendências de forma visual e intuitiva.
Link do Dashboard: [Dashboard interativo no Power BI](https://app.powerbi.com/view?r=eyJrIjoiODAxNGVlYzktODQ4Ny00NzBlLWI3NWEtOTgwYzcyMDU3YzI2IiwidCI6IjIzZGQzNGE4LWRjMGUtNDU0YS05OTE3LTlhNjQ1OWY0OGJhOCJ9)

### Considerações Finais
Este projeto demonstra a implementação de um pipeline de dados completo, desde a extração até a visualização, utilizando ferramentas modernas e acessíveis. Ele pode ser expandido para incluir mais ações ou métricas adicionais conforme necessário.
