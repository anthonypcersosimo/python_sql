import sqlite3
import mysql.connector
print('connected!')

f=open("secret.txt","r")
if f.mode == "r":
    secret = f.read() 

mydb = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    db='stocks',
    use_unicode='true',
    username='root',
    passwd=secret
)
print(mydb)
table_name = 'russell3000'

# Create a cursor (an instance) to manipulate your SQL Database
mycursor = mydb.cursor(buffered=True)

# Print a list of all avail databases for given PORT and HOST above
# mycursor.execute('SHOW DATABASES')
# for x in mycursor:
#     print(x)

# # SELECT DATA FROM DATABASE ===========================
# Select all the data from a table
print('Select all the data from a table')
mycursor.execute('SELECT * FROM ' + table_name)

store_result = mycursor.fetchall()

for x in store_result:
    print(x)
print('==================================================')

# Select all data from specific columns
print('Select all data from specific columns')
mycursor.execute('SELECT Ticker, Price FROM ' + table_name)

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
select_query = 'SELECT * FROM ' + table_name + ' WHERE Sector = "Gas"'

mycursor.execute(select_query)

select_where_result = mycursor.fetchall()

for x in select_where_result:
    print(x)
print('==================================================')


# Select records from column where items CONTAIN (params)
print('Select records from column where items CONTAIN (params)')
select_params_query = ('SELECT * FROM ' + table_name +
                       ' WHERE Sector LIKE "%als%"')

mycursor.execute(select_params_query)

select_params_result = mycursor.fetchall()

for x in select_params_result:
    print(x)
