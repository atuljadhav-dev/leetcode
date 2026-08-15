/* Write your PL/SQL query statement below */
select a.machine_id,round(avg(ac.timestamp-a.timestamp),3) processing_time 
from activity a
join activity ac
on a.machine_id=ac.machine_id and a.activity_type='start' and ac.activity_type='end' group by a.machine_id;