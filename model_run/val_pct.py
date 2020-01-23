import sqlite3
import pandas as pd
import mysql.connector
print('connected!')

f = open("secret.txt", "r")
if f.mode == "r":
    secret = f.read()

# Use table name
db_name = 'ecs'
mydb = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    db=db_name,
    use_unicode='true',
    username='root',
    passwd=secret
)
print(mydb)

# Create a cursor (an instance) to manipulate your SQL Database
mycursor = mydb.cursor(buffered=True)

# Declare table name and query 43830
table_name = 'ec_universe_20191231'
query = f'SELECT last_known_ticker, record_date, unique_id, name, mkt_cap_class, ev_ebitda_ratio, ev_sales_ratio, pe_ratio, price_cf_ratio, price_bv_ratio FROM {table_name}'

# Pass query into the cursor to execute and fetch the result
mycursor.execute(query)

result = mycursor.fetchall()

# Create data frame from result
df = pd.DataFrame.from_records(
    result,
    columns=[i[0] for i in mycursor.description]
)

# Create a column for each field being ranked and rank the multiples ascending by mkt_cap_class
df['eve_rank'] = df.groupby('mkt_cap_class')['ev_ebitda_ratio'].rank(ascending=True, pct=True)
df['evs_rank'] = df.groupby('mkt_cap_class')['ev_sales_ratio'].rank(ascending=True, pct=True)
df['pe_rank'] = df.groupby('mkt_cap_class')['pe_ratio'].rank(ascending=True, pct=True)
df['pcf_rank'] = df.groupby('mkt_cap_class')['price_cf_ratio'].rank(ascending=True, pct=True)
df['pbv_rank'] = df.groupby('mkt_cap_class')['price_bv_ratio'].rank(ascending=True, pct=True)
df['avg'] = df.iloc[:,10:15].mean(axis=1)
df['val_pct'] = df.groupby('mkt_cap_class')['avg'].rank(ascending=True, pct=True)

# print(df)

# # Save dataframe to CSV format
df.to_csv(r"C:\Users\Anthony's Razer\Desktop\Repositories\python_sql\csv\example.csv")