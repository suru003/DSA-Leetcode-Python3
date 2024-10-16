-- https://leetcode.com/problems/market-analysis-i/
WITH cte_counts AS (
    SELECT buyer_id AS user_id
    , COUNT(item_id) AS orders_in_2019
    FROM Orders
    WHERE EXTRACT("Year" FROM order_date) = 2019
    GROUP BY buyer_id
)
SELECT u.user_id AS buyer_id
, u.join_date
, COALESCE(ct.orders_in_2019, 0) AS orders_in_2019
FROM Users u
LEFT JOIN cte_counts ct
ON u.user_id = ct.user_id
;
