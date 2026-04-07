import pandas as pd
from sqlalchemy import create_engine

# CONNECT POSTGRE
db_user = "postgres"
db_password = ""  # если пароль не установлен
db_host = "localhost"
db_port = "5432"
db_name = "instacart_analysis"

engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

# CSV PATH
data_path = "/Users/ankapdf/Desktop/Instacart Market Analysis/Raw_data/"

csv_files = {
    "aisles": "aisles.csv",
    "departments": "departments.csv",
    "products": "products.csv",
    "orders": "orders.csv",
    "order_products_prior": "order_products__prior.csv",
    "order_products_train": "order_products__train.csv"
}

table_columns = {
    "aisles": ["aisle_id", "aisle"],
    "departments": ["department_id", "department"],
    "products": ["product_id", "product_name", "aisle_id", "department_id"],
    "orders": ["order_id", "user_id", "order_number", "order_dow", "order_hour_of_day", "days_since_prior_order"],
    "order_products_prior": ["order_id", "product_id", "add_to_cart_order", "reordered"],
    "order_products_train": ["order_id", "product_id", "add_to_cart_order", "reordered"]
}

# LINE LIMIT
max_rows = 300_000

# LOAD LIGHT TABLES
for table_name in ["aisles", "departments", "products"]:
    df = pd.read_csv(f"{data_path}{csv_files[table_name]}")
    df = df[table_columns[table_name]]
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"{table_name} uploaded: {len(df)} rows.")

# LIMIT FOR THE HEAVY DATA
orders_df = pd.read_csv(f"{data_path}{csv_files['orders']}")
orders_df = orders_df[table_columns["orders"]]

if len(orders_df) > max_rows:
    orders_df = orders_df.sample(n=max_rows, random_state=42)  

orders_df.to_sql("orders", engine, if_exists="replace", index=False)
print(f"orders uploaded: {len(orders_df)} rows.")


limited_order_ids = set(orders_df['order_id'])


# 6. Loading order_products_prior and order_products_train for the chosen orders

for table_name in ["order_products_prior", "order_products_train"]:
    df = pd.read_csv(f"{data_path}{csv_files[table_name]}")
    df = df[table_columns[table_name]]
    df = df[df['order_id'].isin(limited_order_ids)]  
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"{table_name} loaded: {len(df)} rows.")

print("All tables are loaded with a limit in 300_000 rows")