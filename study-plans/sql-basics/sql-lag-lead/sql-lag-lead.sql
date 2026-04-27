select month, 
    revenue,	
    Lag(revenue, 1, 0) over (order by month) as prev_revenue,
    (revenue - prev_revenue) as revenue_change
from monthly_revenue
order by month