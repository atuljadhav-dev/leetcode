/* Write your PL/SQL query statement below */
select ppp.product_id,nvl(pppp.new_price,10) price
from products ppp 
left join (select *
from products p
where change_date=(
    select max(pp.change_date)
    from products pp
    where pp.change_date<='2019-08-16'
    and  p.product_id=pp.product_id   
)) pppp
on ppp.product_id=pppp.product_id
group by ppp.product_id,pppp.new_price