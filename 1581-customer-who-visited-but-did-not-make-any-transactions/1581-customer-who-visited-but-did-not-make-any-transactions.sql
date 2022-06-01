/* Write your T-SQL query statement below */
SELECT Distinct V.customer_id, count(V.visit_id ) as  count_no_trans 
FROM Visits V 
WHERE V.visit_id NOT IN (SELECT visit_id FROM Transactions)
GROUP BY V.customer_id 