/*
combine two tables
Write an SQL query to report the first name, last name, city, and state of each person in the Person table. 
If the address of a personId is not present in the Address table, report null instead.

Return the result table in any order.

The query result format is in the following example.

*/ 


select p.firstName, p.lastName, a.city, state
from Person p
left join Address a on a.personId = p.personId



