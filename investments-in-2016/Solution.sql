/* Write your PL/SQL query statement below */
-- select round(sum(tiv_2016),2) tiv_2016
-- from insurance ii
-- where tiv_2015 in (
-- select tiv_2015
-- from insurance
-- group by tiv_2015
-- having count(*)>1
-- )
-- and (
--     select count(*)
--     from insurance i
--     where i.lat=ii.lat
--     and ii.lon=i.lon
-- )=1

select round(sum(tiv_2016), 2) tiv_2016 
from
(
select count(1) over (partition by tiv_2015) c_2015,
       count(1) over (partition by lat, lon) c_latlon,
       tiv_2016
from Insurance
)
where c_2015>1 and c_latlon=1