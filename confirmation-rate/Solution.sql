/* Write your PL/SQL query statement below */
select s.user_id,round(avg(case when action = 'confirmed' then 1.0 else 0.0 end), 2) as confirmation_rate 
from signups s
left join Confirmations c1
on s.user_id=c1.user_id  
group by s.user_id

