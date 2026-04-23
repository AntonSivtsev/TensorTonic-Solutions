select u.username, e.experiment_name, e.variant, c.revenue
from users u
inner join experiment_assignments e on u.id = e.user_id
inner join conversions c on e.user_id = c.user_ID
order by e.experiment_name asc, revenue desc, username asc