# # GMAS STANDS FOR GRAB-MANIPULATE-AND-SAVE !!

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

# Declare table name and query
table_name = 'ec_universe_20191231'
query = f'SELECT * FROM {table_name}'

# Pass query into the cursor to execute and fetch the result
mycursor.execute(query)

result = mycursor.fetchall()

# Create data frame from resul
df = pd.DataFrame.from_records(
    result,
    columns=[i[0] for i in mycursor.description]
)

# print(df)

# Save dataframe to CSV format
# df.to_csv(r"C:\Users\Anthony's Razer\Desktop\Repositories\python_sql\csv\example.csv")