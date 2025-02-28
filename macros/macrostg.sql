{% macro macrostg() %}
    {% set query %}
        select table_name
        from information_schema.tables
        where table_schema = 'public'
          and table_name like 'f%'
    {% endset %}
    {% set results = run_query(query) %}
    {% if execute %}
        {{ return(results.columns[0].values()) }}
    {% else %}
        {{ return([]) }}
    {% endif %}
{% endmacro %}