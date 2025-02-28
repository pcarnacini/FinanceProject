{{ config(materialized='view') }}

SELECT
  data,
  symbol,
  AVG(close) OVER (
    PARTITION BY symbol 
    ORDER BY data 
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS media_movel_7_dias,
  AVG(close) OVER (
    PARTITION BY symbol 
    ORDER BY data 
    ROWS BETWEEN 29 PRECEDING AND CURRENT ROW
  ) AS media_movel_30_dias
FROM
  {{ ref('stg_acoes') }}