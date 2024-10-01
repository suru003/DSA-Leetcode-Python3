-- https://leetcode.com/problems/consecutive-numbers/

WITH plus_1 AS (
    SELECT id + 1 AS id,
    num
    FROM Logs
),
plus_2 AS (
    SELECT id + 2 AS id,
    num
    FROM Logs
)

SELECT DISTINCT l.num AS ConsecutiveNums
FROM Logs l
JOIN plus_1 p1
ON l.id = p1.id AND l.num = p1.num
JOIN plus_2 p2
ON l.id = p2.id AND l.num = p2.num;


-- Another
SELECT
DISTINCT num AS ConsecutiveNums
FROM (
    SELECT
        id,
        LAG(num, 1) OVER (ORDER BY id) AS PrevNum,
        num,
        LEAD(num, 1) OVER (ORDER BY id) AS NextNum
    FROM Logs) log
WHERE num = PrevNum AND num = NextNum
;