with a as (select customer,
    count(customer) as order_count,	
    sum(amount) as total_spent
    from orders
    group by customer
)

select *
from a
where order_count > 1
Order by total_spent desc, customer asc