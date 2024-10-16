-- https://leetcode.com/problems/primary-department-for-each-employee/
WITH cte_row_num AS (
    SELECT employee_id
    , department_id
    , ROW_NUMBER() OVER(PARTITION BY employee_id ORDER BY primary_flag DESC) as row_num
    FROM Employee
)
SELECT ct.employee_id, ct.department_id FROM cte_row_num ct WHERE ct.row_num = 1;
