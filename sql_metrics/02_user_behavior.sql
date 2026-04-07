-- AVERAGE ORDERS PER USER

SELECT AVG(order_count) AS avg_orders_per_users
FROM (SELECT user_id, COUNT(DISTINCT order_id) AS order_count
FROM master_table
GROUP BY user_id) t;

