select customer, count(customer) as total_orders, sum(amount) as total_spent
from orders
group by customer
order by total_spent desc