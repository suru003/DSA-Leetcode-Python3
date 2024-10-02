-- https://leetcode.com/problems/product-price-at-a-given-date

WITH last_prices AS (
    SELECT sq.product_id
    , sq.new_price
    FROM (
        SELECT p.product_id
        , p.new_price
        , ROW_NUMBER() OVER(
            PARTITION BY p.product_id
            ORDER BY p.change_date
            DESC
        ) AS row_num
        FROM Products p
        WHERE p.change_date <= '2019-08-16'
    ) sq
    WHERE sq.row_num = 1
),
dist_products AS (
    SELECT DISTINCT product_id
    FROM Products
)

SELECT p.product_id
, COALESCE(lp.new_price, 10) AS price
FROM dist_products p
LEFT JOIN last_prices lp
ON p.product_id = lp.product_id
;