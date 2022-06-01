# Write your MySQL query statement below
SELECT U.name, SUM(T.amount) AS balance
FROM Users U JOIN Transactions T ON U.account = T.account       
GROUP BY U.account
HAVING balance > 10000