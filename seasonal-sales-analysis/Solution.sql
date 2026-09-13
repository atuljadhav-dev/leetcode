/* Write your PL/SQL query statement below */
select season ,category,total_quantity,total_revenue
from (select 
    'Winter' season,
    p.category,
    sum(quantity) total_quantity ,
    sum(quantity*price) total_revenue ,
    dense_rank() over (order by sum(quantity)desc,sum(quantity*price) desc) rk
from sales s
join products p
on s.product_id=p.product_id
where to_char(sale_date ,'mm') in ('12','01','02')
group by p.category
union
select 
    'Spring' season,
    p.category,
    sum(quantity) total_quantity ,
    sum(quantity*price)total_revenue ,
    dense_rank() over (order by sum(quantity)desc,sum(quantity*price) desc) rk
from sales s
join products p
on s.product_id=p.product_id
where to_char(sale_date ,'mm') in ('03','04','05')
group by p.category
union
select 
    'Summer' season,
    p.category,
    sum(quantity) total_quantity ,
    sum(quantity*price)total_revenue ,
    dense_rank() over (order by sum(quantity)desc,sum(quantity*price) desc) rk
from sales s
join products p
on s.product_id=p.product_id
where to_char(sale_date ,'mm') in ('06','07','08')
group by p.category
union
select 
    'Fall' season,
    p.category,
    sum(quantity) total_quantity ,
    sum(quantity*price)total_revenue ,
    dense_rank() over (order by sum(quantity)desc,sum(quantity*price) desc) rk
from sales s
join products p
on s.product_id=p.product_id
where to_char(sale_date ,'mm') in ('09','10','11')
group by p.category)
where rk=1