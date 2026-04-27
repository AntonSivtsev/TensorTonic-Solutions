select name,
    (case when email is null then 'N/A' else email end) as display_email,
    (case when deactivated_at is null then 'active' else 'inactive' end) as status
from customers
where phone is not null
order by name