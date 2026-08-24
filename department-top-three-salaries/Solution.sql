/* Write your PL/SQL query statement below */
select d.name Department,e.name Employee ,e.salary
from employee e
join department d
on e.departmentId=d.id
left join (
    select salary,
    departmentId
    from employee e
    where (select count(distinct e1.salary)
    from employee e1
    where e.salary<e1.salary and e.departmentId=e1.departmentId)=2 
    group by salary, departmentId) s
on d.id=s.departmentId
where e.salary>=s.salary or s.salary is null