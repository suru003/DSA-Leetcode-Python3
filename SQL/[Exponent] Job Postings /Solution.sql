--https://www.tryexponent.com/practice/prepare/job-postings
-- 1
SELECT jb.job_id, jb.job_name, ROUND(AVG(yrs_experience), 1) AS avg_experience
FROM job jb
JOIN job_posting jp ON jp.job_id = jb.job_id
JOIN application app ON app.post_id = jp.post_id
JOIN applicant apt ON apt.applicant_id = app.applicant_id
GROUP BY 1, 2
ORDER BY 1
;

-- 2
SELECT EXTRACT(YEAR FROM jp.date_posted)
, SUM(CASE
        WHEN EXTRACT(MONTH FROM jp.date_posted) < 7
            THEN 1
        ELSE 0
      END) AS first_half_count
, SUM(CASE
        WHEN EXTRACT(MONTH FROM jp.date_posted) < 7
            THEN 0
        ELSE 1
      END) AS second_half_count
FROM job_posting jp
GROUP BY 1
;

-- 3
WITH agg_avg_cte AS (
    SELECT jp.job_id
    , AGE(jp.date_posted, app.applied_date) AS elapsed_time
FROM job_posting jp
JOIN application app ON app.post_id = jp.post_id
),
salary_range_cte AS (
    SELECT job_id
    , CASE
        WHEN job_salary <= 100000
            THEN '0–100K'
        WHEN 200000 >= job_salary AND job_salary > 100000
            THEN '100K-200K'
        ELSE 'OVER 200K'
    END AS salary_range
    FROM job
)
SELECT range_cte.salary_range
, AVG(avg_cte.elapsed_time)
FROM salary_range_cte range_cte
JOIN agg_avg_cte avg_cte ON avg_cte.job_id = range_cte.job_id
GROUP BY 1
;

-- 3
WITH agg_avg_cte AS (
    SELECT jp.job_id
    , AGE(app.applied_date, jp.date_posted) AS elapsed_time
FROM job_posting jp
JOIN application app ON app.post_id = jp.post_id
),
salary_range_cte AS (
    SELECT job_id
    , CASE
        WHEN job_salary <= 100000
            THEN '0–100K'
        WHEN 200000 >= job_salary AND job_salary >= 100001
            THEN '100K-200K'
        ELSE '200K+'
    END AS salary_range
    FROM job
)
SELECT range_cte.salary_range
, ROUND(AVG(EXTRACT(EPOCH FROM avg_cte.elapsed_time) / 86400), 2) AS avg_elapsed_time
FROM salary_range_cte range_cte
JOIN agg_avg_cte avg_cte ON avg_cte.job_id = range_cte.job_id
GROUP BY 1
ORDER BY 1
;

-- 4
WITH applicant_application_count AS (
    -- Calculate how many jobs each applicant has applied to
    SELECT
        applicant_id,
        COUNT(DISTINCT post_id) AS job_count
    FROM
        application
    GROUP BY
        applicant_id
),
single_and_multi_applicants AS (
    -- Identify applicants who applied to only one job (single) or multiple jobs
    SELECT
        app.post_id,
        aac.applicant_id,
        CASE
            WHEN aac.job_count = 1 THEN 'single'
            ELSE 'multiple'
        END AS application_type
    FROM
        application app
    JOIN
        applicant_application_count aac ON app.applicant_id = aac.applicant_id
)
SELECT
    jp.job_id,
    j.job_name,
    SUM(CASE WHEN sam.application_type = 'single' THEN 1 ELSE 0 END) AS single_time_applicants,
    SUM(CASE WHEN sam.application_type = 'multiple' THEN 1 ELSE 0 END) AS multi_time_applicants
FROM
    single_and_multi_applicants sam
JOIN
    job_posting jp ON sam.post_id = jp.post_id
JOIN
    job j ON jp.job_id = j.job_id
GROUP BY
    jp.job_id, j.job_name;


-- 5
WITH min_salary_cte AS (
    SELECT * FROM (
        SELECT app.applicant_id
        , aplt.yrs_experience
        , jb.job_id
        , jb.job_salary AS lowest_salary
        , RANK() OVER (PARTITION BY app.applicant_id ORDER BY jb.job_salary) AS ranked
        FROM application app
        JOIN job_posting jp ON jp.post_id = app.post_id
        JOIN job jb ON jb.job_id = jp.job_id
        JOIN applicant aplt ON aplt.applicant_id = app.applicant_id
    ) sub_q
    WHERE sub_q.ranked != 1
)
, most_experienced_cte AS (
    SELECT jb.job_id
    , jb.job_name
    , min_cte.applicant_id
    , min_cte.yrs_experience
    , RANK() OVER (PARTITION BY jb.job_id ORDER BY min_cte.yrs_experience DESC) AS ranked
    FROM job jb
    JOIN min_salary_cte min_cte ON min_cte.job_id = jb.job_id
)
SELECT job_id, job_name, applicant_id, yrs_experience FROM most_experienced_cte  WHERE ranked = 1;