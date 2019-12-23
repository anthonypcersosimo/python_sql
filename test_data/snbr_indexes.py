import sqlite3
import pandas as pd
import mysql.connector
print('connected!')

f = open("secret.txt", "r")
if f.mode == "r":
    secret = f.read()

table_name = 'sn_buy_rated'
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

# # SELECT DATA FROM DATABASE ===========================
# Need indexes for
# SPX

# All Stifel Buy Rated Stocks
# Stifel Buy + VALUE
# Stifel BUY + Growth
# EC Stifel Value 12
# EC Stifel Growth 12

mycursor.execute(f'SELECT * FROM {table_name} WHERE mpt_class LIKE "%V%" LIMIT 30')

result = mycursor.fetchall()

df = pd.DataFrame.from_records(
    result,
    columns=[i[0] for i in mycursor.description]
)

df['mvd_sector_rank'] = df.groupby('gics_sector')['mean_valuation_deviation'].rank(ascending=False)
print(df)

# df.to_csv(r"C:\Users\Anthony's Razer\Desktop\Repositories\python_sql\csv\sn_buy_value.csv")