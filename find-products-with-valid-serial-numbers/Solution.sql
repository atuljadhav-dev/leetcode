/* Write your PL/SQL query statement below */
select *
from products
where regexp_like(description ,'(^| )SN[0-9]{4}-[0-9]{4}($| )')
order by product_id