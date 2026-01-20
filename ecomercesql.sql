select * from orders limit 10;

describe orders;
SET SQL_SAFE_UPDATES = 0;
update orders set Date=STR_TO_DATE(Date,'%Y/%d/%m');

alter table orders modify column Date date; 

select 
count(Order_ID) as total_orders,
round(avg(Amount),2)as avg_order_value,
round(sum(Amount),2) as total_Amount
from orders;

select Category, round(sum(Amount),2) as total_Revenue,
round(count(Order_ID),2) as toatal_order_per_catedgory
from orders group by Category order by total_Revenue desc;

select monthname(Date) as month_name, 
round(sum(Amount),2) as total_revenue_per_month
from orders group by month_name order by month_name desc;

select Customer_ID, count(Order_ID) as total_order_per_customer
from orders group by Customer_ID order by total_order_per_customer desc limit 5 ;

select Order_ID,Category,Amount, round(sum(Amount)over(partition by Category),2) as total_revenue_per_Category
from orders;

select Order_ID,Amount,
case 
when Amount >1000  then 'Premiun'
WHEN Amount BETWEEN 500 AND 1000 THEN 'Standard'
else 
'Budget'

END as Order_Segment
FROM orders;