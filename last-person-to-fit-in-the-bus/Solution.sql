/* Write your PL/SQL query statement below */
select person_name 
from(
    select person_name,s 
    from (
        select person_name,
                sum(weight) over(order by turn asc) as s 
        from Queue )
    where s <=1000 
    order by s desc )
where rownum=1;
