# Write your MySQL query statement below
select p1.firstname, p1.lastname, a.city, a.state from Person p1 left join Address a on p1.personId=a.personId