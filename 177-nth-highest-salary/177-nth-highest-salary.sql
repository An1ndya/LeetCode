CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE P INT;
    SET P = N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT salary AS getNthHighestSalary FROM Employee ORDER BY salary DESC LIMIT P,1
  );
END