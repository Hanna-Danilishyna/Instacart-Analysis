-- TOP 10 PRODUCTS

SELECT product_name, COUNT(*) AS times_ordered
FROM master_table
GROUP BY product_name
ORDER BY times_ordered DESC
LIMIT 10;


-- TOP DEPARTMENT

SELECT department, COUNT(*) AS total_orders
FROM master_table
GROUP BY department
ORDER BY total_orders DESC;