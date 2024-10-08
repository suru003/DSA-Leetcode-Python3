-- https://leetcode.com/problems/trips-and-users/

WITH valid_cte AS (
    SELECT users_id
    FROM Users
    WHERE LOWER(banned) = "no"
)

SELECT
request_at AS 'Day',
ROUND(AVG(
    CASE
        WHEN LOWER(status) LIKE '%cancelled%'
        THEN 1
        ELSE 0
    END
), 2) AS 'Cancellation Rate'
FROM Trips trip
WHERE 1 = 1
    AND request_at >= '2013-10-01' AND request_at <= '2013-10-03'
    AND EXISTS (
        SELECT 1 FROM valid_cte cte
        WHERE cte.users_id = trip.client_id
        )
    AND EXISTS (
        SELECT 1 FROM valid_cte cte
        WHERE cte.users_id = trip.driver_id
    )
GROUP BY request_at;
