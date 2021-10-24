SELECT DISTINCT MAX(salary) AS SecondHighestSalary
  FROM Employee a
 WHERE Salary< (SELECT MAX(salary) FROM Employee b WHERE b.salary > a.salary)
