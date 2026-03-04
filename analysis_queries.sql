use warehouse analyst_wh;
use database hyundai;
select * from customers limit 3;
select * from sales limit 3;
select * from vehicle limit 3;
select * from service limit 3;
--1.What is the average cost for each hyundai model
select v.model_name,avg(s.service_cost) as average_cost from vehicle as v join service as s on v.vehicle_id=s.vehicle_id group by v.model_name;
--2.What is the average cost for each engine_type
select v.engine_type,avg(s.service_cost) as average_cost from vehicle as v join service as s on v.vehicle_id=s.vehicle_id group by v.engine_type;
--3.What is the average cost for each segment
select v.segment,avg(s.service_cost) as average_cost from vehicle as v join service as s on v.vehicle_id=s.vehicle_id group by v.segment;
--4.which dealer regions handle the highest number of services
select dealer_region,count(*) as total_services from service group by dealer_region order by count(*) desc;
--5.which service type is most common across regions
select dealer_region,service_type,count(*) from service group by dealer_region,service_type order by dealer_region,count(*) desc;
--6.who are the top customers by number of service visits
select c.customer_id,c.name,count(distinct s.service_id) as total_count from service as s join sales as sa join customers c on sa.customer_id=c.customer_id group by c.customer_id,c.name order by total_count desc limit 10;
--7.Monthly service revenue trend
SELECT DATE_TRUNC('month', service_date) AS service_month, COUNT(service_id) AS total_services, SUM(service_cost) AS total_revenue,ROUND(AVG(service_cost), 2) AS avg_service_cost FROM SERVICE
GROUP BY service_month ORDER BY service_month;
--8.Top vehicle models by service revenue
SELECT v.model_name,COUNT(s.service_id) AS total_services,SUM(s.service_cost) AS total_revenue,
ROUND(AVG(s.service_cost), 2) AS avg_service_cost FROM SERVICE s JOIN VEHICLE v ON s.vehicle_id = v.vehicle_id GROUP BY v.model_name ORDER BY total_revenue DESC LIMIT 10;
--9.Rank dealer regions by service revenue
SELECT dealer_region,COUNT(service_id) AS total_services,SUM(service_cost) AS total_revenue,RANK() OVER (ORDER BY SUM(service_cost) DESC) AS revenue_rank FROM SERVICE GROUP BY dealer_region ORDER BY revenue_rank;
--10.customers who purchased more than one vehicle and show their total vehicles purchased and total amount spent
SELECT c.customer_id,c.name,COUNT(s.vehicle_id) AS total_vehicles_purchased,SUM(s.final_price) AS total_spent FROM CUSTOMERS c JOIN SALES s ON c.customer_id = s.customer_id GROUP BY c.customer_id,
c.name HAVING COUNT(s.vehicle_id) > 1 ORDER BY total_spent DESC;

