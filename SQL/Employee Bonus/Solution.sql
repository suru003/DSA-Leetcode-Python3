-- https://leetcode.com/problems/employee-bonus/

SELECT e.name
, b.bonus
FROM Employee e
LEFT JOIN Bonus b
ON e.empId = b.empId
WHERE 1 = 1
    AND b.empId IS NULL
    OR b.bonus < 1000;
