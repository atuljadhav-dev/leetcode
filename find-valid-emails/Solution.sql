/* Write your PL/SQL query statement below */
select *
from users
where regexp_like(email,'^[a-zA-Z0-9]+@[a-zA-Z]+\.com$')
order by user_id;