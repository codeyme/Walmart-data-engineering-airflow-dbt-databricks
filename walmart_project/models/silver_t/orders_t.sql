{{
    config(
        materialized='incremental',
        unique_key='order_id'
    )
}}


select *, current_timestamp() as processed_at
 from {{source('walmart_databricks', 'orders')}}
where is_active = 'Y'

{% if is_incremental() %}
  and updated_timestamp > (select COALESCE(max(updated_timestamp, '1900-01-01'), '1900-01-01') from {{ this }})
{% endif %}
