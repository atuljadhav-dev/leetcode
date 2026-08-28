/* Write your PL/SQL query statement below */
select customer_number
from (
    select customer_number,dense_rank() over (order by count(*) desc) r
    from orders
    group by customer_number
)  
where r=1