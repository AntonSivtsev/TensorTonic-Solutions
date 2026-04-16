-- Write your SQL query here
select name, salary, dept_name
from employees inner join departments on employees.dept_id = departments.id