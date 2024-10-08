-- https://leetcode.com/problems/exchange-seats/

WITH agg_cte AS (
    SELECT id
    , student
    , CASE 
        WHEN id % 2 = 1
            THEN LEAD(student) OVER(ORDER BY id)
        ELSE LAG(student) OVER(ORDER BY id)
    END AS student_swap
    FROM Seat
)
SELECT id
, COALESCE(student_swap, student) AS student
FROM agg_cte;
