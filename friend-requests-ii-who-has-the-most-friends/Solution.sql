/* Write your PL/SQL query statement below */
WITH T1 AS 
(
    SELECT requester_id AS ID FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS ID FROM RequestAccepted
)

SELECT * FROM (SELECT ID , COUNT(ID) AS NUM FROM T1 GROUP BY ID ORDER BY NUM DESC ) WHERE ROWNUM=1

