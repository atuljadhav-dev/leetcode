/* Write your PL/SQL query statement below */
select 
    c1.category category1,
    c2.category category2, 
    count(distinct p1.user_id) customer_count -- for pid1,pid2=pid2,pid1 distinct remove that
from productpurchases p1
join productpurchases p2
on p1.user_id=p2.user_id 
and p1.product_id!=p2.product_id
join productInfo c1
on p1.product_id=c1.product_id
join productinfo c2
on p2.product_id=c2.product_id
where c1.category<c2.category
group by c1.category,c2.category
having count(distinct p1.user_id)>2
order by customer_count desc, category1 asc,category2 asc