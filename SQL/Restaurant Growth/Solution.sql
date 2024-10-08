-- https://leetcode.com/problems/restaurant-growth/
WITH total_cte AS (
    SELECT
    visited_on
    , SUM(amount) AS total
    FROM Customer
    GROUP BY visited_on
)
SELECT
visited_on
, SUM(total) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount
, ROUND(AVG(total) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS average_amount
FROM total_cte
ORDER BY visited_on
OFFSET 6
;