{{ config(materialized='view') }}

SELECT
  DATE_TRUNC('month', data) AS mes,
  symbol,
  AVG(volume) AS media_volume_mensal
FROM
  {{ ref('stg_acoes') }}
GROUP BY
  DATE_TRUNC('month', data),
  symbol