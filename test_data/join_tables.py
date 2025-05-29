# # GMAS STANDS FOR GRAB-MANIPULATE-AND-SAVE !!

import sqlite3
import pandas as pd
import mysql.connector
print('connected!')

f = open("secret.txt", "r")
if f.mode == "r":
    secret = f.read()

# Use table name
db_name = 'ecs_downloads'
mydb = mysql.connector.connect(
    user='root',
    password=secret,
    host='127.0.0.1',
    database='python'
)
print(mydb)

# Create a cursor (an instance) to manipulate your SQL Database
mycursor = mydb.cursor(buffered=True)

# Second database name for join
db_second = 'ecs'
table_name_second = 'ec_universe_20191231'
join_field = 'sedol'

# Declare table name and query
table_name = 'preferred_fields_dl'
query = f'SELECT * FROM {db_name}.{table_name} JOIN {db_second}.{table_name_second} ON {table_name_second}.{join_field} = {table_name}.{join_field}'

# Pass query into the cursor to execute and fetch the result
mycursor.execute(query)

result = mycursor.fetchall()

# Create data frame from result
df = pd.DataFrame.from_records(
    result,
    columns=[i[0] for i in mycursor.description]
)

sector_eps = df.groupby('abv_gics_sector')['eps_cfy'].sum()

print('Total EPS by Sector:')
print(sector_eps)

# Save dataframe to CSV format
# df.to_csv(r"C:\Users\Anthony's Razer\Desktop\Repositories\python_sql\csv\example.csv")