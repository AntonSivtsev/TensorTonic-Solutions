select customer, count(customer) as total_orders, sum(amount) as total_spent
from orders
group by customer
having total_orders >= 2
order by total_spent desc