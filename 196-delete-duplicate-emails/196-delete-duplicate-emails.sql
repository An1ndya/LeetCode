# Write your MySQL query statement below

DELETE P1 FROM Person P1
INNER JOIN Person P2 
WHERE P1.id > P2.id AND P1.email = P2.email;