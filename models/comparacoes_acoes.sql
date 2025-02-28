{{ config(materialized='view') }}

WITH retornos_medios AS (
  SELECT
    symbol,
    AVG((close - open) / open) AS retorno_medio
  FROM
    {{ ref('stg_acoes') }}
  GROUP BY
    symbol
)
SELECT
  symbol,
  retorno_medio
FROM
  retornos_medios
ORDER BY
  retorno_medio DESC
LIMIT 5