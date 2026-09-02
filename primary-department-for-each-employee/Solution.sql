/* Write your PL/SQL query statement below */
select employee_id,department_id
from employee e
where  (
    select count(department_id)
    from employee ee
    where e.employee_id=ee.employee_id
)=1
or department_id=(select department_id
    from employee ee
    where e.employee_id=ee.employee_id
    and primary_flag='Y');