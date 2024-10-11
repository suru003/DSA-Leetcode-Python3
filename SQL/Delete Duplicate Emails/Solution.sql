-- https://leetcode.com/problems/delete-duplicate-emails/
WITH del_cte AS (
    SELECT MIN(id) AS id FROM Person GROUP BY email
)
DELETE FROM Person p
WHERE NOT EXISTS ( SELECT 1 FROM del_cte dc WHERE dc.id = p.id);