-- https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/

WITH cte_agg AS (
    SELECT reports_to
        , COUNT(*) AS reports_count
        , ROUND(AVG(age)) AS average_age
    FROM Employees
    GROUP BY reports_to
)
SELECT e.employee_id
, e.name
, ct.reports_count
, ct.average_age
FROM Employees e
JOIN cte_agg ct
ON e.employee_id = ct.reports_to
ORDER BY e.employee_id
;
