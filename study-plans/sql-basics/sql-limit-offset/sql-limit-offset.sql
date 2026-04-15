-- Write your SQL query here
select product, revenue, sale_date
from sales
order by revenue desc, sale_date
limit 3 offset 1 