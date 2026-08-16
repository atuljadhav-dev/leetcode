/* Write your PL/SQL query statement below */
select project_id,round(avg(experience_years),2) as average_years 
from employee e
inner join project p
on e.employee_id=p.employee_id
group by project_id;