select category, 
    count(category) as total_sales, 
    sum(amount) as total_revenue,
    round(avg(discount), 2) as avg_discount
from sales
group by category
order by total_revenue desc, category asc