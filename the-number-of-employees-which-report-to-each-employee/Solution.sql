/* Write your PL/SQL query statement below */
select m.employee_id,m.name,count(*) reports_count,round(avg(e.age)) average_age
from employees m
join employees e
on m.employee_id=e.reports_to
group by m.employee_id,m.name
order by m.employee_id