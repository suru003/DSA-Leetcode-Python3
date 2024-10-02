--https://leetcode.com/problems/average-selling-price/

WITH cte_agg AS (
    SELECT p.product_id
    , p.start_date
    , SUM(p.price * u.units) AS total_price
    , SUM(u.units) AS total_units
    FROM Prices p
    LEFT JOIN UnitsSold u
    ON p.product_id = u.product_id
    AND p.start_date <= u.purchase_date
    AND u.purchase_date <= p.end_date
    GROUP BY p.product_id, p.start_date
)
SELECT cte.product_id
, COALESCE(ROUND(SUM(cte.total_price) / SUM(cte.total_units), 2), 0) AS average_price
FROM cte_agg cte
GROUP BY cte.product_id;

-- Solution 2
SELECT p.product_id
, COALESCE(ROUND(SUM(p.price * u.units * 1.0) / SUM(u.units), 2), 0) AS average_price
FROM Prices p
LEFT JOIN UnitsSold u
    ON p.product_id = u.product_id
    AND purchase_date BETWEEN start_date AND end_date
GROUP BY p.product_id;
