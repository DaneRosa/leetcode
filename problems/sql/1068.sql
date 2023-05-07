-- # Write your MySQL query statement below
-- # Write an SQL query that reports the product_name, year, and price for each sale_id in the Sales table.
select p.product_name, s.year, s.price
from Sales s
join Product p on p.product_id = s.product_id