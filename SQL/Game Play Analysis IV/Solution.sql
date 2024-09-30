-- https://leetcode.com/problems/game-play-analysis-iv

WITH cte_ids AS
(
    SELECT
    a.player_id
    , MIN(a.event_date)
    , CASE
        WHEN EXISTS (
            SELECT 1
            FROM Activity b
            WHERE 1 = 1
                AND a.player_id = b.player_id
                AND b.event_date = MIN(a.event_date) + 1
        ) THEN 1
        ELSE 0
        END AS score
    FROM Activity a
    GROUP BY a.player_id
)
SELECT ROUND(AVG(cte.score), 2) AS fraction
FROM cte_ids cte;
