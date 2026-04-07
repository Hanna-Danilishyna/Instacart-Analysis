-- REORDER RATE

SELECT AVG(reordered) AS reorder_rate
FROM master_table;

-- REORDER RATE BY THE DEPARTMENT

SELECT department, AVG(reordered) AS reorder_rate
FROM master_table
GROUP BY department
ORDER BY reorder_rate DESC;

-- TOP 10 "LOYAL" PRODUCTS

SELECT product_name, AVG(reordered) AS reorder_rate, COUNT(*) AS total_orders
FROM master_table
GROUP BY product_name
HAVING COUNT(*)>100
ORDER BY reorder_rate DESC
LIMIT 10;
