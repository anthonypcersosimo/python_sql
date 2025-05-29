# # GMAS STANDS FOR GRAB-MANIPULATE-AND-SAVE !!
import pandas as pd
import mysql.connector
print('connected!')

f = open("secret.txt", "r")
if f.mode == "r":
    secret = f.read()

mydb = mysql.connector.connect(
    user='root',
    password=secret,
    host='127.0.0.1',
    database='python'
)
print(mydb)

# Create a cursor (an instance) to manipulate your SQL Database
mycursor = mydb.cursor(buffered=True)

# Declare table name and query
table_name = 'russell3000'
query = f'SELECT * FROM {table_name}'

# Pass query into the cursor to execute and fetch the result
mycursor.execute(query)

result = mycursor.fetchall()

# Create data frame from result
df = pd.DataFrame.from_records(
    result,
    columns=[i[0] for i in mycursor.description]
)

print(df)

# Save dataframe to CSV format
# df.to_csv(r"C:\Users\Anthony's Razer\Desktop\Repositories\python_sql\csv\example.csv")