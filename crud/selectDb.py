import sqlite3
import mysql.connector
print('connected!')

f=open("secret.txt","r")
if f.mode == "r":
    secret = f.read() 

mydb = mysql.connector.connect(
    user='root',
    password=secret,
    host='127.0.0.1',
    database='python'
)
print(mydb)
table_name = 'master_tickets'

# Create a cursor (an instance) to manipulate your SQL Database
mycursor = mydb.cursor(buffered=True)

# Print a list of all avail databases for given PORT and HOST above
# mycursor.execute('SHOW DATABASES')
# for x in mycursor:
#     print(x)

# # SELECT DATA FROM DATABASE ===========================
# Select all the data from a table
# print('Select all the data from a table')
# mycursor.execute('SELECT * FROM ' + table_name)

# store_result = mycursor.fetchall()

# for x in store_result:
#     print(x)
# print('==================================================')

# Select all data from specific columns
print('Select all data from specific columns')
mycursor.execute('SELECT ticker, notes FROM ' + table_name + ' LIMIT 10')

select_all_result = mycursor.fetchall()

for x in select_all_result:
    print(x)
print('==================================================')


# Selecting only one row from table
print('Selecting only one row from table')
mycursor.execute('SELECT * FROM ' + table_name)

single_result = mycursor.fetchone()

print(single_result)
print('==================================================')


# Selecting data WHERE (some clause)
print('Selecting data WHERE (some clause)')
select_query = 'SELECT * FROM ' + table_name + ' WHERE snam = "ZCCFI"'

mycursor.execute(select_query)

select_where_result = mycursor.fetchall()

for x in select_where_result:
    print(x)
print('==================================================')


# Select records from column where items CONTAIN (params)
print('Select records from column where items CONTAIN (params)')
select_params_query = ('SELECT * FROM ' + table_name +
                       ' WHERE ticker LIKE "%aa%"')

mycursor.execute(select_params_query)

select_params_result = mycursor.fetchall()

for x in select_params_result:
    print(x)
