-- https://leetcode.com/problems/last-person-to-fit-in-the-bus/

WITH agg_cte AS (
    SELECT q.person_id
    , q.person_name
    , q.weight
    , SUM(q.weight) OVER(ORDER BY q.turn) AS cumm_sum
    FROM Queue q
)
SELECT cte.person_name
FROM agg_cte cte
WHERE cte.cumm_sum <= 1000
ORDER BY cte.cumm_sum DESC
LIMIT 1;
