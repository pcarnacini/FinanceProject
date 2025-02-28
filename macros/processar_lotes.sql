{% macro processar_lotes(tables, batch_size=10) %}
    {% set batches = [] %}
    {% for i in range(0, tables|length, batch_size) %}
        {% set batch = tables[i:i+batch_size] %}
        {% do batches.append(batch) %}
    {% endfor %}
    {{ return(batches) }}
{% endmacro %}