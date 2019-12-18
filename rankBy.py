import sqlite3
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

f = open('secret.txt', 'r')
if f.mode == 'r':
    secret = f.read()

db_name = 'stocks'
table_name = 'russell3000'

mydb = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    db=db_name,
    use_unicode='true',
    username='root',
    passwd=secret
)

if mydb:
    print(f'Connected to SQL Database: {db_name}')

# Create a cursor (an instance) to manipulate your SQL Database
mycursor = mydb.cursor(buffered=True)

# Rank Sector by Price ===============

# Start by building your query, then executing it and storing the result in a variable
query = f'SELECT * FROM {table_name}'
mycursor.execute(query)

result = mycursor.fetchall()
# print(result, '==============================')

# Convert MySQL data into DataFrame WITH headers
df = pd.DataFrame.from_records(
    result, columns=[i[0] for i in mycursor.description])
# print(df)

# Create a column called Price_Rank and rank the price descending by Sector
df['Price_Rank'] = df.groupby('Sector')['Price'].rank(ascending=False)

# Create a column called Price_Pct_Rank and rank tge price descending by Sector in percentile rank


# Print your shiny new data frame sorted by Sector A-Z and then Price_Rank Hi-Lo
sortedDf = df.sort_values(['Sector', 'Price_Rank'], ascending=[False, True])

print(sortedDf)

# # Attempt to store modified dataFrame back into SQL table
# engine = create_engine("mysql://root:curb3436ale7770dog!@localhost/stocks")
# sortedDf.to_sql(name='russell3000', con=engine, if_exists='replace')

# # Start by building your query, then executing it and storing the result in a variable
# queryCheck = f'SELECT * FROM {table_name}'
# mycursor.execute(queryCheck)

# check_result = mycursor.fetchall()
# print(check_result)
