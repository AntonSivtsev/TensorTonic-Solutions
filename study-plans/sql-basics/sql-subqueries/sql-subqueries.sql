select distinct(name),	
    price,	
    (price - (select avg(price) from products)) as vs_avg
from products inner join sales on products.id = sales.product_ID
Order by vs_avg desc, name asc