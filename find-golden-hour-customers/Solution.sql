/* Write your PL/SQL query statement below */
select 
    customer_id,
    count(*) total_orders,
    round(avg(
        case when to_char(order_timestamp,'HH24:MI') between '11:00' and '14:00'   then 1 
        when to_char(order_timestamp,'HH24:MI') between '18:00' and '21:00'   then 1
        else 0
        end
        )*100) peak_hour_percentage,
    round(avg(order_rating),2) average_rating

from restaurant_orders
group by customer_id
having count(*)>2
and count(order_rating )>count(*)/2
and avg(order_rating)>=4
and avg(
        case when to_char(order_timestamp,'HH24:MI') between '11:00' and '14:00'   then 1 
        when to_char(order_timestamp,'HH24:MI') between '18:00' and '21:00'   then 1
        else 0
        end) >0.6 
order by average_rating desc, customer_id desc