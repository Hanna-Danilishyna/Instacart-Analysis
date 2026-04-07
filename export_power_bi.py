import os
import pandas as pd
from sqlalchemy import create_engine

# CONNECT POSTGRE
db_user = "postgres"
db_password = ""  
db_host = "localhost"
db_port = "5432"
db_name = "instacart_analysis"

engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

# EXPORT PATH
export_path = "/Users/ankapdf/Desktop/Instacart Market Analysis/Prepared/"
os.makedirs(export_path, exist_ok=True)

# SQL REQUESTS
sql_queries = {
    "total_orders": """
        SELECT COUNT(DISTINCT order_id) AS total_orders
        FROM master_table;
    """,
    "total_users": """
        SELECT COUNT(DISTINCT user_id) AS total_users
        FROM master_table;
    """,
    "avg_products_per_order": """
        SELECT AVG(product_count) AS avg_products_per_order
        FROM (
            SELECT order_id, COUNT(product_id) AS product_count
            FROM master_table
            GROUP BY order_id
        ) t;
    """,
    "avg_orders_per_user": """
        SELECT AVG(order_count) AS avg_orders_per_user
        FROM (
            SELECT user_id, COUNT(DISTINCT order_id) AS order_count
            FROM master_table
            GROUP BY user_id
        ) t;
    """,
    "top_10_products": """
        SELECT product_name, COUNT(*) AS times_ordered
        FROM master_table
        GROUP BY product_name
        ORDER BY times_ordered DESC
        LIMIT 10;
    """,
    "top_department": """
        SELECT department, COUNT(*) AS total_orders
        FROM master_table
        GROUP BY department
        ORDER BY total_orders DESC;
    """,
    "orders_by_dow": """
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
    """,
    "orders_by_hour": """
        SELECT order_hour_of_day,
        LPAD(order_hour_of_day::text, 2, '0') || ':00 - ' ||
        LPAD((order_hour_of_day + 1)::text, 2, '0') || ':00' AS hour_interval,
        COUNT(DISTINCT order_id) AS total_orders
        FROM master_table
        GROUP BY order_hour_of_day
        ORDER BY order_hour_of_day;
    """,
    
    
    "reorder_rate": """
        SELECT AVG(reordered) AS reorder_rate
        FROM master_table;
    """,
    "reorder_rate_by_department": """
        SELECT department, AVG(reordered) AS reorder_rate
        FROM master_table
        GROUP BY department
        ORDER BY reorder_rate DESC;
    """,
    "top_10_loyal_products": """
        SELECT product_name, AVG(reordered) AS reorder_rate, COUNT(*) AS total_orders
        FROM master_table
        GROUP BY product_name
        HAVING COUNT(*) > 100
        ORDER BY reorder_rate DESC
        LIMIT 10;
    """
}

# EXPORT TO CSV IF DOESN'T EXIST
overwrite = True
for name, query in sql_queries.items():
    file_path = os.path.join(export_path, f"{name}.csv")
    
    
    if os.path.exists(file_path) and not overwrite:
        print(f" {name}.csv ALREADY EXISTS")
        continue
    
    df = pd.read_sql(query, engine)
    df.to_csv(file_path, index=False)
    
    print(f"{name}.csv saved: {len(df)} rows")

print("Successfully exported")