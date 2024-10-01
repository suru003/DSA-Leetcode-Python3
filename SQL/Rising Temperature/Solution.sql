-- https://leetcode.com/problems/rising-temperature/

SELECT w1.id
FROM Weather w1
WHERE w1.temperature >
    (
        SELECT w2.temperature
        FROM Weather w2
        WHERE w1.recordDate = w2.recordDate + 1
    );


-- QUALIFY with LAG
SELECT id
FROM Weather
QUALIFY temperature > LAG(temperature) OVER (ORDER BY recordDate);
