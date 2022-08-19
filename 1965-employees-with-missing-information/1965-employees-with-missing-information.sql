/* Write your PL/SQL query statement below */
(select employee_id from employees 
union 
select employee_id from salaries)
minus
(select employee_id from employees
intersect
select employee_id from salaries)
order by employee_id asc;