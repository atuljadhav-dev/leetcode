/* Write your PL/SQL query statement below */
select contest_id,round(count(*)/(select count(*) from users)*100,2) percentage 
from Register 
group by contest_id
order by count(*) desc,contest_id
