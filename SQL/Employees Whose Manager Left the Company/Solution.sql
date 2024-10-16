-- https://leetcode.com/problems/employees-whose-manager-left-the-company/
SELECT e.employee_id
FROM Employees e
WHERE 1 = 1
AND e.manager_id IS NOT NULL
AND e.salary < 30000
AND NOT EXISTS
    (
        SELECT 1 FROM Employees e2
        WHERE e.manager_id = e2.employee_id
    )
ORDER BY e.employee_id
;