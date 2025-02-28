{{ config(materialized='view') }}

SELECT
  data,
  symbol,
  (((close - open) / open)*100) AS retorno_diario
FROM
  {{ ref('stg_acoes') }}