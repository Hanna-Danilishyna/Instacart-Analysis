
-- AMOUNT OF ORDERS
SELECT COUNT (DISTINCT order_id) AS total_orders
FROM master_table;

-- AMOUNT OF USERS

SELECT COUNT(DISTINCT user_id) AS total_users
FROM master_table;

-- AVERAGE AMOUNT OF ITEMS PER ORDER
SELECT AVG(product_count) AS avg_products_per_order

FROM (SELECT order_id, COUNT(product_id) AS product_count
FROM master_table
GROUP BY order_id)
t;


