-- ORDERS BY THE DAY OF THE WEEK

SELECT CASE order_dow
        WHEN 0 THEN 'Sunday'
        WHEN 1 THEN 'Monday'
        WHEN 2 THEN 'Tuesday'
        WHEN 3 THEN 'Wednesday'
        WHEN 4 THEN 'Thursday'
        WHEN 5 THEN 'Friday'
        WHEN 6 THEN 'Saturday'
    END AS day_of_week, COUNT(DISTINCT order_id) AS total_orders
FROM master_table
GROUP BY order_dow
ORDER BY order_dow;

-- ORDERS BY HOUR

SELECT 
    order_hour_of_day,
    LPAD(order_hour_of_day::text, 2, '0') || ':00 - ' ||
    LPAD((order_hour_of_day + 1)::text, 2, '0') || ':00' AS hour_interval,
    COUNT(DISTINCT order_id) AS total_orders
FROM master_table
GROUP BY order_hour_of_day
ORDER BY order_hour_of_day;