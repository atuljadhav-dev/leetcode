/* Write your PL/SQL query statement below */
select nvl(e.employee_id, s.employee_id) employee_id
from employees e
full join salaries s
on e.employee_id=s.employee_id
where e.name is null
or s.salary is null
order by employee_id;