/* Write your PL/SQL query statement below */
select name,sum(amount) balance
from users u
join transactions t
on u.account=t.account
group by t.account, name
having sum(amount)>10000