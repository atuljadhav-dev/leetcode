/* Write your PL/SQL query statement below */
select 
    round(
        avg(
            case when order_date=customer_pref_delivery_date 
            then 1 else 0 end
            )*100
        ,2) immediate_percentage 
from (
    select 
        rank() over (partition by customer_id order by order_date) rn,
        order_date ,customer_pref_delivery_date 
    from Delivery )
where rn=1