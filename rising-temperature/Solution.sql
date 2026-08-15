-- # Write your MySQL query statement below
select we.id as Id
from weather w
join weather we
on we.recordDate =w.recordDate +1 and w.temperature<we.temperature;
