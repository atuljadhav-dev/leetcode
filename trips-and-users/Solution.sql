/* Write your PL/SQL query statement below */
select request_at day, round(sum(case when status!='completed' then 1 else 0 end)/count(*),2)  "Cancellation Rate"
from trips t
join users c
on t.client_id=c.users_id
join users d
on t.driver_id=d.users_id
where c.banned='No' and d.banned='No'
and request_at between '2013-10-01' and '2013-10-03'
group by request_at