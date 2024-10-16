-- https://leetcode.com/problems/tree-node/
WITH cte_parents AS (
    SELECT p_id FROM Tree WHERE p_id IS NOT NULL
)
SELECT t.id
, CASE
    WHEN p_id IS NULL
        THEN 'Root'
    WHEN EXISTS (SELECT 1 FROM cte_parents ct WHERE ct.p_id = t.id)
        THEN 'Inner'
    ELSE 'Leaf'
END AS "type"
FROM Tree t
;
