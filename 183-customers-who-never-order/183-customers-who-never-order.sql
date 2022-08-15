/* Write your PL/SQL query statement below */
select name customers from customers where id not in (select distinct customerId from orders);