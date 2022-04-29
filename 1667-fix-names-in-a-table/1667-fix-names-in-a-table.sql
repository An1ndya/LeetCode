# Write your MySQL query statement below

SELECT user_id, CONCAT(UCASE(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM Users 
ORDER BY user_id
