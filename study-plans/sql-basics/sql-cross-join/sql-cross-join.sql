select s.segment_name, m.metric_name
from segments s
cross join metrics m
Order by segment_name asc, metric_name asc