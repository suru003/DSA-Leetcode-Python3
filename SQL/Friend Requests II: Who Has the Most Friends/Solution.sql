-- https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/
WITH cte_1 AS (
    SELECT requester_id
    , COUNT(*) AS count
    FROM RequestAccepted
    GROUP BY requester_id
)
, cte_2 AS (
    SELECT accepter_id
    , COUNT(*) AS count
    FROM RequestAccepted
    GROUP BY accepter_id
)
SELECT requester_id AS id
, SUM(count) AS num
FROM
    (
    SELECT * FROM cte_1
    UNION ALL
    SELECT * FROM cte_2
    )
GROUP BY requester_id
ORDER BY SUM(count) DESC
LIMIT 1
;
