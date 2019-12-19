import sqlite3
import mysql.connector
print('connected!')

f=open("secret.txt","r")
if f.mode == "r":
    secret = f.read() 

mydb = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    db='ecs',
    use_unicode='true',
    username='root',
    passwd=secret
)
print(mydb)

db_name = 'ecs'
table_name = 'sn_buy_rated'

# Create a cursor (an instance) to manipulate your SQL Database
mycursor = mydb.cursor(buffered=True)

# # Create New Database
# mycursor.execute(f'CREATE DATABASE {db_name}')
# mycursor.execute('SHOW DATABASES')
# for x in mycursor:
#     print(x)

# Create new Table
mycursor.execute('')