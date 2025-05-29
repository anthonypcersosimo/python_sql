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

db_name = 'python'
table_name = 'master_tickets'

# Create a cursor (an instance) to manipulate your SQL Database
mycursor = mydb.cursor(buffered=True)

# # Create New Database

mycursor.execute(f'CREATE DATABASE {db_name}')
mycursor.execute('SHOW DATABASES')
for x in mycursor:
    print(x)

drop_query = f'DROP TABLE IF EXISTS {table_name}'
create_query = f'CREATE TABLE {table_name} (snam CHAR(20) NOT NULL, trade_order CHAR(20), ticker CHAR(10))'

# Create new Table
mycursor.execute(drop_query)
mycursor.execute(create_query)

mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)