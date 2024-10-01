-- https://leetcode.com/problems/students-and-examinations/

SELECT
s.student_id
, s.student_name
, subs.subject_name
, COUNT(ex.student_id) AS attended_exams
FROM Students s
CROSS JOIN Subjects subs
LEFT JOIN Examinations ex
ON s.student_id = ex.student_id
    AND ex.subject_name = subs.subject_name
GROUP BY s.student_id, s.student_name, subs.subject_name
ORDER BY s.student_id, subs.subject_name;
