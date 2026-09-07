/* Write your PL/SQL query statement below */
select to_char(event_day, 'yyyy-mm-dd') day, emp_id, sum(out_time-in_time) total_time
from employees
group by emp_id, event_day