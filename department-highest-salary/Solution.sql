/* Write your PL/SQL query statement below */
select d.name as Department,e.name as Employee,e.salary
from employee e
join department d
on e.departmentId=d.id
where e.salary in (
    select max(salary)
    from employee ee
    where ee.departmentId=e.departmentId
)