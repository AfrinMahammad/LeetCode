# Write your MySQL query statement below
select name customers from customers where id not in (select distinct customerId from orders);