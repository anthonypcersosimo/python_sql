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
mycursor.execute(f'SELECT * FROM {table_name}')

result = mycursor.fetchall()

df = pd.DataFrame.from_records(
    result,
    columns=[i[0] for i in mycursor.description]
)

df.to_csv(r"C:\Users\Anthony's Razer\Desktop\Repositories\python_sql\csv\ec_universe_20190531_retail.csv")