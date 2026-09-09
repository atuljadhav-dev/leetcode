/* Write your PL/SQL query statement below */
-- Select player_id,to_char(min(event_date),'yyyy-mm-dd') as first_login
-- from Activity group by player_id;
select distinct player_id,to_char(event_date,'yyyy-mm-dd') first_login
from activity a
where event_date=(
    select min(aa.event_date)
    from activity aa
    where a.player_id=aa.player_id
)