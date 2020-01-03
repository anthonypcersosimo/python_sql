import sqlite3
import pandas as pd
import mysql.connector
print('connected!')

f = open("secret.txt", "r")
if f.mode == "r":
    secret = f.read()

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

# # SELECT ONLY CERTAIN FIELDS ===========================

table_name = 'ec_universe_20191231'
mycursor.execute(f'SELECT un_adj_ticker, record_date, dividend_yield, abv_gics_sector, mkt_cap_class  FROM {table_name}')

result = mycursor.fetchall()

df = pd.DataFrame.from_records(
    result,
    columns=[i[0] for i in mycursor.description]
)

sector_yield = df.groupby('abv_gics_sector')['dividend_yield'].mean()

print(sector_yield)

# sector_yield.to_csv(r"C:\Users\Anthony's Razer\Desktop\Repositories\python_sql\csv\sector_yield_check.csv")