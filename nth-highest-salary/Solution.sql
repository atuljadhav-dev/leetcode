CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN
    /* Write your PL/SQL query statement below */
    select distinct salary into result
    from employee e
    where (
    select count(distinct ee.salary)
    from employee ee
    where e.salary<ee.salary
    )=N-1;
    RETURN result;
END;