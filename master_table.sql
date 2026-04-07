DROP TABLE IF EXISTS order_products_all;
CREATE TABLE order_products_all AS
SELECT * FROM order_products_prior
UNION ALL
SELECT * FROM order_products_train;

DROP TABLE IF EXISTS orders_joined;
CREATE TABLE orders_joined AS
SELECT 
    o.order_id,
    o.user_id,
    o.order_number,
    o.order_dow,
    o.order_hour_of_day,
    o.days_since_prior_order,
    op.product_id,
    op.add_to_cart_order,
    op.reordered
FROM orders o
JOIN order_products_all op
ON o.order_id = op.order_id;

DROP TABLE IF EXISTS orders_products;
CREATE TABLE orders_products AS
SELECT 
    oj.*,
    p.product_name,
    p.aisle_id,
    p.department_id
FROM orders_joined oj
JOIN products p
ON oj.product_id = p.product_id;

DROP TABLE IF EXISTS master_table;
CREATE TABLE master_table AS
SELECT 
    op.*,
    a.aisle,
    d.department
FROM orders_products op
JOIN aisles a ON op.aisle_id = a.aisle_id
JOIN departments d ON op.department_id = d.department_id;

SELECT * FROM master_table
LIMIT 50000;
