# Write your MySQL query statement below
SELECT *
FROM Patients
WHERE INSTR(conditions,'DIAB1') = 1 OR   INSTR(conditions,' DIAB1') > 0  