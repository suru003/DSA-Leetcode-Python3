-- https://leetcode.com/problems/customers-who-bought-all-products/

WITH total_count AS (
    SELECT COUNT(1) AS target_count
    FROM Product
),
agg_count AS (
    SELECT customer_id
    , product_key
    , COUNT(1) AS unique_count
    FROM Customer
    GROUP BY customer_id, product_key
)
SELECT customer_id
FROM agg_count
GROUP BY customer_id
HAVING COUNT(unique_count) = ( SELECT target_count FROM total_count )
;