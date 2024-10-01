-- https://leetcode.com/problems/average-time-of-process-per-machine/

WITH lagged_rows AS
(
    SELECT
    machine_id
    , process_id
    , activity_type
    , "timestamp"
    , LAG("timestamp", 1)
        OVER(
            PARTITION BY machine_id, process_id
            ORDER BY "timestamp"
            ) AS prev_timestamp

    FROM Activity
    -- WHERE activity_type = 'end'
)

SELECT machine_id
, ROUND(AVG("timestamp" - prev_timestamp)::NUMERIC, 3) AS processing_time
FROM lagged_rows
WHERE LOWER(activity_type) = 'end'
GROUP BY machine_id;
