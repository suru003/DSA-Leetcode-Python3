-- https://leetcode.com/problems/list-the-products-ordered-in-a-period/

SELECT prd.product_name
, SUM(ord.unit) AS unit
FROM Orders ord
JOIN Products prd
ON prd.product_id = ord.product_id
WHERE 1 = 1
    AND EXTRACT(MONTH FROM order_date) = 2
    AND EXTRACT(YEAR FROM order_date) = 2020
GROUP BY prd.product_name
HAVING SUM(ord.unit) > 99;