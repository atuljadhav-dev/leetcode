select t1.product_id,product_name
from Product t1 
join Sales t2
on t1.product_id=t2.product_id 
group by t1.product_id,product_name
having min(sale_date) >= '2019-01-01' 
and max(sale_date) <= '2019-03-31'