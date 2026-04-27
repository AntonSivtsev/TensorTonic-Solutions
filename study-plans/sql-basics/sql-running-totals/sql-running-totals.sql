select account,
    txn_date,
    amount,
    sum(amount) over (partition by account order by txn_date) as running_total
from transactions
order by account asc, txn_date asc