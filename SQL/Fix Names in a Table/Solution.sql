-- https://leetcode.com/problems/fix-names-in-a-table/
SELECT
    user_id,
    UPPER(LEFT(name, 1)) || LOWER(RIGHT(name, - 1)) AS name
FROM users
ORDER BY user_id

-- Solution 2
SELECT user_id
	, (UPPER(SUBSTRING(name, 1, 1)) || LOWER(SUBSTRING(name, 2, LENGTH(name)))) AS name
FROM users
ORDER BY user_id;