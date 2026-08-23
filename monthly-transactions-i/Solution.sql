/* Write your PL/SQL query statement below */
select 
    TO_CHAR(trans_date, 'YYYY-MM') month,
    country,
    COUNT(*) trans_count,
    SUM(case WHEN state='approved' then 1 else 0 end)  approved_count,
    sum(amount) trans_total_amount ,
    sum(case when state='approved' then amount else 0 end) approved_total_amount
from transactions
group by TO_CHAR(trans_date, 'YYYY-MM'),country
