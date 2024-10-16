-- https://leetcode.com/problems/user-activity-for-the-past-30-days-i/
SELECT activity_date AS day
, COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE 1 = 1
AND '2019-07-27'::DATE - activity_date > -1
AND '2019-07-27'::DATE - activity_date < 30
GROUP BY activity_date
;
