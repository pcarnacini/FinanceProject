{{ config(materialized='view') }}

WITH retornos AS (
  SELECT
    data,
    symbol,
    (close - open) / close AS retorno_diario
  FROM
    {{ ref('stg_acoes') }}
)
SELECT
  data,
  symbol,
  STDDEV(retorno_diario) OVER (
    PARTITION BY symbol 
    ORDER BY data 
    ROWS BETWEEN 29 PRECEDING AND CURRENT ROW
  ) AS volatilidade_30_dias
FROM
  retornos