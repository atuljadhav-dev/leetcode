/* Write your PL/SQL query statement below */
select user_id buyer_id,to_char(join_date,'yyyy-mm-dd') join_date,count(order_id) orders_in_2019 
from users u
left join (
    select *
    from orders
    where order_date like '2019%'
) o
on u.user_id=o.buyer_id
group by user_id,join_date