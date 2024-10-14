-- https://leetcode.com/problems/percentage-of-users-attended-a-contest/
WITH agg_cte AS (
    SELECT COUNT(1) AS total_users FROM users
)

SELECT r.contest_id
, ROUND(COUNT(1)::NUMERIC / (SELECT total_users FROM agg_cte) * 100, 2) AS "percentage"
FROM Register r
GROUP BY r.contest_id
ORDER BY "percentage" DESC, r.contest_id ASC
;