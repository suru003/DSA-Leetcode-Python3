-- https://leetcode.com/problems/queries-quality-and-percentage/
WITH agg_cte AS (
    SELECT q.query_name
    , q.rating::NUMERIC / q.position AS quality_ratio
    , CASE
        WHEN q.rating < 3 THEN 1
        ELSE 0
    END AS is_poor
    FROM Queries q
    WHERE q.query_name IS NOT NULL
)
SELECT ac.query_name
, ROUND(AVG(ac.quality_ratio), 2) AS quality
, ROUND(AVG(ac.is_poor) * 100, 2) AS poor_query_percentage
FROM agg_cte ac
GROUP BY ac.query_name;


-- Solution 2
SELECT
    query_name,
    ROUND(SUM(rating::NUMERIC / position) / COUNT(result), 2) AS quality,
    ROUND(100.0 * SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / COUNT(rating), 2) AS poor_query_percentage
FROM
    Queries
WHERE
    query_name IS NOT NULL
GROUP BY
    query_name;
