with tb as (
    select order_date, 
    count(order_date) as daily_count,
    sum(amount) as daily_revenue
    from orders
    group by order_date
)

select avg(daily_count) as avg_daily_orders,
    avg(daily_revenue) as avg_daily_revenue,
    max(daily_count) as busiest_day_orders
from tb