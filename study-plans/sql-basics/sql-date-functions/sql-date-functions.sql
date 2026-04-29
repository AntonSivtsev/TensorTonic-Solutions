select username,
    signup_date, 
    EXTRACT(YEAR FROM signup_date) as signup_year,
    EXTRACT(month FROM signup_date) as signup_month, 
    extract(quarter from signup_date) as signup_quarter,
    DATE_TRUNC('month', signup_date) as cohort_month
from signups
Order by signup_date asc, username asc