{{ config(materialized='view') }}

SELECT
  data,
  symbol,
  (close - open) / open AS retorno_diario
FROM
  {{ ref('stg_acoes') }}