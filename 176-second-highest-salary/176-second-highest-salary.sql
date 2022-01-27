/* Write your PL/SQL query statement below */

SELECT MAX (salary) AS SecondHighestSalary
FROM Employee 
WHERE Salary NOT IN (SELECT Max (salary) FROM Employee);