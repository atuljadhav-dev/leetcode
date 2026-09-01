/* Write your PL/SQL query statement below */
select name,sum(nvl(distance,0)) travelled_distance
from users u
left join rides r
on u.id=r.user_id
group by name,u.id
order by sum(nvl(distance,0)) desc,name asc