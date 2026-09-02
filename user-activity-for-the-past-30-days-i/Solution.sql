/* Write your PL/SQL query statement below */
select to_char(activity_date,'yyyy-mm-dd') as day,count(distinct user_id) active_users
from activity
where '2019-06-27'<activity_date
and activity_date<'2019-07-28'
group by activity_date
