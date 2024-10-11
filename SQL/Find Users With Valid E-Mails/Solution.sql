-- https://leetcode.com/problems/find-users-with-valid-e-mails

SELECT *
FROM Users
WHERE mail ~ '^[a-zA-Z]+[a-zA-Z0-9_.-]*@leetcode\.com$'

-- Solution 2
SELECT user_id, name, mail
FROM Users
WHERE regexp_match(mail, '^[a-zA-Z]([a-zA-Z0-9_.-]+)?@leetcode\.com$') IS NOT NULL;