-- Write your SQL query here
select customers.name, customers.city, coalesce (SUM(orders.amount), 0) as total_spent
from customers left join orders on customers.id = orders.customer_id
group by name, city
order by total_spent Desc, name