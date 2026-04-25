select username, 
    segment, 
    engagement_score,
    row_number() over (partition by segment order by engagement_score desc) as activity_rank
from user_activity
order by segment ASC, activity_rank asc