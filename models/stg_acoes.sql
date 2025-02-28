{{ config(materialized='table') }}

{% set tables = macrostg() %}

with stg_acoes as (
    {% for table_name in tables %}
    select 
        data,
        open,
        high,
        low,
        close,
        volume,
        symbol
    from {{ source('public', table_name) }} 
    {% if not loop.last %}union all{% endif %}
    {% endfor %}
)

select * from stg_acoes