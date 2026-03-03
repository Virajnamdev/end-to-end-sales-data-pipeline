create database company_data;
use company_data;
show tables;
select*from company_data_cleaned limit 10; 

create view view_data as
select
   date,
   YEAR(date) as year,
   MONTH(date) as month,
   DAY(date) as day,
   DATE_FORMAT(date,'%Y-%m') as d_format,
   title,
   artist,
   purchase_price,
   sale_price,
   (sale_price - purchase_price) as profit,
   ((sale_price - purchase_price)/purchase_price)*100 as profit_margin,
   gross_appreciation_multiplier,
   gross_appreciation_period
from company_data_cleaned; 



 


   

