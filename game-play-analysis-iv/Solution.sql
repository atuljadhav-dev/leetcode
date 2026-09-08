/* Write your PL/SQL query statement below */
SELECT ROUND(
    COUNT(DISTINCT CASE WHEN event_date = first_login + 1 THEN player_id END) 
    / 
    COUNT(DISTINCT player_id), 
    2
) AS fraction
FROM (
    SELECT player_id,
           event_date,
           MIN(event_date) OVER(PARTITION BY player_id) AS first_login
    FROM Activity
);