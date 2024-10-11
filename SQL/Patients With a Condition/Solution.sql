-- https://leetcode.com/problems/patients-with-a-condition/
SELECT patient_id, patient_name, conditions
FROM patients p
WHERE EXISTS (
   SELECT 1
    FROM unnest(string_to_array(p.conditions, ' ')) AS condition
    WHERE condition ILIKE 'diab1%'
);
