/* Write your PL/SQL query statement below */
select product_id,year first_year,quantity,price
from sales s
where year= (
    select min(year)
    from sales ss
    where s.product_id=ss.product_id
)