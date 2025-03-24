--https://www.tryexponent.com/practice/prepare/post-success

-- 1
SELECT usr.user_type
, SUM(pst.is_successful_post::int)
, MIN(post_date)
FROM "user" usr
JOIN post pst ON pst.user_id = usr.user_id
WHERE EXTRACT(EPOCH FROM AGE(CURRENT_DATE, pst.post_date)) / 86400 < 29
GROUP BY 1
;

-- 2
SELECT interface
, COUNT(1) AS total_posts
, SUM(is_successful_post::INT) AS successful_posts
, ROUND(SUM(is_successful_post::INT) * 100 / COUNT(1), 2) AS success_rate
FROM post
WHERE LOWER(interface) LIKE '%lite%'
GROUP BY 1
;

-- 3
WITH user_success_cte AS (
    SELECT
        p.user_id,
        COUNT(p.post_id) AS total_posts,
        ROUND(SUM(p.is_successful_post::integer) * 100.0 / COUNT(p.post_id), 2) AS success_rate
    FROM
        post p
    GROUP BY
        p.user_id
)
, avgs_cte AS (
    SELECT AVG(total_posts) AS avg_total_posts
    , AVG(success_rate) AS avg_success_rate
    FROM user_success_cte
)
SELECT
    ups.user_id,
    ups.total_posts,
    ups.success_rate
FROM
    user_success_cte ups
CROSS JOIN
    avgs_cte avgs
WHERE
    ups.total_posts > avgs.avg_total_posts
    AND ups.success_rate < avgs.avg_success_rate
;

-- 4
WITH young_cte AS (
    SELECT
    ROUND(SUM(pst.is_successful_post::INT) * 100 / COUNT(1), 2) AS success_rate
    FROM post pst
    JOIN "user" usr ON usr.user_id = pst.user_id
    WHERE usr.age < 19
)
, non_young_cte AS (
    SELECT
    ROUND(SUM(pst.is_successful_post::INT) * 100 / COUNT(1), 2) AS success_rate
    FROM post pst
    JOIN "user" usr ON usr.user_id = pst.user_id
    WHERE usr.age > 18
)
SELECT y_cte.success_rate AS young_adult_success_rate
, ny_cte.success_rate AS non_young_adult_success_rate
, y_cte.success_rate - ny_cte.success_rate AS success_rate_difference
FROM young_cte y_cte
CROSS JOIN non_young_cte ny_cte
;

-- 5
WITH last_unsuccessful_post AS (
    SELECT
        user_id,
        MAX(post_date) AS last_unsuccessful_date
    FROM post
    WHERE is_successful_post = FALSE
    GROUP BY 1
),
successful_streak AS (
    SELECT
        p.user_id,
        COUNT(*) AS successful_posts_streak
    FROM post p
    LEFT JOIN last_unsuccessful_post lup ON p.user_id = lup.user_id
    WHERE 1 = 1
    AND p.is_successful_post = TRUE
    AND (lup.last_unsuccessful_date IS NULL OR p.post_date > lup.last_unsuccessful_date)
    GROUP BY 1
),
total_posts AS (
    SELECT
        user_id,
        COUNT(*) AS total_posts,
        SUM(is_successful_post::INT) AS total_successful_posts
    FROM post
    GROUP BY 1
)
SELECT
    u.user_id,
    CASE
        WHEN tp.total_posts = 0 THEN 0
        ELSE ROUND((tp.total_successful_posts * 1.0 / tp.total_posts) * 100, 2)
    END AS success_rate,
    COALESCE(ss.successful_posts_streak, 0) AS successful_posts_streak
FROM "user" u
LEFT JOIN successful_streak ss ON u.user_id = ss.user_id
LEFT JOIN total_posts tp ON u.user_id = tp.user_id
ORDER BY u.user_id
;