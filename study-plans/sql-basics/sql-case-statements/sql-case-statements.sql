select username,
    session_count,
    (case
    when session_count >= 50 then 'Power'
    when session_count >= 10 then 'Casual'
    else 'Dormant'
    end) as 'activity_level',
    (case
    when platform = 'ios' or platform = 'android' then 'Mobile'
    when platform = 'web' or platform = 'desktop' then 'Desktop'
    else 'Other'
    end) as platform_type
from user_sessions
ORDER BY CASE activity_level
             WHEN 'Power'   THEN 1
             WHEN 'Casual'  THEN 2
             WHEN 'Dormant' THEN 3
             ELSE 4
         END, username asc