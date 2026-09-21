/* Write your PL/SQL query statement below */
select 
    p1.product_id product1_id,
    p2.product_id product2_id,
    c1.category product1_category,
    c2.category product2_category, 
    count(*) customer_count
from productpurchases p1
join productpurchases p2
on p1.user_id=p2.user_id
join productInfo c1
on p1.product_id=c1.product_id
join productinfo c2
on p2.product_id=c2.product_id
where p1.product_id<p2.product_id
group by p1.product_id,p2.product_id,c1.category,c2.category
having count(*)>2
order by count(*) desc,p1.product_id asc,p2.product_id asc