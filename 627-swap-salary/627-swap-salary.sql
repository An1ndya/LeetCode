# Write your MySQL query statement below
UPDATE Salary
SET sex = CASE
        when sex = 'm' Then 'f'
        else  'm'
        end