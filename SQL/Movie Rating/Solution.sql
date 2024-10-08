-- https://leetcode.com/problems/movie-rating/

WITH top_user AS (
    SELECT us.name AS results
    FROM MovieRating mr
    JOIN Users us
    ON mr.user_id = us.user_id
    GROUP BY us.name
    ORDER BY
        COUNT(*) DESC
        , us.name ASC
    LIMIT 1
),
top_movie AS (
    SELECT mv.title AS results
    FROM MovieRating mr
    JOIN Movies mv
    ON mr.movie_id = mv.movie_id
    WHERE 1 = 1
    AND EXTRACT(MONTH FROM mr.created_at) = 2
    AND EXTRACT(YEAR FROM mr.created_at) = 2020
    GROUP BY mv.title
    ORDER BY
        AVG(mr.rating) DESC
        , mv.title ASC
    LIMIT 1
)

SELECT * FROM top_user
UNION ALL
SELECT * FROM top_movie
;
