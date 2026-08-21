select * from {{source('walmart_databricks', 'orders')}};
select * from {{source('walmart_databricks', 'products')}};