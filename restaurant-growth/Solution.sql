/* Write your PL/SQL query statement below */
select to_char(visited_on,'yyyy-mm-dd') visited_on,(
    select sum(amount)
    from customer cc
    where cc.visited_on>=c.visited_on-6 and cc.visited_on<=c.visited_on
) amount,(
    select round(sum(amount)/7,2)
    from customer cc
    where cc.visited_on>=c.visited_on-6 and cc.visited_on<=c.visited_on
) average_amount
from customer c
where (
    select count(distinct ccc.visited_on)
    from customer ccc
    where c.visited_on>ccc.visited_on
)>=6
group by visited_on
order by visited_on